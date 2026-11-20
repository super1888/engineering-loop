# /// script
# requires-python = ">=3.12"
# dependencies = ["alibabacloud-dyvmsapi20170525==5.3.0"]
# ///

"""Call one number with an approved recording and save the call result."""

import argparse
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile
import time
from uuid import uuid4


RESULTS_DIR = Path(__file__).resolve().parent / "results"
BEIJING = timezone(timedelta(hours=8))
VOICE_NOTIFICATION_PRODUCT = 11000000300006
CONNECTED_CODES = {"200000", "200001"}
UNCONNECTED_CODES = {
    "502", "200002", "200003", "200004", "200005", "200007", "200010", "200011",
    "200104", "200117", "200118", "200119", "200121",
}


class DemoError(Exception):
    """A message that can be printed without exposing credentials or numbers."""


class VoiceService:
    def __init__(self):
        key_id = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
        secret = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        if not key_id or not secret:
            raise DemoError("请设置 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。")

        try:
            from alibabacloud_dyvmsapi20170525 import models
            from alibabacloud_dyvmsapi20170525.client import Client
            from alibabacloud_tea_openapi.models import Config
            from darabonba.policy.retry import RetryOptions
            from darabonba.runtime import RuntimeOptions
        except ImportError:
            raise DemoError("请使用 uv run voice_demo.py 运行，uv 会安装阿里云 SDK。") from None

        token = os.environ.get("ALIBABA_CLOUD_SECURITY_TOKEN") or None
        self.client = Client(Config(
            endpoint="dyvmsapi.aliyuncs.com",
            type="sts" if token else "access_key",
            access_key_id=key_id,
            access_key_secret=secret,
            security_token=token,
            retry_options=RetryOptions(retryable=False),
        ))
        self.models = models
        self.runtime = RuntimeOptions(connect_timeout=5_000, read_timeout=10_000)

    def dial(self, phone, voice_code, caller):
        request = self.models.SingleCallByVoiceRequest(
            called_number=phone,
            called_show_number=caller,
            voice_code=voice_code,
            play_times=1,
        )
        return self.client.single_call_by_voice_with_options(request, self.runtime).body

    def query(self, call_id, query_date_ms):
        request = self.models.QueryCallDetailByCallIdRequest(
            call_id=call_id,
            prod_id=VOICE_NOTIFICATION_PRODUCT,
            query_date=query_date_ms,
        )
        return self.client.query_call_detail_by_call_id_with_options(request, self.runtime).body


def beijing_day_ms(when):
    day = when.astimezone(BEIJING).replace(hour=0, minute=0, second=0, microsecond=0)
    return int(day.timestamp()) * 1_000


def summarize_detail(data):
    detail = json.loads(data) if isinstance(data, str) and data else data
    if not detail:
        return None
    if not isinstance(detail, dict):
        raise DemoError("阿里云返回的话单格式无法解析。")

    state = str(detail.get("state") or "")
    if state in {"", "200"}:
        return None
    completed = (
        state in CONNECTED_CODES or state in UNCONNECTED_CODES or detail.get("endDate")
    )
    duration = detail.get("duration")
    if not completed or duration is None or duration == "":
        return None
    if not re.fullmatch(r"[0-9]+", str(duration)):
        raise DemoError("阿里云返回的通话时长无法解析。")

    seconds = int(duration)
    answered = bool(detail.get("startDate") or seconds > 0 or state in CONNECTED_CODES)
    return {
        "status": "已接通" if answered else "未接通",
        "answered": answered,
        "duration_seconds": seconds,
        "carrier_state": state,
    }


def save_record(path, record):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False)
    temp_path = Path(temp.name)
    try:
        with temp:
            json.dump(record, temp, ensure_ascii=False, indent=2)
            temp.write("\n")
        temp_path.replace(path)
    finally:
        temp_path.unlink(missing_ok=True)


def sdk_error_code(error):
    source = getattr(error, "inner_exception", None) or error
    return getattr(source, "code", None) or type(source).__name__


def query_result(service, path, record, wait_seconds):
    deadline = time.monotonic() + wait_seconds
    while True:
        try:
            body = service.query(record["call_id"], record["query_date_ms"])
        except Exception as error:
            raise DemoError(f"查询话单失败（{sdk_error_code(error)}）。可用 result 续查。") from None
        if body is None or body.code != "OK":
            code = body.code if body else "无响应"
            raise DemoError(f"查询话单失败（{code}）。可用 result 续查。")

        summary = summarize_detail(body.data)
        if summary is not None:
            record.update(summary)
            save_record(path, record)
            return

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            print("话单尚未生成。通话结束 3–5 分钟后可用 result 续查。", file=sys.stderr)
            return
        time.sleep(min(10, remaining))


def call(args):
    voice_code = args.voice_code.strip()
    if not voice_code:
        raise DemoError("请输入审核通过的语音文件 ID。")
    service = VoiceService()
    started = datetime.now(BEIJING)
    path = RESULTS_DIR / f"call-{uuid4().hex}.json"
    record = {
        "status": "提交结果待确认",
        "call_id": None,
        "requested_at": started.isoformat(timespec="seconds"),
        "query_date_ms": beijing_day_ms(started),
        "answered": None,
        "duration_seconds": None,
    }
    save_record(path, record)
    print(f"话单文件 {path}", file=sys.stderr, flush=True)
    try:
        body = service.dial(args.phone, voice_code, args.caller)
    except Exception as error:
        raise DemoError(
            f"提交结果待确认（{sdk_error_code(error)}）。请先在阿里云控制台核对呼叫记录。"
        ) from None

    if body is not None and body.code and body.code != "OK":
        record.update(status="发起失败", provider_code=body.code)
        save_record(path, record)
        raise DemoError(f"阿里云拒绝了呼叫请求（{body.code}）。")
    if body is None or body.code != "OK" or not body.call_id:
        raise DemoError("阿里云未返回呼叫 ID。请先在控制台核对呼叫记录。")

    print(f"呼叫已受理，CallId {body.call_id}", file=sys.stderr, flush=True)
    record.update(status="待话单", call_id=body.call_id)
    save_record(path, record)
    if args.wait:
        query_result(service, path, record, args.wait)
    return record


def result(args):
    record = json.loads(args.record.read_text(encoding="utf-8"))
    if not isinstance(record, dict) or not record.get("call_id") or not record.get("query_date_ms"):
        raise DemoError("文件中缺少 CallId 或查询日期。请在阿里云控制台核对呼叫记录。")
    if record.get("answered") is None:
        query_result(VoiceService(), args.record, record, args.wait)
    return record


def simulate(args):
    detail = (
        {"state": "200003", "duration": 0}
        if args.missed else {"state": "200001", "duration": 8}
    )
    return {"simulated": True, **summarize_detail(detail)}


def phone_number(value):
    if not re.fullmatch(r"1[0-9]{10}", value):
        raise argparse.ArgumentTypeError("请输入 11 位中国内地手机号。")
    return value


def seconds_to_wait(value):
    seconds = int(value)
    if seconds < 0:
        raise argparse.ArgumentTypeError("等待秒数应为 0 或正整数。")
    return seconds


def main(argv=None):
    parser = argparse.ArgumentParser(description="阿里云预录语音通知试拨")
    commands = parser.add_subparsers(required=True)
    mock = commands.add_parser("simulate", help="查看模拟话单")
    mock.add_argument("--missed", action="store_true", help="模拟无人接听")
    mock.set_defaults(run=simulate)

    live = commands.add_parser("call", help="拨打一通真实电话")
    live.add_argument("--phone", required=True, type=phone_number, help="中国内地手机号")
    live.add_argument("--voice-code", required=True, help="审核通过的语音文件 ID")
    live.add_argument("--caller", help="专属模式的主叫号码或服务实例 ID")
    live.add_argument("--wait", type=seconds_to_wait, default=300, help="等待话单的秒数，0 为仅提交")
    live.set_defaults(run=call)

    lookup = commands.add_parser("result", help="按本地文件中的 CallId 查询或读取话单")
    lookup.add_argument("record", type=Path, help="call 命令输出的话单文件")
    lookup.add_argument("--wait", type=seconds_to_wait, default=0, help="等待秒数，0 为仅查询一次")
    lookup.set_defaults(run=result)

    args = parser.parse_args(argv)
    try:
        report = args.run(args)
    except (DemoError, OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print(
            "\n已停止。拿到 CallId 后可用 result 续查，提交结果待确认时可查阿里云控制台。",
            file=sys.stderr,
        )
        return 130

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
