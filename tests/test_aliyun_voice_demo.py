from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "voice_demo", ROOT / "examples/aliyun-voice-demo/voice_demo.py",
)
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)

CALL_ID = "123456789012^987654321098"
PHONE = "13900000000"
VOICE_CODE = "recording.wav"
CALL = ["call", "--phone", PHONE, "--voice-code", VOICE_CODE]


class VoiceDemoTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.service = Mock()
        self.service.dial.return_value = SimpleNamespace(code="OK", call_id=CALL_ID)
        for change in (
            patch.object(demo, "VoiceService", return_value=self.service),
            patch.object(demo, "RESULTS_DIR", self.directory),
        ):
            change.start()
            self.addCleanup(change.stop)

    def run_cli(self, *args):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            status = demo.main(args)
        payload = stdout.getvalue()
        return status, json.loads(payload) if payload else None, stderr.getvalue()

    def saved_file(self):
        (path,) = self.directory.glob("*.json")
        return path

    def test_early_hangup_is_answered_and_saved(self):
        self.service.query.return_value = SimpleNamespace(
            code="OK", data={"state": 200001, "duration": "4"},
        )
        status, report, _ = self.run_cli(*CALL, "--caller", "057100000000")
        self.assertEqual(status, 0)
        self.assertEqual(report["call_id"], CALL_ID)
        self.assertTrue(report["answered"])
        self.assertEqual(report["duration_seconds"], 4)
        self.assertEqual(json.loads(self.saved_file().read_text()), report)
        self.service.dial.assert_called_once_with(PHONE, VOICE_CODE, "057100000000")
        self.service.query.assert_called_once_with(CALL_ID, report["query_date_ms"])

    def test_pending_report_stays_unknown_and_can_be_queried_without_redialing(self):
        _, submitted, _ = self.run_cli(*CALL, "--wait", "0")
        self.service.query.side_effect = [
            SimpleNamespace(code="OK", data=None),
            SimpleNamespace(code="OK", data='{"state":"200","duration":0}'),
            SimpleNamespace(code="OK", data='{"state":"200003","duration":0}'),
        ]
        path = self.saved_file()
        for _ in range(2):
            status, pending, _ = self.run_cli("result", str(path))
            self.assertEqual(status, 0)
            self.assertIsNone(pending["answered"])
            self.assertIsNone(pending["duration_seconds"])
            self.assertEqual(json.loads(path.read_text()), submitted)

        status, completed, _ = self.run_cli("result", str(path))
        self.assertEqual(status, 0)
        self.assertIs(completed["answered"], False)
        self.assertEqual(completed["duration_seconds"], 0)
        self.assertEqual(completed["call_id"], CALL_ID)
        self.assertEqual(json.loads(path.read_text()), completed)
        self.service.dial.assert_called_once_with(PHONE, VOICE_CODE, None)

    def test_submit_timeout_is_unknown_and_does_not_redial(self):
        self.service.dial.side_effect = TimeoutError("provider response unavailable")
        status, _, error = self.run_cli(*CALL)
        self.assertEqual(status, 1)
        self.assertIn("待确认", error)
        saved = json.loads(self.saved_file().read_text())
        self.assertIsNone(saved["call_id"])
        self.assertIsNone(saved["answered"])
        self.assertNotIn(PHONE, self.saved_file().read_text())
        self.service.dial.assert_called_once()
        self.service.query.assert_not_called()

    def test_accepted_call_id_remains_visible_if_saving_it_fails(self):
        save = demo.save_record

        def save_only_before_dial(path, record):
            if record["call_id"]:
                raise OSError("could not save accepted call")
            save(path, record)

        with patch.object(demo, "save_record", side_effect=save_only_before_dial):
            status, _, error = self.run_cli(*CALL)
        self.assertEqual(status, 1)
        self.assertIn(CALL_ID, error)
        self.assertIsNone(json.loads(self.saved_file().read_text())["call_id"])
        self.service.dial.assert_called_once()
        self.service.query.assert_not_called()

    def test_lookup_timestamp_follows_the_beijing_day(self):
        instant = datetime(2022, 11, 20, 16, 0, 1, tzinfo=timezone.utc)
        self.assertEqual(demo.beijing_day_ms(instant), 1668960000000)


if __name__ == "__main__":
    unittest.main()
