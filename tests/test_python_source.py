from pathlib import Path
import json
import os
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from convention_oracle import assess, assess_comment_control
from record_routing_trial import record
from python_source import fresh_python


def replace_with_timestamp_collision(path, before, after):
    source = path.read_text(encoding="utf-8")
    path.write_text(source, encoding="utf-8", newline="\n")
    cache = Path(py_compile.compile(str(path), doraise=True,
                 invalidation_mode=py_compile.PycInvalidationMode.TIMESTAMP))
    stamp = path.stat()
    path.write_text(source.replace(before, after), encoding="utf-8", newline="\n")
    assert path.stat().st_size == stamp.st_size
    os.utime(path, ns=(stamp.st_atime_ns, stamp.st_mtime_ns))
    return cache, cache.read_bytes(), path.read_bytes()


class PythonSourceTests(unittest.TestCase):
    def test_browser_server_unicode_logs_do_not_prevent_port_announcement(self):
        with tempfile.TemporaryDirectory() as directory:
            trial = Path(directory)
            candidate = trial / "candidate"
            shutil.copytree(ROOT / "evals/fixtures/async-import", candidate,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            fake_modules = trial / "node_modules/playwright"
            fake_modules.mkdir(parents=True)
            (fake_modules / "index.js").write_text(
                "exports.chromium = { launch() { throw Error('Reached browser launch control'); } };\n",
                encoding="utf-8")
            env = {**os.environ, "NODE_PATH": str(fake_modules.parent),
                   "EVAL_PYTHON": sys.executable, "EVAL_BROWSER_EXECUTABLE": sys.executable,
                   "PYTHONIOENCODING": "gbk"}
            command = ["node", str(ROOT / "evals/async_import_browser_oracle.cjs"), str(candidate)]
            path = candidate / "backend/service.py"
            original = path.read_bytes()
            for log in (b"", '\nprint("启动日志✓")\n'.encode("utf-8")):
                with self.subTest(logged=bool(log)):
                    path.write_bytes(original + log)
                    result = subprocess.run(command, capture_output=True, encoding="utf-8",
                                            env=env, timeout=30)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    report = json.loads(result.stdout)
                    self.assertFalse(report["passed"])
                    self.assertIn("Reached browser launch control", report["error"])
                    self.assertNotIn("UnicodeEncodeError", report["error"])
                    self.assertEqual(path.read_bytes(), original + log)

    def test_import_cache_settings_are_restored_after_an_exception(self):
        previous = sys.pycache_prefix, sys.dont_write_bytecode
        with self.assertRaisesRegex(RuntimeError, "import failed"):
            with fresh_python() as python:
                cache = Path(sys.pycache_prefix)
                self.assertTrue(cache.is_dir())
                self.assertTrue(sys.dont_write_bytecode)
                self.assertEqual(python[-1], f"pycache_prefix={cache}")
                raise RuntimeError("import failed")
        self.assertEqual((sys.pycache_prefix, sys.dont_write_bytecode), previous)
        self.assertFalse(cache.exists())

    def test_convention_probes_execute_current_source_with_same_size_and_timestamp(self):
        for mode in ("amount", "comment"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                workspace = Path(directory) / "workspace"
                shutil.copytree(ROOT / "evals/fixtures/convention-boundary", workspace,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                constants = workspace / "order_constants.py"
                if mode == "amount":
                    constants.write_text(constants.read_text().replace("10_000", "15_000"), encoding="utf-8")
                orders = workspace / "orders.py"
                orders.write_text(orders.read_text().replace(
                    "    # References are always uppercase.\n", ""), encoding="utf-8")
                cache, cached, source = replace_with_timestamp_collision(
                    orders, "<= MAX_ORDER_TOTAL_CENTS", ">= MAX_ORDER_TOTAL_CENTS")
                failures = (assess if mode == "amount" else assess_comment_control)(workspace)
                self.assertTrue(any("Behavior check failed" in item or "boundary changed" in item
                                    for item in failures), failures)
                self.assertEqual(cache.read_bytes(), cached)
                self.assertEqual(orders.read_bytes(), source)

    def test_public_python_reports_execute_current_test_source(self):
        for mode, fixture, test_folder in (("comment", "convention-boundary", "tests"),
                                           ("routing", "skill-routing", "backend/tests")):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                trial = Path(directory)
                workspace = trial / "workspace"
                shutil.copytree(ROOT / "evals/fixtures" / fixture, workspace,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                tests = workspace / test_folder / "test_orders.py"
                tests.write_text("import unittest\nclass SourceTest(unittest.TestCase):\n"
                                 "    def test_current_source(self): self.assertTrue(True)\n", encoding="utf-8")
                cache, cached, source = replace_with_timestamp_collision(tests, "True)", "None)")
                if mode == "comment":
                    orders = workspace / "orders.py"
                    orders.write_text(orders.read_text().replace(
                        "    # References are always uppercase.\n", ""), encoding="utf-8")
                    self.assertTrue(any("Public behavior failed" in failure
                                        for failure in assess_comment_control(workspace)))
                else:
                    for command in (["git", "init", "--quiet"], ["git", "add", "."],
                                    ["git", "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid",
                                     "commit", "--quiet", "-m", "Baseline"]):
                        subprocess.run(command, cwd=workspace, check=True, capture_output=True)
                    (trial / "evidence").mkdir()
                    (trial / "evidence/events.jsonl").write_text(
                        json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
                    output = trial / "recorded"
                    output.mkdir()
                    self.assertFalse(record(trial, output, "backend-A")["public_backend_pass"])
                self.assertEqual(cache.read_bytes(), cached)
                self.assertEqual(tests.read_bytes(), source)

    def test_native_oracles_and_browser_server_import_current_candidate_source(self):
        for mode, fixture, module in (("receipt", "receipt", "inventory.py"),
                                     ("async", "async-import", "backend/service.py"),
                                     ("routing", "skill-routing", "backend/orders.py"),
                                     ("browser", "async-import", "backend/service.py")):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                trial = Path(directory)
                workspace = trial / "workspace"
                shutil.copytree(ROOT / "evals/fixtures" / fixture, workspace,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                path = workspace / module
                path.write_text("raise RuntimeError('stale-source')\n", encoding="utf-8")
                cache, cached, source = replace_with_timestamp_collision(path, "stale-source", "fresh-source")
                if mode == "browser":
                    fake_modules = trial / "node_modules/playwright"
                    fake_modules.mkdir(parents=True)
                    (fake_modules / "index.js").write_text(
                        "exports.chromium = { launch() { throw Error('Browser must not launch'); } };\n",
                        encoding="utf-8")
                    command = ["node", str(ROOT / "evals/async_import_browser_oracle.cjs"), str(workspace)]
                    env = {**os.environ, "NODE_PATH": str(fake_modules.parent),
                           "EVAL_PYTHON": sys.executable, "EVAL_BROWSER_EXECUTABLE": sys.executable}
                else:
                    oracle = {"receipt": "receipt_oracle.py", "async": "async_import_oracle.py",
                              "routing": "routing_oracle.py"}[mode]
                    command = [sys.executable, str(ROOT / "evals" / oracle), str(workspace)]
                    env = None
                result = subprocess.run(command, capture_output=True, text=True, env=env, timeout=30)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("fresh-source", result.stdout + result.stderr)
                self.assertNotIn("stale-source", result.stdout + result.stderr)
                self.assertEqual(cache.read_bytes(), cached)
                self.assertEqual(path.read_bytes(), source)


if __name__ == "__main__":
    unittest.main()
