"""Evaluator-only checks. Usage: python evals/receipt_oracle.py CANDIDATE_DIRECTORY.

The candidate is trusted local exercise code, not sandboxed by this helper.
Keep this file outside the implementation agent's provided workspace.
"""

from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
import importlib.util
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import unittest


class ReceiptContractTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "stock.db"
        self.inventory = Inventory(self.path)
        self.addCleanup(self.inventory.close)
        self.inventory.create_order("A", 100)
        self.inventory.create_order("B", 100)

    def receipt_rows(self):
        with closing(sqlite3.connect(self.path)) as connection:
            return connection.execute(
                "SELECT request_id, order_id, quantity, result FROM receipts ORDER BY request_id"
            ).fetchall()

    def test_retry_retains_original_result_after_other_receipt_and_reopen(self):
        self.assertEqual(self.inventory.receive("A", 60, "R1"), 60)
        self.assertEqual(self.inventory.receive("A", 20, "R2"), 80)
        other = Inventory(self.path)
        try:
            self.assertEqual(other.receive("A", 60, "R1"), 60)
            self.assertEqual(other.received("A"), 80)
        finally:
            other.close()
        self.assertEqual(self.receipt_rows(), [("R1", "A", 60, 60), ("R2", "A", 20, 80)])

    def test_conflicting_identity_leaves_both_orders_unchanged(self):
        self.inventory.receive("A", 20, "R1")
        for order, quantity in [("A", 30), ("B", 20)]:
            with self.subTest(order=order, quantity=quantity):
                with self.assertRaises(ValueError):
                    self.inventory.receive(order, quantity, "R1")
        self.assertEqual(self.inventory.received("A"), 20)
        self.assertEqual(self.inventory.received("B"), 0)
        self.assertEqual(self.receipt_rows(), [("R1", "A", 20, 20)])

    def test_over_receipt_is_atomic_and_does_not_consume_identity(self):
        self.inventory.receive("A", 60, "R1")
        with self.assertRaises(ValueError):
            self.inventory.receive("A", 50, "R2")
        self.assertEqual(self.inventory.received("A"), 60)
        self.assertEqual(self.receipt_rows(), [("R1", "A", 60, 60)])
        self.assertEqual(self.inventory.receive("A", 40, "R2"), 100)

    def test_invalid_quantity_and_unknown_order_leave_no_receipt(self):
        for quantity in [0, -1, 1.5, True, "2"]:
            with self.subTest(quantity=quantity):
                with self.assertRaises(ValueError):
                    self.inventory.receive("A", quantity, "invalid")
        with self.assertRaises(KeyError):
            self.inventory.receive("missing", 1, "missing")
        self.assertEqual(self.inventory.received("A"), 0)
        self.assertEqual(self.receipt_rows(), [])

    def compete(self, requests):
        barrier = threading.Barrier(len(requests))

        def attempt(request):
            inventory = Inventory(self.path)
            try:
                barrier.wait(timeout=10)
                try:
                    return ("accepted", inventory.receive("A", *request))
                except ValueError:
                    return ("rejected", None)
            finally:
                inventory.close()

        with ThreadPoolExecutor(max_workers=len(requests)) as executor:
            return list(executor.map(attempt, requests))

    def test_competing_duplicate_connections_write_once(self):
        self.assertEqual(self.compete([(60, "R1"), (60, "R1")]),
                         [("accepted", 60), ("accepted", 60)])
        self.assertEqual(self.inventory.received("A"), 60)
        self.assertEqual(self.receipt_rows(), [("R1", "A", 60, 60)])

    def test_competing_distinct_receipts_cannot_over_receive(self):
        results = self.compete([(60, "R1"), (60, "R2")])
        self.assertCountEqual(results, [("accepted", 60), ("rejected", None)])
        self.assertEqual(self.inventory.received("A"), 60)
        self.assertEqual(len(self.receipt_rows()), 1)

    def test_storage_failure_rolls_back_inventory_and_identity(self):
        with closing(sqlite3.connect(self.path)) as connection, connection:
            connection.execute("""CREATE TRIGGER reject_receipt BEFORE INSERT ON receipts
                BEGIN SELECT RAISE(ABORT, 'exercise storage failure'); END""")
        with self.assertRaises(sqlite3.DatabaseError):
            self.inventory.receive("A", 60, "R1")
        self.assertEqual(self.inventory.received("A"), 0)
        self.assertEqual(self.receipt_rows(), [])
        with closing(sqlite3.connect(self.path)) as connection, connection:
            connection.execute("DROP TRIGGER reject_receipt")
        self.assertEqual(self.inventory.receive("A", 60, "R1"), 60)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not (Path(sys.argv[1]) / "inventory.py").is_file():
        sys.exit("Usage: python evals/receipt_oracle.py CANDIDATE_DIRECTORY (must contain inventory.py)")
    candidate = Path(sys.argv.pop()).resolve() / "inventory.py"
    spec = importlib.util.spec_from_file_location("receipt_candidate", candidate)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    Inventory = module.Inventory
    unittest.main(verbosity=2)
