from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from record_convention_trial import run_result


class ConventionRecorderTests(unittest.TestCase):
    def test_patch_uses_the_trial_baseline_instead_of_the_current_template(self):
        with tempfile.TemporaryDirectory() as directory:
            trial = Path(directory)
            workspace = trial / "workspace"
            shutil.copytree(ROOT / "evals/fixtures/convention-boundary", workspace,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            order_document = workspace / "ORDER.md"
            order_document.write_text(order_document.read_text(encoding="utf-8")
                                      + "\nFrozen trial context.\n", encoding="utf-8")
            for command in (["git", "init", "--quiet"], ["git", "config", "core.autocrlf", "false"],
                            ["git", "add", "."],
                            ["git", "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid",
                             "commit", "--quiet", "-m", "Frozen baseline"]):
                subprocess.run(command, cwd=workspace, check=True, capture_output=True)
            (trial / "evidence").mkdir()
            (trial / "evidence/events.jsonl").write_text(
                json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
            output = trial / "recorded"
            output.mkdir()

            unchanged = run_result(trial, output, "amount-A")
            self.assertEqual(unchanged["changed_files"], [])
            self.assertEqual((output / "amount-A.patch").read_text(encoding="utf-8"), "")

            constants = workspace / "order_constants.py"
            constants.write_text(constants.read_text(encoding="utf-8").replace("10_000", "15_000"),
                                 encoding="utf-8")
            changed = run_result(trial, output, "amount-B")
            self.assertEqual(changed["changed_files"], ["order_constants.py"])
            self.assertEqual(changed["oracle_failures"], [])
            patch = (output / "amount-B.patch").read_text(encoding="utf-8")
            self.assertIn("-MAX_ORDER_TOTAL_CENTS = 10_000", patch)
            self.assertIn("+MAX_ORDER_TOTAL_CENTS = 15_000", patch)

            order_document.unlink()
            (workspace / "extra.py").write_text("VALUE = 1\n", encoding="utf-8")
            added_and_deleted = run_result(trial, output, "amount-C")
            self.assertCountEqual(added_and_deleted["changed_files"],
                                  ["ORDER.md", "extra.py", "order_constants.py"])
            patch = (output / "amount-C.patch").read_text(encoding="utf-8")
            self.assertIn("-Frozen trial context.", patch)
            self.assertIn("+VALUE = 1", patch)


if __name__ == "__main__":
    unittest.main()
