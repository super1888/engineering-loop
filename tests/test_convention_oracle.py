from pathlib import Path
import os
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

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
        orders = self.workspace / "orders.py"
        original = orders.read_text(encoding="utf-8")
        for statement, reference in (
                ("from order_constants import MAX_ORDER_TOTAL_CENTS", "MAX_ORDER_TOTAL_CENTS"),
                ("from order_constants import MAX_ORDER_TOTAL_CENTS as MAX_ACCEPTED_ORDER_TOTAL_CENTS",
                 "MAX_ACCEPTED_ORDER_TOTAL_CENTS"),
                ("import order_constants", "order_constants.MAX_ORDER_TOTAL_CENTS"),
                ("import order_constants as order_limits", "order_limits.MAX_ORDER_TOTAL_CENTS")):
            updated = original.replace("from order_constants import MAX_ORDER_TOTAL_CENTS", statement)
            with self.subTest(statement=statement, used=True):
                orders.write_text(updated.replace("<= MAX_ORDER_TOTAL_CENTS", "<= " + reference), encoding="utf-8")
                self.assertEqual(assess(self.workspace), [])
            with self.subTest(statement=statement, used=False):
                orders.write_text(updated.replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000"), encoding="utf-8")
                self.assertIn("Order behavior must use the module-owned constant.", assess(self.workspace))

    def test_native_candidate_output_retains_utf8_and_invalid_byte_diagnostics(self):
        constants = self.workspace / "order_constants.py"
        original_constants = constants.read_text(encoding="utf-8")
        orders = self.workspace / "orders.py"
        original_orders = orders.read_text(encoding="utf-8")
        diagnostic = "中文日志".encode("utf-8") + b"\xff\n"
        for mode, check in (("amount", assess), ("comment", assess_comment_control)):
            with self.subTest(mode=mode):
                constants.write_text(original_constants.replace("10_000", "15_000")
                                     if mode == "amount" else original_constants, encoding="utf-8")
                source = original_orders.replace("    # References are always uppercase.\n", "")
                orders.write_text(source + f"\nimport sys\nprint('正常中文日志')\nsys.stdout.buffer.write({diagnostic!r})\n",
                                  encoding="utf-8")
                candidate = {p.relative_to(self.workspace): p.read_bytes()
                             for p in self.workspace.rglob("*.py")}
                self.assertEqual(check(self.workspace), [])
                self.assertEqual({p.relative_to(self.workspace): p.read_bytes()
                                  for p in self.workspace.rglob("*.py")}, candidate)
                if mode == "amount":
                    orders.write_text(source + f"\nimport sys\nsys.stderr.buffer.write({diagnostic!r})\n"
                                      "raise SystemExit(7)\n", encoding="utf-8")
                    failures = check(self.workspace)
                    self.assertTrue(any("Behavior check failed: 中文日志\ufffd" in f for f in failures), failures)
                    self.assertIn("Order behavior must use the module-owned constant.", failures)
                else:
                    tests = self.workspace / "tests/test_orders.py"
                    public = tests.read_text(encoding="utf-8")
                    tests.write_text(public + f"\nimport sys\nsys.stderr.buffer.write({diagnostic!r})\n"
                                     "raise RuntimeError('中文失败')\n", encoding="utf-8")
                    failures = check(self.workspace)
                    self.assertTrue(any("Public behavior failed: " in f and "中文日志\ufffd" in f
                                        and "RuntimeError: 中文失败" in f for f in failures), failures)

    def test_optimization_environment_cannot_disable_independent_assertions(self):
        constants = self.workspace / "order_constants.py"
        original_constants = constants.read_text(encoding="utf-8")
        orders = self.workspace / "orders.py"
        valid = orders.read_text(encoding="utf-8")
        for level in ("1", "2"):
            with self.subTest(level=level), patch.dict(os.environ, PYTHONOPTIMIZE=level):
                constants.write_text(original_constants.replace("10_000", "15_000"), encoding="utf-8")
                orders.write_text(valid, encoding="utf-8")
                self.assertEqual(assess(self.workspace), [])
                orders.write_text(valid.replace("<= MAX_ORDER_TOTAL_CENTS", ">= MAX_ORDER_TOTAL_CENTS"),
                                  encoding="utf-8")
                failures = assess(self.workspace)
                self.assertTrue(any("Behavior check failed" in failure for failure in failures), failures)
                self.assertIn("Order behavior must use the module-owned constant.", failures)
                constants.write_text(original_constants, encoding="utf-8")
                comment = valid.replace("    # References are always uppercase.\n", "")
                orders.write_text(comment, encoding="utf-8")
                self.assertEqual(assess_comment_control(self.workspace), [])
                orders.write_text(comment.replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000"), encoding="utf-8")
                self.assertIn("The unrelated order amount boundary changed.",
                              assess_comment_control(self.workspace))

    def test_annotated_constant_keeps_value_and_assignment_checks(self):
        constants = self.workspace / "order_constants.py"
        original = constants.read_text(encoding="utf-8")
        for declaration, valid in (
                ("MAX_ORDER_TOTAL_CENTS: int = 15_000", True),
                ("MAX_ORDER_TOTAL_CENTS: int\nMAX_ORDER_TOTAL_CENTS = 15_000", True),
                ("MAX_ORDER_TOTAL_CENTS: int = 9_999", False),
                ("MAX_ORDER_TOTAL_CENTS: int", False)):
            with self.subTest(declaration=declaration):
                constants.write_text(original.replace("MAX_ORDER_TOTAL_CENTS = 10_000", declaration), encoding="utf-8")
                failures = assess(self.workspace)
                if valid:
                    self.assertEqual(failures, [])
                else:
                    self.assertIn("The module-owned amount constant must be 15,000 cents.", failures)

    def test_early_zero_exit_cannot_skip_behavior_checks(self):
        constants = self.workspace / "order_constants.py"
        constants.write_text(constants.read_text(encoding="utf-8").replace("10_000", "15_000"), encoding="utf-8")
        orders = self.workspace / "orders.py"
        orders.write_text(orders.read_text(encoding="utf-8") + "\nraise SystemExit(0)\n", encoding="utf-8")
        self.assertIn("Behavior checks did not reach completion", assess(self.workspace))

    def test_amount_change_preserves_unrelated_reference_validation(self):
        constants = self.workspace / "order_constants.py"
        constants.write_text(constants.read_text(encoding="utf-8").replace("10_000", "15_000"), encoding="utf-8")
        orders = self.workspace / "orders.py"
        valid = orders.read_text(encoding="utf-8")
        self.assertEqual(assess(self.workspace), [])
        orders.write_text(valid.replace('    if len(code) < 4:\n        raise ValueError("reference too short")\n', ''),
                          encoding="utf-8")
        failures = assess(self.workspace)
        self.assertTrue(any("Behavior check failed" in failure for failure in failures), failures)

    def test_unused_reference_cannot_hide_inlined_behavior_limits(self):
        constants = self.workspace / "order_constants.py"
        constants.write_text(constants.read_text(encoding="utf-8").replace("10_000", "15_000"), encoding="utf-8")
        orders = self.workspace / "orders.py"
        original = orders.read_text(encoding="utf-8")
        order_source, export_source = original.split("\ndef accepts_export_total", 1)
        for scope in ("order", "export", "both"):
            with self.subTest(scope=scope):
                order = (order_source.replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000")
                         if scope in ("order", "both") else order_source)
                export = (export_source.replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000")
                          if scope in ("export", "both") else export_source)
                updated = order + "\ndef accepts_export_total" + export
                orders.write_text(updated + "\ndef unused_limit():\n    return MAX_ORDER_TOTAL_CENTS\n", encoding="utf-8")
                for bytecode in self.workspace.glob("__pycache__/*.pyc"):
                    bytecode.unlink()
                self.assertIn("Order behavior must use the module-owned constant.", assess(self.workspace))

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
        tests = self.workspace / "tests/test_orders.py"
        tests.write_text(tests.read_text(encoding="utf-8").replace(
            "class OrderTests", '@unittest.skip("control: not executed")\nclass OrderTests'), encoding="utf-8")
        self.assertTrue(any("Public behavior failed" in failure
                            for failure in assess_comment_control(self.workspace)))

    def test_comment_control_checks_actual_unchanged_amount_boundary(self):
        for name, declaration, inlined_scope, valid in (
                ("plain", "MAX_ORDER_TOTAL_CENTS = 10_000", None, True),
                ("annotated", "MAX_ORDER_TOTAL_CENTS: int = 10000", None, True),
                ("stale-text", "# MAX_ORDER_TOTAL_CENTS = 10_000\nMAX_ORDER_TOTAL_CENTS = 15_000", None, False),
                ("order-inline", "MAX_ORDER_TOTAL_CENTS = 10_000", "order", False),
                ("export-inline", "MAX_ORDER_TOTAL_CENTS = 10_000", "export", False)):
            with self.subTest(name=name):
                workspace = self.workspace.parent / name
                shutil.copytree(self.workspace, workspace,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                constants = workspace / "order_constants.py"
                constants.write_text(constants.read_text(encoding="utf-8").replace(
                    "MAX_ORDER_TOTAL_CENTS = 10_000", declaration), encoding="utf-8")
                orders = workspace / "orders.py"
                source = orders.read_text(encoding="utf-8").replace(
                    "    # References are always uppercase.\n", "")
                if inlined_scope:
                    order, export = source.split("\ndef accepts_export_total", 1)
                    if inlined_scope == "order":
                        order = order.replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000")
                    else:
                        export = export.replace("<= MAX_ORDER_TOTAL_CENTS", "<= 15_000")
                    source = order + "\ndef accepts_export_total" + export
                orders.write_text(source, encoding="utf-8")
                failures = assess_comment_control(workspace)
                self.assertEqual(failures, [] if valid else
                                 ["The unrelated order amount boundary changed."])


if __name__ == "__main__":
    unittest.main()
