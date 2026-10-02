from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

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

    def test_recording_keeps_staged_and_unstaged_changes_against_baseline(self):
        subprocess.run(["git", "init", "--quiet"], cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=self.workspace, check=True, capture_output=True)
        subprocess.run(["git", "-c", "user.name=Eval Test", "-c", "user.email=eval@example.invalid",
                        "commit", "--quiet", "-m", "Baseline"], cwd=self.workspace,
                       check=True, capture_output=True)
        self._write_valid_implementation()
        trial = self.workspace.parent
        (trial / "evidence").mkdir()
        (trial / "evidence/events.jsonl").write_text(
            json.dumps({"type": "turn.completed"}) + "\n", encoding="utf-8")
        output = trial / "recorded"
        output.mkdir()
        before = record(trial, output, "full-A")
        patch = (output / "full-A.patch").read_text(encoding="utf-8")
        subprocess.run(["git", "add", "backend/orders.py", "ui/order-form.mjs"],
                       cwd=self.workspace, check=True, capture_output=True)
        staged = record(trial, output, "full-A")
        self.assertCountEqual(staged["changed_files"], ["backend/orders.py", "ui/order-form.mjs"])
        self.assertEqual(staged["changed_files"], before["changed_files"])
        self.assertEqual((output / "full-A.patch").read_text(encoding="utf-8"), patch)
        with (self.workspace / "backend/orders.py").open("a", encoding="utf-8") as source:
            source.write("# Unstaged follow-up\n")
        mixed = record(trial, output, "full-A")
        mixed_patch = (output / "full-A.patch").read_text(encoding="utf-8")
        self.assertCountEqual(mixed["changed_files"], staged["changed_files"])
        self.assertIn('+    order = {"id": len(store) + 1', mixed_patch)
        self.assertIn("+  const response = await postJson", mixed_patch)
        self.assertIn("+# Unstaged follow-up", mixed_patch)


if __name__ == "__main__":
    unittest.main()
