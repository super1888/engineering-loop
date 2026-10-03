import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


POWERSHELL = shutil.which("powershell") or shutil.which("pwsh")


@unittest.skipUnless(POWERSHELL, "PowerShell is unavailable; native gate reproduction was not run")
class NativeCommandGateTests(unittest.TestCase):
    def test_resolved_evidence_namespace_is_checked_before_writes_or_launch(self):
        for name, actual, expected, gated in (
                ("copied prefix overwrites prior evidence", "round-a", "round-b", False),
                ("mismatch blocked before side effects", "round-a", "round-b", True),
                ("new round preserves old evidence", "round-b", "round-b", True),
                ("authorized same-round replacement", "round-a", "round-a", True)):
            with self.subTest(case=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                original = {"round-a-launch.json": b'{"round":"round-a","prior":true}\n',
                            "round-a.log": b"prior native output\n",
                            "round-a-report.json": b'{"tests":3,"passed":3}\n'}
                for path, content in original.items():
                    (root / path).write_bytes(content)
                (root / "work.py").write_text(
                    "from pathlib import Path\nPath('work-started.txt').write_text('started')\n"
                    "print('new native output')\n", encoding="utf-8")
                script = "$ErrorActionPreference = 'Stop'\n"
                script += f"$taskPrefix = '{actual}'\n"
                if gated:
                    script += "if ($taskPrefix -ne $env:LOOP_EXPECTED_EVIDENCE_PREFIX) { exit 7 }\n"
                script += (
                    "@{ round=$taskPrefix } | ConvertTo-Json | "
                    "Set-Content -LiteralPath ($taskPrefix + '-launch.json') -Encoding utf8\n"
                    "& $env:LOOP_NATIVE_GATE_PYTHON work.py > ($taskPrefix + '.log')\n"
                    "exit $LASTEXITCODE\n")
                runner = root / f"{expected}.ps1"
                runner.write_text(script, encoding="utf-8")
                result = subprocess.run(
                    [POWERSHELL, "-NoProfile", "-NonInteractive", "-File", str(runner)], cwd=root,
                    env={**os.environ, "LOOP_NATIVE_GATE_PYTHON": sys.executable,
                         "LOOP_EXPECTED_EVIDENCE_PREFIX": expected},
                    capture_output=True, text=True, timeout=15,
                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                blocked = gated and actual != expected
                self.assertEqual(result.returncode, 7 if blocked else 0, result.stdout + result.stderr)
                self.assertEqual((root / "work-started.txt").exists(), not blocked)
                for path in ("round-a-launch.json", "round-a.log"):
                    if blocked or actual != "round-a":
                        self.assertEqual((root / path).read_bytes(), original[path])
                    else:
                        self.assertNotEqual((root / path).read_bytes(), original[path])
                self.assertEqual((root / "round-a-report.json").read_bytes(), original["round-a-report.json"])
                for path in ("round-b-launch.json", "round-b.log"):
                    self.assertEqual((root / path).exists(), not blocked and actual == "round-b")

    def test_failed_prerequisite_stops_dependent_steps_and_expected_failure_can_continue(self):
        for name, status, expected, gated in (
                ("masked failure", 7, 0, False),
                ("unexpected failure", 7, 0, True),
                ("successful prerequisite", 0, 0, True),
                ("expected negative check", 7, 7, True),
                ("negative check unexpectedly succeeds", 0, 7, True)):
            with self.subTest(case=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "prerequisite.py").write_text(f"import sys\nsys.exit({status})\n", encoding="utf-8")
                for stage, content in (("artifact", "changed"), ("verification", "started")):
                    (root / f"{stage}.py").write_text(
                        f"from pathlib import Path\nPath('{stage}.txt').write_text('{content}')\n", encoding="utf-8")
                script = "$ErrorActionPreference = 'Stop'\n"
                script += "& $env:LOOP_NATIVE_GATE_PYTHON prerequisite.py\n"
                if gated:
                    script += ("$taskNativeExit = $LASTEXITCODE\n"
                               f"if ($taskNativeExit -ne {expected}) {{\n"
                               "  if ($taskNativeExit -eq 0) { exit 1 }\n"
                               "  exit $taskNativeExit\n}\n")
                script += ("& $env:LOOP_NATIVE_GATE_PYTHON artifact.py\n"
                           "& $env:LOOP_NATIVE_GATE_PYTHON verification.py\n"
                           "exit $LASTEXITCODE\n")
                (root / "commands.ps1").write_text(script, encoding="utf-8")
                result = subprocess.run([POWERSHELL, "-NoProfile", "-NonInteractive", "-File", str(root / "commands.ps1")],
                    cwd=root, env={**os.environ, "LOOP_NATIVE_GATE_PYTHON": sys.executable},
                    capture_output=True, text=True, timeout=15,
                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                blocked = gated and status != expected
                self.assertEqual(result.returncode, (status or 1) if blocked else 0, result.stdout + result.stderr)
                self.assertEqual((root / "artifact.txt").exists(), not blocked)
                self.assertEqual((root / "verification.txt").exists(), not blocked)


if __name__ == "__main__":
    unittest.main()
