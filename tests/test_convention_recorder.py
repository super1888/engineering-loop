from pathlib import Path
from contextlib import redirect_stdout
import hashlib
import io
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
import prepare_async_import_trial
import record_convention_trial


class ConventionRecorderTests(unittest.TestCase):
    def test_style_skill_is_frozen_and_recorded_instead_of_read_from_its_source(self):
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory) / "repository"
            skill = repository / "skills/engineering-loop"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_bytes(b"Synthetic entry.\n")
            for command in (["git", "init", "--quiet"], ["git", "add", "."],
                            ["git", "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid",
                             "commit", "--quiet", "-m", "Inputs"]):
                subprocess.run(command, cwd=repository, check=True, capture_output=True)
            style = Path(directory) / "风格 skill"
            contents = {"SKILL.md": b"Frozen style.\r\nNo final newline",
                        "references/说明 空格.md": "冻结约定\n".encode("utf-8"),
                        "documents/__pycache__": b"Ordinary style input.\n"}
            for name, content in contents.items():
                path = style / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            (style / "__pycache__").mkdir()
            (style / "__pycache__/cached.md").write_bytes(b"Disposable cache.\n")
            (style / "local.pyc").write_bytes(b"Disposable bytecode.\n")
            scratch = Path(directory) / "trial"
            scratch.mkdir()
            previous = Path.cwd()
            try:
                os.chdir(directory)
                with patch.object(prepare_convention_trial, "ROOT", repository), \
                        patch.object(prepare_convention_trial.tempfile, "mkdtemp", return_value=str(scratch)), \
                        patch.object(sys, "argv", ["prepare", "--baseline", "HEAD", "--style-skill", style.name]), \
                        redirect_stdout(io.StringIO()):
                    prepare_convention_trial.main()
            finally:
                os.chdir(previous)
            for name in contents:
                (style / name).write_bytes(b"Later source replacement.\n")
            snapshot = scratch / "style-skill"
            self.assertEqual({path.relative_to(snapshot).as_posix(): path.read_bytes()
                              for path in snapshot.rglob("*") if path.is_file()}, contents)
            expected_hashes = {name: hashlib.sha256(content).hexdigest() for name, content in contents.items()}
            manifest = json.loads((scratch / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["style_skill"], style.name)
            self.assertEqual(manifest["style_skill_hashes"], expected_hashes)
            self.assertEqual(len(manifest["trials"]), 4)
            for trial_id in manifest["trials"]:
                trial = scratch / trial_id
                prompt = (trial / "prompt.txt").read_text(encoding="utf-8")
                self.assertIn(str(snapshot / "SKILL.md"), prompt)
                self.assertNotIn(style.name, prompt)
                (trial / "evidence/events.jsonl").write_text(
                    json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
            output = Path(directory) / "recorded"
            with patch.object(sys, "argv", ["record", "--amount-root", str(scratch),
                    "--comment-root", str(scratch), "--style-root", str(scratch), "--output", str(output)]):
                record_convention_trial.main()
            self.assertEqual(json.loads((output / "inputs.json").read_text(encoding="utf-8"))
                             ["style_skill_hashes"], expected_hashes)
            del manifest["style_skill_hashes"]
            (scratch / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            with patch.object(sys, "argv", ["record", "--amount-root", str(scratch),
                    "--comment-root", str(scratch), "--style-root", str(scratch), "--output", str(output)]):
                record_convention_trial.main()
            self.assertIsNone(json.loads((output / "inputs.json").read_text(encoding="utf-8"))
                              ["style_skill_hashes"])

    def test_prepared_workspaces_preserve_files_named_like_cache_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory) / "repository"
            shutil.copytree(ROOT / "skills/engineering-loop", repository / "skills/engineering-loop")
            for name in ("convention-boundary", "skill-routing", "async-import"):
                fixture = repository / "evals/fixtures" / name
                shutil.copytree(ROOT / "evals/fixtures" / name, fixture)
                (fixture / "documents").mkdir()
                (fixture / "documents/__pycache__").write_bytes(b"Ordinary frozen input.\n")
                (fixture / "__pycache__").mkdir(exist_ok=True)
                (fixture / "__pycache__/cached.md").write_bytes(b"Disposable cache.\n")
                (fixture / "local.pyc").write_bytes(b"Disposable bytecode.\n")
            for name in ("async_import_oracle.py", "async_import_browser_oracle.cjs",
                         "async_import_change.md", "python_source.py"):
                shutil.copyfile(ROOT / "evals" / name, repository / "evals" / name)
            for command in (["git", "init", "--quiet"], ["git", "config", "core.autocrlf", "false"],
                            ["git", "add", "."], ["git", "-c", "user.name=Eval",
                             "-c", "user.email=eval@example.invalid", "commit", "--quiet", "-m", "Inputs"]):
                subprocess.run(command, cwd=repository, check=True, capture_output=True)
            for module, fixture, arguments, count in (
                    (prepare_convention_trial, "convention-boundary", ["--baseline", "HEAD"], 4),
                    (prepare_routing_trial, "skill-routing", ["--output"], 6),
                    (prepare_async_import_trial, "async-import", ["--output"], 2)):
                with self.subTest(preparer=module.__name__):
                    scratch = Path(directory) / module.__name__
                    scratch.mkdir()
                    args = list(arguments)
                    if module is prepare_routing_trial:
                        args.append(str(scratch))
                    elif module is prepare_async_import_trial:
                        args += [str(Path(directory) / "recorded"), "--node-modules", "unused", "--browser", "unused"]
                    with patch.object(module, "ROOT", repository), patch.object(module.tempfile, "mkdtemp", return_value=str(scratch)), \
                            patch.object(sys, "argv", [module.__name__, *args]), redirect_stdout(io.StringIO()):
                        if module is prepare_async_import_trial:
                            module.main()
                        else:
                            with patch.object(module, "FIXTURE", repository / "evals/fixtures" / fixture):
                                module.main()
                    workspaces = list(scratch.glob("*/workspace"))
                    self.assertEqual(len(workspaces), count)
                    manifest_path = (Path(directory) / "recorded/inputs.json" if module is prepare_async_import_trial
                                     else scratch / "manifest.json")
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    if module is prepare_convention_trial:
                        self.assertIsNone(manifest["style_skill_hashes"])
                        self.assertFalse((scratch / "style-skill").exists())
                    self.assertEqual(manifest["fixture_hashes"]["documents/__pycache__"],
                                     hashlib.sha256(b"Ordinary frozen input.\n").hexdigest())
                    self.assertNotIn("__pycache__/cached.md", manifest["fixture_hashes"])
                    self.assertNotIn("local.pyc", manifest["fixture_hashes"])
                    for workspace in workspaces:
                        self.assertEqual((workspace / "documents/__pycache__").read_bytes(), b"Ordinary frozen input.\n")
                        self.assertFalse((workspace / "__pycache__").exists())
                        self.assertFalse((workspace / "local.pyc").exists())
                        if module is not prepare_async_import_trial:
                            self.assertIn("documents/__pycache__", subprocess.check_output(
                                ["git", "ls-files"], cwd=workspace, text=True).splitlines())

    def test_input_hashes_ignore_cache_inside_the_root_only(self):
        with tempfile.TemporaryDirectory() as directory:
            for ancestor in ("ordinary", "__pycache__", ".git"):
                root = Path(directory) / ancestor / "inputs"
                root.mkdir(parents=True)
                (root / "context.md").write_bytes(b"Frozen context.\n")
                (root / "documents").mkdir()
                (root / "documents/__pycache__").write_bytes(b"Ordinary input file.\n")
                (root / "__pycache__").mkdir()
                (root / "__pycache__/cached.md").write_bytes(b"Disposable cache.\n")
                (root / "local.pyc").write_bytes(b"Disposable bytecode.\n")
                for module in (prepare_convention_trial, prepare_bar_trial, prepare_routing_trial):
                    with self.subTest(ancestor=ancestor, preparer=module.__name__):
                        self.assertEqual(module.hashes(root), {
                            "context.md": hashlib.sha256(b"Frozen context.\n").hexdigest(),
                            "documents/__pycache__": hashlib.sha256(b"Ordinary input file.\n").hexdigest(),
                        })

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
