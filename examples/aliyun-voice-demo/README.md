# 阿里云电话通知 Demo

用已审核的录音或专属文本模板给指定的中国内地手机号打电话。接通后播报一次并自动挂断，Demo 将线路接通状态和实际通话秒数保存到本地。

## 先看模拟结果

在仓库根目录用 Python 3.12 运行。模拟模式只使用本地数据。

```sh
python3.12 examples/aliyun-voice-demo/voice_demo.py simulate
python3.12 examples/aliyun-voice-demo/voice_demo.py simulate --missed
```

## 实拨一通

1. 开通阿里云语音服务，完成企业资质和场景话术审核。在语音服务控制台上传 WAV 或 MP3 到「语音通知文件」，审核通过后复制语音 ID。公共号池选公共模式，使用已配置的固定主叫时选专属模式。 [开通说明](https://help.aliyun.com/zh/vms/getting-started/through-the-api-or-sdk-using-voice-notification-or-audio-captcha/) · [上传录音](https://help.aliyun.com/zh/vms/user-guide/uploading-audio-files/)
2. 在当前终端设置 `ALIBABA_CLOUD_ACCESS_KEY_ID` 和 `ALIBABA_CLOUD_ACCESS_KEY_SECRET`。凭据需有 `dyvms:SingleCallByVoice` 和 `dyvms:QueryCallDetailByCallId` 权限。使用 STS 临时凭据时还要设置 `ALIBABA_CLOUD_SECURITY_TOKEN`。
3. 替换下面的手机号和语音 ID 后运行。此命令会发起一通真实电话，`uv` 会安装脚本声明的 SDK。专属模式追加 `--caller '主叫号码或服务实例ID'`。

```sh
uv run --python 3.12 examples/aliyun-voice-demo/voice_demo.py call \
  --phone '你的手机号' \
  --voice-code '审核通过的语音ID'
```

以 macOS 的 Zsh 为例，可在运行前这样输入凭据。Secret 输入时不回显。

```zsh
read -r 'ALIBABA_CLOUD_ACCESS_KEY_ID?阿里云 AccessKey ID '
read -rs 'ALIBABA_CLOUD_ACCESS_KEY_SECRET?阿里云 AccessKey Secret '
printf '\n'
export ALIBABA_CLOUD_ACCESS_KEY_ID ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

## 用带姓名的文本模板实拨

在语音服务控制台申请专属模式文本模板，在正文用 `${name}` 表示收件人姓名，最后一句以「再见」结束。模板审核通过后，使用已启用的专属主叫号码或服务实例 ID。凭据需有 `dyvms:SingleCallByTts` 和 `dyvms:QueryCallDetailByCallId` 权限。 [模板说明](https://help.aliyun.com/zh/vms/user-guide/create-a-text-to-speech-template) · [外呼接口](https://help.aliyun.com/zh/vms/developer-reference/api-dyvmsapi-2017-05-25-singlecallbytts)

```sh
uv run --python 3.12 examples/aliyun-voice-demo/voice_demo.py call \
  --phone '你的手机号' \
  --template-code '审核通过的模板ID' \
  --name '测试姓名' \
  --caller '主叫号码或服务实例ID'
```

每次只播报一遍。播完后阿里云结束通话，话单可用下方的 `result` 命令续查。 [挂断规则](https://help.aliyun.com/zh/vms/support/number-using-the-faq)

## 查看话单

终端会打印 `CallId` 和 `results/` 下的 JSON 路径。接通记 `answered: true`，未接通记 `answered: false` 和 `duration_seconds: 0`。话单未生成时，这两个字段保留为 `null`。

默认最多等待约 5 分钟。如果话单仍待生成，用打印出来的路径运行下面的命令，会继续查询同一通电话。调用 `call --wait 0` 可在取得 `CallId` 后立即退出。

```sh
uv run --python 3.12 examples/aliyun-voice-demo/voice_demo.py result '终端打印的JSON路径'
```

如果提交超时或未拿到 `CallId`，先在阿里云控制台核对呼叫记录，再决定是否重新拨打。话单记录的是运营商线路是否接通。 [呼叫详情 API](https://help.aliyun.com/zh/vms/developer-reference/api-dyvmsapi-2017-05-25-querycalldetailbycallid) · [话单延迟说明](https://help.aliyun.com/zh/vms/support/api-sdk-faq)
