from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from record_convention_trial import run_result
from convention_oracle import assess
import prepare_convention_trial
import prepare_bar_trial
import prepare_routing_trial


class ConventionRecorderTests(unittest.TestCase):
    def test_input_hashes_ignore_cache_inside_the_root_only(self):
        with tempfile.TemporaryDirectory() as directory:
            for ancestor in ("ordinary", "__pycache__", ".git"):
                root = Path(directory) / ancestor / "inputs"
                root.mkdir(parents=True)
                (root / "context.md").write_bytes(b"Frozen context.\n")
                (root / "__pycache__").mkdir()
                (root / "__pycache__/cached.md").write_bytes(b"Disposable cache.\n")
                (root / "local.pyc").write_bytes(b"Disposable bytecode.\n")
                for module in (prepare_convention_trial, prepare_bar_trial, prepare_routing_trial):
                    with self.subTest(ancestor=ancestor, preparer=module.__name__):
                        self.assertEqual(list(module.hashes(root)), ["context.md"])

    def test_skill_snapshot_preserves_native_paths_and_committed_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repository"
            skill = root / "skills/engineering-loop"
            contents = {Path("SKILL.md"): b"entry\n",
                        Path("references/plain.md"): b"plain\r\nwithout final newline",
                        Path("references/说明 空格.md"): "冻结内容\n".encode("utf-8")}
            for relative, content in contents.items():
                path = skill / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            for command in (["git", "init", "--quiet"], ["git", "config", "core.autocrlf", "false"],
                            ["git", "config", "core.quotepath", "true"], ["git", "add", "."],
                            ["git", "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid",
                             "commit", "--quiet", "-m", "Frozen skill"]):
                subprocess.run(command, cwd=root, check=True, capture_output=True)
            for relative in contents:
                (skill / relative).write_bytes(b"uncommitted replacement\n")
            (skill / "references/untracked.md").write_bytes(b"not in revision\n")
            snapshot = Path(directory) / "snapshot"
            with patch.object(prepare_convention_trial, "ROOT", root):
                prepare_convention_trial.copy_skill_revision("HEAD", snapshot)
            self.assertEqual({path.relative_to(snapshot): path.read_bytes()
                              for path in snapshot.rglob("*") if path.is_file()}, contents)

    def test_patch_uses_the_trial_baseline_instead_of_the_current_template(self):
        with tempfile.TemporaryDirectory() as directory:
            trial = Path(directory) / "__pycache__" / ".git" / "trial"
            workspace = trial / "workspace"
            shutil.copytree(ROOT / "evals/fixtures/convention-boundary", workspace,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            order_document = workspace / "ORDER.md"
            order_document.write_text(order_document.read_text(encoding="utf-8")
                                      + "\nFrozen trial context.\n", encoding="utf-8")
            baseline_document = order_document.read_bytes()
            empty_document = workspace / "empty-before.md"
            empty_document.write_bytes(b"")
            binary_baseline = {"encoded-edit.md": "Before edit\n".encode("utf-16"),
                               "encoded-delete.md": "Before delete\n".encode("utf-16")}
            for name, content in binary_baseline.items():
                (workspace / name).write_bytes(content)
            for command in (["git", "init", "--quiet"], ["git", "config", "core.autocrlf", "false"],
                            ["git", "add", "."],
                            ["git", "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid",
                             "commit", "--quiet", "-m", "Frozen baseline"]):
                subprocess.run(command, cwd=workspace, check=True, capture_output=True)
            (trial / "evidence").mkdir()
            (trial / "evidence/events.jsonl").write_text(
                json.dumps({"type": "item.completed", "item": {"type": "agent_message",
                           "text": "A stable table. " + str(workspace)}}) + "\n"
                + json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
            output = trial / "recorded"
            output.mkdir()

            previous = Path.cwd()
            try:
                os.chdir(trial.parent)
                unchanged = run_result(Path(trial.name), output, "amount-A")
            finally:
                os.chdir(previous)
            self.assertEqual((output / "amount-A-final.txt").read_text(encoding="utf-8"),
                             "A stable table. " + str(workspace).replace(str(trial.parent), "<trial-root>") + "\n")
            self.assertEqual(unchanged["changed_files"], [])
            self.assertEqual((output / "amount-A.patch").read_text(encoding="utf-8"), "")

            constants = workspace / "order_constants.py"
            baseline_constants = constants.read_bytes()
            constants.write_text(constants.read_text(encoding="utf-8").replace("10_000", "15_000"),
                                 encoding="utf-8")
            changed = run_result(trial, output, "amount-B")
            self.assertEqual(changed["changed_files"], ["order_constants.py"])
            self.assertEqual(changed["oracle_failures"], [])
            patch = (output / "amount-B.patch").read_text(encoding="utf-8")
            self.assertIn("-MAX_ORDER_TOTAL_CENTS = 10_000", patch)
            self.assertIn("+MAX_ORDER_TOTAL_CENTS = 15_000", patch)

            valid_constants = constants.read_text(encoding="utf-8")
            constants.write_text(valid_constants.rstrip("\n"), encoding="utf-8", newline="\n")
            without_newline = run_result(trial, output, "amount-D")
            self.assertEqual(without_newline["oracle_failures"], [])
            reverse_check = subprocess.run(
                ["git", "apply", "--reverse", "--check", str(output / "amount-D.patch")],
                cwd=workspace, capture_output=True, text=True)
            self.assertEqual(reverse_check.returncode, 0, reverse_check.stderr)
            constants.write_text(valid_constants, encoding="utf-8", newline="\n")

            order_document.unlink()
            empty_document.unlink()
            (workspace / "extra.py").write_text("VALUE = 1\n", encoding="utf-8")
            (workspace / "empty-after.py").write_bytes(b"")
            (workspace / "__pycache__").mkdir()
            (workspace / "__pycache__/cached.md").write_bytes(b"Disposable cache.\n")
            binary_candidate = {"encoded-edit.md": "After edit\n".encode("utf-16"),
                                "新增 编码.md": "Added document\n".encode("utf-16")}
            for name, content in binary_candidate.items():
                (workspace / name).write_bytes(content)
            (workspace / "encoded-delete.md").unlink()
            added_and_deleted = run_result(trial, output, "amount-C")
            self.assertEqual(added_and_deleted["oracle_failures"], [])
            self.assertCountEqual(added_and_deleted["changed_files"],
                                  ["ORDER.md", "extra.py", "order_constants.py", "empty-before.md",
                                   "empty-after.py", "encoded-edit.md", "encoded-delete.md", "新增 编码.md"])
            patch = (output / "amount-C.patch").read_text(encoding="utf-8")
            self.assertIn("-Frozen trial context.", patch)
            self.assertIn("+VALUE = 1", patch)
            replay = trial / "replay"
            subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(workspace), str(replay)],
                           check=True, capture_output=True)
            applied = subprocess.run(["git", "apply", str(output / "amount-C.patch")], cwd=replay,
                                     capture_output=True)
            self.assertEqual(applied.returncode, 0, applied.stderr.decode("utf-8", errors="replace"))
            self.assertEqual(assess(replay), [])
            for name, content in binary_candidate.items():
                self.assertEqual((replay / name).read_bytes(), content)
            self.assertFalse((replay / "encoded-delete.md").exists())
            subprocess.run(["git", "apply", "--reverse", str(output / "amount-C.patch")],
                           cwd=workspace, check=True, capture_output=True)
            self.assertFalse((workspace / "extra.py").exists())
            self.assertFalse((workspace / "empty-after.py").exists())
            self.assertEqual(empty_document.read_bytes(), b"")
            self.assertEqual(order_document.read_bytes(), baseline_document)
            self.assertEqual(constants.read_bytes(), baseline_constants)
            for name, content in binary_baseline.items():
                self.assertEqual((workspace / name).read_bytes(), content)
            self.assertFalse((workspace / "新增 编码.md").exists())
            self.assertEqual(subprocess.check_output(["git", "diff", "--cached", "--name-only"],
                                                    cwd=workspace), b"")


if __name__ == "__main__":
    unittest.main()
