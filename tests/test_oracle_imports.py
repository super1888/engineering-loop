from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OracleImportTests(unittest.TestCase):
    def test_unicode_candidate_logs_do_not_prevent_cli_contract_checks(self):
        for fixture, oracle, module, count in (
                ("receipt", "receipt_oracle.py", "inventory.py", 7),
                ("async-import", "async_import_oracle.py", "backend/service.py", 8)):
            with self.subTest(oracle=oracle), tempfile.TemporaryDirectory() as directory:
                candidate = Path(directory) / "candidate"
                shutil.copytree(ROOT / "evals/fixtures" / fixture, candidate,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                command = [sys.executable, str(ROOT / "evals" / oracle), str(candidate)]
                env = {**os.environ, "PYTHONIOENCODING": "gbk"}
                baseline = subprocess.run(command, capture_output=True, env=env, timeout=30)
                self.assertEqual(baseline.returncode, 1, baseline.stderr)
                self.assertIn(f"Ran {count} tests".encode(), baseline.stderr)
                path = candidate / module
                source = path.read_bytes() + '\nprint("评测日志✓")\n'.encode("utf-8")
                path.write_bytes(source)
                logged = subprocess.run(command, capture_output=True, env=env, timeout=30)
                self.assertEqual(logged.returncode, baseline.returncode, logged.stderr)
                self.assertIn("评测日志✓".encode("utf-8"), logged.stdout)
                self.assertIn(f"Ran {count} tests".encode(), logged.stderr)
                self.assertEqual(logged.stderr.splitlines()[-1], baseline.stderr.splitlines()[-1])
                self.assertNotIn(b"UnicodeEncodeError", logged.stderr)
                self.assertEqual(path.read_bytes(), source)

    def test_receipt_oracle_loads_dataclasses_with_postponed_annotations(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "candidate"
            shutil.copytree(ROOT / "evals/fixtures/receipt", candidate,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            inventory = candidate / "inventory.py"
            source = (b"from __future__ import annotations\nfrom dataclasses import dataclass\n"
                      b"from sqlite3 import Connection\n"
                      + inventory.read_bytes().replace(
                          b"class Inventory:",
                          b"@dataclass\nclass Inventory:\n    db: Connection"))
            inventory.write_bytes(source)
            public = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
                                    cwd=candidate, capture_output=True, text=True, timeout=30)
            self.assertIn("Ran 3 tests", public.stderr)
            result = subprocess.run([sys.executable, str(ROOT / "evals/receipt_oracle.py"), str(candidate)],
                                    capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn("Ran 7 tests", result.stderr)
            self.assertNotIn("AttributeError", result.stderr)
            self.assertEqual(inventory.read_bytes(), source)

    def test_receipt_oracle_resolves_candidate_sibling_imports_from_another_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidate = root / "候选 目录"
            shutil.copytree(ROOT / "evals/fixtures/receipt", candidate,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            oracle = [sys.executable, str(ROOT / "evals/receipt_oracle.py")]
            baseline = subprocess.run(oracle + [str(candidate)], cwd=root,
                                      capture_output=True, text=True, timeout=30)
            self.assertEqual(baseline.returncode, 1, baseline.stderr)
            self.assertIn("Ran 7 tests", baseline.stderr)
            inventory = candidate / "inventory.py"
            helper = candidate / "receipt_storage.py"
            helper.write_bytes(inventory.read_bytes())
            inventory.write_bytes(b"from receipt_storage import Inventory\n")
            before = {path: path.read_bytes() for path in (inventory, helper)}
            public = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
                                    cwd=candidate, capture_output=True, text=True, timeout=30)
            self.assertIn("Ran 3 tests", public.stderr)
            for supplied_path in (str(candidate), candidate.name):
                with self.subTest(path=supplied_path):
                    result = subprocess.run(oracle + [supplied_path], cwd=root,
                                            capture_output=True, text=True, timeout=30)
                    self.assertEqual(result.returncode, baseline.returncode, result.stderr)
                    self.assertIn("Ran 7 tests", result.stderr)
                    self.assertEqual(result.stderr.splitlines()[-1], baseline.stderr.splitlines()[-1])
                    self.assertNotIn("ModuleNotFoundError", result.stderr)
            self.assertEqual({path: path.read_bytes() for path in before}, before)

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
