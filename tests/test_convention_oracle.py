from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from convention_oracle import assess, assess_comment_control


class ConventionOracleTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.workspace = Path(self.directory.name) / "workspace"
        shutil.copytree(ROOT / "evals/fixtures/convention-boundary", self.workspace)

    def test_baseline_fails_accepted_change(self):
        failures = assess(self.workspace)
        self.assertTrue(any("15,000" in failure for failure in failures))
        self.assertTrue(any("Behavior check failed" in failure for failure in failures))

    def test_valid_change_preserves_reason_and_owner(self):
        constants = self.workspace / "order_constants.py"
        constants.write_text(constants.read_text(encoding="utf-8").replace("10_000", "15_000"), encoding="utf-8")
        self.assertEqual(assess(self.workspace), [])

    def test_inlining_limit_and_dropping_reason_fails(self):
        constants = self.workspace / "order_constants.py"
        constants.write_text("MAX_ORDER_TOTAL_CENTS = 15_000\n", encoding="utf-8")
        orders = self.workspace / "orders.py"
        orders.write_text(orders.read_text(encoding="utf-8").replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000")
                          .replace("    # References are always uppercase.\n", ""), encoding="utf-8")
        failures = assess(self.workspace)
        self.assertTrue(any("explanation" in failure for failure in failures))
        self.assertTrue(any("module-owned constant" in failure for failure in failures))

    def test_stale_comment_control_is_separate(self):
        self.assertTrue(any("obsolete" in failure for failure in assess_comment_control(self.workspace)))
        orders = self.workspace / "orders.py"
        orders.write_text(orders.read_text(encoding="utf-8").replace("    # References are always uppercase.\n", ""), encoding="utf-8")
        self.assertEqual(assess_comment_control(self.workspace), [])


if __name__ == "__main__":
    unittest.main()
