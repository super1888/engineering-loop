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
from routing_oracle import assess
from record_routing_trial import record


class RoutingOracleTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.workspace = Path(self.directory.name) / "workspace"
        shutil.copytree(ROOT / "evals/fixtures/skill-routing", self.workspace,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def test_unimplemented_baseline_fails_both_sides(self):
        failures = assess(self.workspace)
        self.assertIsNotNone(failures["backend"])
        self.assertIsNotNone(failures["form"])

    def test_silent_early_exit_processes_fail_the_cli(self):
        for exit_code, diagnostic in ((0, "Behavior checks did not reach completion"),
                                      (1, "Process exited with code 1")):
            with self.subTest(exit_code=exit_code):
                workspace = self.workspace.parent / f"exit-{exit_code}"
                shutil.copytree(self.workspace, workspace,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                (workspace / "backend/orders.py").write_text(
                    f"raise SystemExit({exit_code})\n", encoding="utf-8")
                (workspace / "ui/order-form.mjs").write_text(
                    f"export function submitOrder() {{}}\nprocess.exit({exit_code});\n", encoding="utf-8")
                result = subprocess.run([sys.executable, str(ROOT / "evals/routing_oracle.py"),
                                         str(workspace)], capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(f"backend: FAIL: {diagnostic}", result.stdout)
                self.assertIn(f"form: FAIL: {diagnostic}", result.stdout)

    def _write_valid_implementation(self):
        (self.workspace / "backend/orders.py").write_text('''def create_order(store: list[dict], payload: dict) -> dict:
    name = payload.get("item_name")
    quantity = payload.get("quantity")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("invalid name")
    if isinstance(quantity, bool) or not isinstance(quantity, int) or not 1 <= quantity <= 20:
        raise ValueError("invalid quantity")
    order = {"id": len(store) + 1, "item_name": name.strip(), "quantity": quantity}
    store.append(order)
    return order
''', encoding="utf-8")
        (self.workspace / "ui/order-form.mjs").write_text('''export async function submitOrder(fields, postJson) {
  const name = typeof fields.itemName === "string" ? fields.itemName.trim() : "";
  const quantity = Number(fields.quantity);
  if (!name || !Number.isInteger(quantity) || quantity < 1 || quantity > 20) {
    return { ok: false, error: "invalid order", fields };
  }
  const response = await postJson("/orders", { item_name: name, quantity });
  if (response.status !== 201) {
    return { ok: false, error: response.body.error, fields };
  }
  return { ok: true, order: response.body };
}
''', encoding="utf-8")

    def test_valid_backend_and_form_pass(self):
        self._write_valid_implementation()
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_form_oracle_requires_an_error_on_local_validation_failure(self):
        self._write_valid_implementation()
        form = self.workspace / "ui/order-form.mjs"
        valid = form.read_text(encoding="utf-8")
        for replacement in ('return { ok: false, fields };',
                            'return { ok: false, error: "", fields };'):
            with self.subTest(local_failure=replacement):
                form.write_text(valid.replace('return { ok: false, error: "invalid order", fields };',
                                               replacement), encoding="utf-8")
                result = assess(self.workspace)
                self.assertIsNone(result["backend"])
                self.assertIn("AssertionError", result["form"] or "")
        form.write_text(valid, encoding="utf-8")
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_form_oracle_checks_the_accepted_minimum_quantity(self):
        self._write_valid_implementation()
        form = self.workspace / "ui/order-form.mjs"
        valid = form.read_text(encoding="utf-8")
        form.write_text(valid.replace('quantity < 1', 'quantity < 2'), encoding="utf-8")
        result = assess(self.workspace)
        self.assertIsNone(result["backend"])
        self.assertIn("AssertionError", result["form"] or "")
        form.write_text(valid, encoding="utf-8")
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_form_oracle_preserves_original_fields_on_each_failure_path(self):
        self._write_valid_implementation()
        form = self.workspace / "ui/order-form.mjs"
        valid = form.read_text(encoding="utf-8")
        for error in ('"invalid order"', 'response.body.error'):
            with self.subTest(failure=error):
                statement = f'return {{ ok: false, error: {error}, fields }};'
                form.write_text(valid.replace(statement, 'fields.quantity = "";\n    ' + statement),
                                encoding="utf-8")
                result = assess(self.workspace)
                self.assertIsNone(result["backend"])
                self.assertIn("AssertionError", result["form"] or "")
        form.write_text(valid, encoding="utf-8")
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_backend_oracle_rejects_silent_coercion_of_contract_input_types(self):
        self._write_valid_implementation()
        orders = self.workspace / "backend/orders.py"
        valid = orders.read_text(encoding="utf-8")
        for old, new in ((
                'name = payload.get("item_name")', 'name = str(payload.get("item_name"))'), (
                'quantity = payload.get("quantity")',
                'quantity = payload.get("quantity")\n    if isinstance(quantity, str):\n        quantity = int(quantity)'), (
                'not isinstance(quantity, int)',
                'not isinstance(quantity, (int, float)) or quantity % 1 != 0'), (
                'name = payload.get("item_name")',
                'name = payload.get("item_name", "")\n    if name is None:\n        name = "Pen"'), (
                'quantity = payload.get("quantity")',
                'quantity = payload.get("quantity", 0)\n    if quantity is None:\n        quantity = 1')):
            with self.subTest(coercion=new):
                orders.write_text(valid.replace(old, new), encoding="utf-8")
                result = assess(self.workspace)
                self.assertIn("Accepted invalid payload", result["backend"] or "")
                self.assertIsNone(result["form"])
        orders.write_text(valid, encoding="utf-8")
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_backend_oracle_checks_stored_order_values_and_failed_write_atomicity(self):
        self._write_valid_implementation()
        orders = self.workspace / "backend/orders.py"
        valid = orders.read_text(encoding="utf-8")
        for old, new in ((
                'store.append(order)', 'store.append({**order, "quantity": 0})'), (
                'raise ValueError("invalid name")',
                'store[0]["quantity"] = 0\n        raise ValueError("invalid name")')):
            with self.subTest(write=new):
                orders.write_text(valid.replace(old, new), encoding="utf-8")
                result = assess(self.workspace)
                self.assertIn("AssertionError", result["backend"] or "")
                self.assertIsNone(result["form"])
        orders.write_text(valid, encoding="utf-8")
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_backend_oracle_rejects_defaults_for_missing_required_fields(self):
        self._write_valid_implementation()
        orders = self.workspace / "backend/orders.py"
        valid = orders.read_text(encoding="utf-8")
        for field, default in (("item_name", '"Pen"'), ("quantity", "1")):
            with self.subTest(field=field):
                orders.write_text(valid.replace(f'payload.get("{field}")',
                                                 f'payload.get("{field}", {default})'), encoding="utf-8")
                result = assess(self.workspace)
                self.assertIn("Accepted invalid payload", result["backend"] or "")
                self.assertIsNone(result["form"])
        orders.write_text(valid, encoding="utf-8")
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})

    def test_optimization_environment_cannot_disable_independent_assertions(self):
        self._write_valid_implementation()
        orders = self.workspace / "backend/orders.py"
        valid = orders.read_text(encoding="utf-8")
        for level in ("1", "2"):
            with self.subTest(level=level), patch.dict(os.environ, PYTHONOPTIMIZE=level):
                orders.write_text(valid, encoding="utf-8")
                self.assertEqual(assess(self.workspace), {"backend": None, "form": None})
                orders.write_text(valid.replace('"item_name": name.strip()', '"item_name": name'),
                                  encoding="utf-8")
                result = assess(self.workspace)
                self.assertIn("AssertionError", result["backend"] or "")
                self.assertIsNone(result["form"])

    def test_recording_requires_public_tests_to_execute(self):
        self._write_valid_implementation()
        trial = self.workspace.parent
        (trial / "evidence").mkdir()
        (trial / "evidence/events.jsonl").write_text(
            json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
        output = trial / "recorded"
        output.mkdir()
        subprocess.run(["git", "init", "--quiet"], cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "-c", "user.name=Eval Test", "-c", "user.email=eval@example.invalid",
                        "commit", "--quiet", "-m", "Baseline"], cwd=self.workspace,
                       check=True, capture_output=True)
        normal = record(trial, output, "full-A")
        self.assertTrue(normal["public_backend_pass"])
        self.assertTrue(normal["public_form_pass"])
        backend_tests = self.workspace / "backend/tests/test_orders.py"
        form_tests = self.workspace / "ui/order-form.test.mjs"
        backend_tests.write_text(backend_tests.read_text(encoding="utf-8").replace(
            "class OrderTests", '@unittest.skip("control: not executed")\nclass OrderTests'), encoding="utf-8")
        form_tests.write_text(form_tests.read_text(encoding="utf-8").replace("test(", "test.skip("), encoding="utf-8")
        for state in ("skipped", "empty"):
            if state == "empty":
                backend_tests.write_text("", encoding="utf-8")
                form_tests.write_text("", encoding="utf-8")
            result = record(trial, output, "full-A")
            for arm in ("backend", "form"):
                with self.subTest(state=state, arm=arm):
                    self.assertFalse(result[f"public_{arm}_pass"])

    def test_recorded_patch_replays_implementation_in_new_files(self):
        for command in (["git", "init", "--quiet"], ["git", "config", "core.autocrlf", "false"],
                        ["git", "add", "."],
                        ["git", "-c", "user.name=Eval Test", "-c", "user.email=eval@example.invalid",
                         "commit", "--quiet", "-m", "Baseline"]):
            subprocess.run(command, cwd=self.workspace, check=True, capture_output=True)
        self._write_valid_implementation()
        helper = self.workspace / "backend/validation.py"
        helper.write_bytes((self.workspace / "backend/orders.py").read_bytes())
        (self.workspace / "backend/orders.py").write_text("from .validation import create_order\n", encoding="utf-8")
        additions = {"backend/validation.py": helper.read_bytes(),
                     "审阅 结论.md": b"Mixed lines\r\nwithout final newline",
                     "__pycache__ policy.md": b"Cache directories are excluded.\n",
                     "__pycache__": b"An ordinary file can share a cache directory name.\n",
                     "empty.py": b"", "payload.bin": bytes(range(256))}
        for name, content in additions.items():
            (self.workspace / name).write_bytes(content)
        cache = self.workspace / "backend/__pycache__"
        cache.mkdir()
        (cache / "local.md").write_bytes(b"Disposable cache output.\n")
        (self.workspace / "local.pyc").write_bytes(b"Disposable bytecode.\n")
        trial = self.workspace.parent
        (trial / "evidence").mkdir()
        (trial / "evidence/events.jsonl").write_text(
            json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
        output = trial / "recorded"
        output.mkdir()
        result = record(trial, output, "full-A")
        self.assertTrue(result["oracle_backend_pass"])
        self.assertTrue(result["oracle_form_pass"])
        self.assertCountEqual(result["untracked_non_cache"], additions)
        replay = trial / "replay"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", "--config", "core.autocrlf=false",
                        str(self.workspace), str(replay)],
                       check=True, capture_output=True)
        subprocess.run(["git", "apply", str(output / "full-A.patch")], cwd=replay,
                       check=True, capture_output=True)
        self.assertEqual(assess(replay), {"backend": None, "form": None})
        for name, content in additions.items():
            with self.subTest(name=name):
                self.assertEqual((replay / name).read_bytes(), content)
                self.assertEqual((self.workspace / name).read_bytes(), content)
        self.assertEqual(subprocess.check_output(["git", "diff", "--cached", "--name-only"],
                                                cwd=self.workspace), b"")

    def test_recording_keeps_staged_and_unstaged_changes_against_baseline(self):
        tracked_name = "后端 说明.md"
        untracked_name = "审阅 结论.md"
        (self.workspace / tracked_name).write_text("Baseline note.\n", encoding="utf-8", newline="\n")
        subprocess.run(["git", "init", "--quiet"], cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "config", "core.autocrlf", "false"],
                       cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "config", "core.quotepath", "true"],
                       cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "-c", "user.name=Eval Test", "-c", "user.email=eval@example.invalid",
                        "commit", "--quiet", "-m", "Baseline"], cwd=self.workspace,
                       check=True, capture_output=True)
        self._write_valid_implementation()
        (self.workspace / tracked_name).write_text("Changed note.\n", encoding="utf-8", newline="\n")
        for path in (self.workspace / "backend/orders.py", self.workspace / "ui/order-form.mjs"):
            path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
        trial = self.workspace.parent
        (trial / "evidence").mkdir()
        (trial / "evidence/events.jsonl").write_text(
            json.dumps({"type": "item.completed", "item": {"type": "agent_message",
                       "text": "A stable table. " + str(self.workspace)}}) + "\n"
            + json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
        output = trial / "recorded"
        output.mkdir()
        previous = Path.cwd()
        try:
            os.chdir(trial.parent)
            before = record(Path(trial.name), output, "full-A")
        finally:
            os.chdir(previous)
        self.assertEqual((output / "full-A-final.txt").read_text(encoding="utf-8"),
                         "A stable table. " + str(self.workspace).replace(str(trial.parent), "<trial-root>") + "\n")
        patch = (output / "full-A.patch").read_text(encoding="utf-8")
        subprocess.run(["git", "add", "backend/orders.py", "ui/order-form.mjs", tracked_name],
                       cwd=self.workspace, check=True, capture_output=True)
        staged = record(trial, output, "full-A")
        self.assertCountEqual(staged["changed_files"], ["backend/orders.py", "ui/order-form.mjs", tracked_name])
        self.assertEqual(staged["changed_files"], before["changed_files"])
        self.assertEqual((output / "full-A.patch").read_text(encoding="utf-8"), patch)
        with (self.workspace / "backend/orders.py").open("a", encoding="utf-8") as source:
            source.write("# Unstaged follow-up\n")
        (self.workspace / untracked_name).write_text("Untracked note.\n", encoding="utf-8")
        mixed = record(trial, output, "full-A")
        mixed_patch = (output / "full-A.patch").read_text(encoding="utf-8")
        self.assertCountEqual(mixed["changed_files"], staged["changed_files"])
        self.assertEqual(mixed["untracked_non_cache"], [untracked_name])
        self.assertIn('+    order = {"id": len(store) + 1', mixed_patch)
        self.assertIn("+  const response = await postJson", mixed_patch)
        self.assertIn("+# Unstaged follow-up", mixed_patch)
        self.assertIn("+Changed note.", mixed_patch)
        native_diff = subprocess.check_output(
            ["git", "diff", "HEAD", "--", *mixed["changed_files"]], cwd=self.workspace)
        added_diff = subprocess.run(["git", "diff", "--no-index", "--", "/dev/null", untracked_name],
                                    cwd=self.workspace, capture_output=True)
        self.assertEqual(added_diff.returncode, 1)
        self.assertEqual((output / "full-A.patch").read_bytes(), native_diff + added_diff.stdout)
        reverse_check = subprocess.run(
            ["git", "apply", "--reverse", "--check", str(output / "full-A.patch")],
            cwd=self.workspace, capture_output=True, text=True)
        self.assertEqual(reverse_check.returncode, 0, reverse_check.stderr)

    def test_recording_cli_normalizes_relative_roots_and_keeps_prompt_mismatch_gate(self):
        parent = self.workspace.parent
        runner = parent / "runner"
        runner.mkdir()
        for folder in ("ab", "c"):
            subprocess.run([sys.executable, str(ROOT / "evals/prepare_routing_trial.py"),
                            "--output", str(parent / folder)], check=True,
                           capture_output=True, text=True, timeout=40)
        for task in ("full", "backend"):
            for variant in ("A", "B", "C"):
                trial = parent / ("c" if variant == "C" else "ab") / f"{task}-{variant}"
                (trial / "evidence/events.jsonl").write_text(
                    json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
        inputs = []
        for name, ab, c in (("absolute", str(parent / "ab"), str(parent / "c")),
                            ("relative", "../ab", "../c")):
            output = parent / name
            result = subprocess.run([sys.executable, str(ROOT / "evals/record_routing_trial.py"),
                                     "--ab-root", ab, "--c-root", c, "--output", str(output)],
                                    cwd=runner, capture_output=True, text=True, timeout=40)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            inputs.append(json.loads((output / "inputs.json").read_text(encoding="utf-8")))
            for prompt in inputs[-1]["normalized_prompts"].values():
                self.assertNotIn(str(parent), prompt)
                self.assertIn("<workspace>", prompt)
            outcomes = json.loads((output / "outcomes.json").read_text(encoding="utf-8"))
            self.assertTrue(all(not trial["public_backend_pass"] for trial in outcomes.values()))
        self.assertEqual(inputs[0], inputs[1])
        output = parent / "relative"
        before = {p.name: p.read_bytes() for p in output.iterdir()}
        for task in ("full", "backend"):
            for variant in ("A", "B", "C"):
                for relative in ("AGENTS.md", ".agents/skills/engineering-loop/SKILL.md",
                                 ".agents/skills/order-backend/SKILL.md", ".agents/skills/order-form/SKILL.md"):
                    with self.subTest(changed_instruction=f"{task}-{variant}/{relative}"):
                        trial = parent / ("c" if variant == "C" else "ab") / f"{task}-{variant}"
                        instruction = trial / "workspace" / relative
                        original = instruction.read_bytes()
                        try:
                            instruction.write_bytes(original + b"\nChanged frozen instruction.\n")
                            drift = subprocess.run([sys.executable, str(ROOT / "evals/record_routing_trial.py"),
                                                    "--ab-root", "../ab", "--c-root", "../c",
                                                    "--output", str(output)], cwd=runner,
                                                   capture_output=True, text=True, timeout=40)
                            self.assertEqual(drift.returncode, 1, drift.stdout + drift.stderr)
                            diagnostic = ("Trial project instructions changed after preparation"
                                          if relative == "AGENTS.md" else "Trial skill changed after preparation")
                            self.assertIn(diagnostic, drift.stderr)
                            self.assertEqual({p.name: p.read_bytes() for p in output.iterdir()}, before)
                        finally:
                            instruction.write_bytes(original)
                            for name, content in before.items():
                                (output / name).write_bytes(content)
        for task in ("full", "backend"):
            for variant in ("A", "B", "C"):
                with self.subTest(changed_baseline=f"{task}-{variant}"):
                    workspace = parent / ("c" if variant == "C" else "ab") / f"{task}-{variant}/workspace"
                    baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=workspace).strip()
                    source = workspace / "backend/orders.py"
                    original = source.read_bytes()
                    try:
                        source.write_bytes(original + b"\n# Committed candidate change.\n")
                        subprocess.run(["git", "add", "backend/orders.py"], cwd=workspace, check=True,
                                       capture_output=True)
                        subprocess.run(["git", "-c", "user.name=Eval Test", "-c", "user.email=eval@example.invalid",
                                        "commit", "--quiet", "-m", "Unexpected candidate commit"], cwd=workspace,
                                       check=True, capture_output=True)
                        drift = subprocess.run([sys.executable, str(ROOT / "evals/record_routing_trial.py"),
                                                "--ab-root", "../ab", "--c-root", "../c", "--output", str(output)],
                                               cwd=runner, capture_output=True, text=True, timeout=40)
                        self.assertEqual(drift.returncode, 1, drift.stdout + drift.stderr)
                        self.assertIn("Trial baseline changed after preparation", drift.stderr)
                        self.assertEqual({p.name: p.read_bytes() for p in output.iterdir()}, before)
                    finally:
                        subprocess.run(["git", "update-ref", "HEAD", baseline.decode()], cwd=workspace,
                                       check=True, capture_output=True)
                        subprocess.run(["git", "read-tree", baseline.decode()], cwd=workspace,
                                       check=True, capture_output=True)
                        source.write_bytes(original)
                        for name, content in before.items():
                            (output / name).write_bytes(content)
        prompt = parent / "c/full-C/prompt.txt"
        prompt.write_text(prompt.read_text(encoding="utf-8") + "\nDifferent approved task.\n", encoding="utf-8")
        rejected = subprocess.run([sys.executable, str(ROOT / "evals/record_routing_trial.py"),
                                   "--ab-root", "../ab", "--c-root", "../c",
                                   "--output", str(parent / "mismatch")], cwd=runner,
                                  capture_output=True, text=True, timeout=40)
        self.assertEqual(rejected.returncode, 1, rejected.stdout + rejected.stderr)
        self.assertIn("Prompt mismatch: full", rejected.stderr)
        self.assertFalse((parent / "mismatch/outcomes.json").exists())
        for variant in ("A", "B"):
            prompt = parent / "ab" / f"full-{variant}/prompt.txt"
            prompt.write_text(prompt.read_text(encoding="utf-8") + "\nDifferent approved task.\n",
                              encoding="utf-8")
        output = parent / "relative"
        before = {p.name: p.read_bytes() for p in output.iterdir()}
        changed_together = subprocess.run([sys.executable, str(ROOT / "evals/record_routing_trial.py"),
                                          "--ab-root", "../ab", "--c-root", "../c",
                                          "--output", str(output)], cwd=runner,
                                         capture_output=True, text=True, timeout=40)
        self.assertEqual(changed_together.returncode, 1,
                         changed_together.stdout + changed_together.stderr)
        self.assertIn("Trial prompt changed after preparation", changed_together.stderr)
        self.assertEqual({p.name: p.read_bytes() for p in output.iterdir()}, before)


if __name__ == "__main__":
    unittest.main()
