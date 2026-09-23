from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from routing_oracle import assess


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

    def test_valid_backend_and_form_pass(self):
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
        self.assertEqual(assess(self.workspace), {"backend": None, "form": None})


if __name__ == "__main__":
    unittest.main()
