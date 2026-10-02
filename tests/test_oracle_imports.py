from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OracleImportTests(unittest.TestCase):
    def test_contract_checks_cannot_be_bypassed_by_an_import_exit(self):
        for fixture, oracle, module, tests in (
                ("receipt", "receipt_oracle.py", "inventory.py", 7),
                ("async-import", "async_import_oracle.py", "backend/service.py", 8)):
            with self.subTest(oracle=oracle), tempfile.TemporaryDirectory() as directory:
                candidate = Path(directory) / "candidate"
                shutil.copytree(ROOT / "evals/fixtures" / fixture, candidate,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                command = [sys.executable, str(ROOT / "evals" / oracle), str(candidate)]
                baseline = subprocess.run(command, capture_output=True, text=True, timeout=30)
                self.assertEqual(baseline.returncode, 1, baseline.stderr)
                self.assertIn(f"Ran {tests} tests", baseline.stderr)
                for code in (0, 1):
                    with self.subTest(exit_code=code):
                        exit_candidate = Path(directory) / f"exit-{code}"
                        shutil.copytree(ROOT / "evals/fixtures" / fixture, exit_candidate,
                                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                        (exit_candidate / module).write_text(f"raise SystemExit({code})\n", encoding="utf-8")
                        result = subprocess.run(command[:-1] + [str(exit_candidate)],
                                                capture_output=True, text=True, timeout=30)
                        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                        self.assertIn("Candidate import exited before checks", result.stderr)


if __name__ == "__main__":
    unittest.main()
