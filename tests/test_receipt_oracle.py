import importlib.util
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
spec = importlib.util.spec_from_file_location("receipt_oracle", ROOT / "evals/receipt_oracle.py")
oracle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oracle)


class OracleResourceTests(unittest.TestCase):
    def test_oracle_rejects_receipt_contract_mutants(self):
        baseline = (ROOT / "evals/fixtures/receipt/inventory.py").read_text(encoding="utf-8")
        start = baseline.index("    def receive(")
        end = baseline.index("    def close(", start)
        receive = '''    def receive(self, order_id, quantity, request_id):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("invalid quantity")
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            receipt = self.db.execute(
                "SELECT order_id, quantity, result FROM receipts WHERE request_id = ?",
                (request_id,)).fetchone()
            if receipt is not None:
                if receipt[:2] != (order_id, quantity):
                    raise ValueError("conflicting receipt")
                return receipt[2]
            order = self.db.execute(
                "SELECT ordered, received FROM orders WHERE order_id = ?",
                (order_id,)).fetchone()
            if order is None:
                raise KeyError(order_id)
            ordered, received = order
            result = received + quantity
            if result > ordered:
                raise ValueError("excessive receipt")
            self.db.execute("UPDATE orders SET received = ? WHERE order_id = ?",
                            (result, order_id))
            self.db.execute("INSERT INTO receipts VALUES (?, ?, ?, ?)",
                            (request_id, order_id, quantity, result))
            return result

'''
        broken = receive.replace(
            '            self.db.execute("UPDATE orders',
            '            if result == ordered:\n                return result\n'
            '            self.db.execute("UPDATE orders')
        missing_receipt = receive.replace(
            '            self.db.execute("INSERT INTO receipts',
            '            if result == ordered:\n                return result\n'
            '            self.db.execute("INSERT INTO receipts')
        insertion = ('            self.db.execute("INSERT INTO receipts VALUES (?, ?, ?, ?)",\n'
                     '                            (request_id, order_id, quantity, result))\n')
        tracked_failure = receive.replace(insertion,
            '            try:\n' + ''.join('    ' + line for line in insertion.splitlines(keepends=True)) +
            '            except sqlite3.DatabaseError:\n'
            '                self.storage_failed = True\n                raise\n')
        recovery_mutants = []
        for name, anchor in (("recovery missing writes", '            self.db.execute("UPDATE orders'),
                             ("recovery missing receipt", '            try:\n')):
            recovery_mutants.append((name, tracked_failure.replace(anchor,
                '            if getattr(self, "storage_failed", False):\n                return result\n' + anchor), 1))
        failure_other_order_mutants = []
        for exception, message in (("ValueError", "excessive receipt"),
                                   ("sqlite3.DatabaseError", "exercise storage failure")):
            wrapper = (receive.replace('    def receive(', '    def _receive(') +
                '    def receive(self, order_id, quantity, request_id):\n'
                '        try:\n            return self._receive(order_id, quantity, request_id)\n'
                f'        except {exception} as error:\n'
                f'            if str(error) == {message!r}:\n'
                '                with self.db:\n'
                '                    self.db.execute("UPDATE orders SET received = 1 WHERE order_id = \'B\'")\n'
                '            raise\n\n')
            failure_other_order_mutants.append((f"other order after {exception}", wrapper, 1))
        competing_mutants = []
        for field in ("quantity", "result"):
            wrapper = (receive.replace('    def receive(', '    def _receive(') +
                '    def receive(self, order_id, quantity, request_id):\n'
                '        try:\n            return self._receive(order_id, quantity, request_id)\n'
                '        finally:\n'
                '            if request_id == "R2" and quantity == 60:\n'
                '                with self.db:\n'
                f'                    self.db.execute("UPDATE receipts SET {field} = {field} + 1")\n\n')
            competing_mutants.append((f"competing wrong {field}", wrapper, 1))
        deferred_write_mutants = []
        for corrupt in ("UPDATE orders SET received = 0 WHERE order_id = 'A'",
                        "UPDATE receipts SET quantity = 21 WHERE request_id = 'R2'",
                        "UPDATE receipts SET result = 81 WHERE request_id = 'R2'"):
            wrapper = (receive.replace('    def receive(', '    def _receive(') +
                '    def receive(self, order_id, quantity, request_id):\n'
                '        result = self._receive(order_id, quantity, request_id)\n'
                '        if (request_id, quantity) == ("R2", 20):\n'
                f'            with self.db:\n                self.db.execute({corrupt!r})\n'
                '        elif (request_id, quantity) == ("R1", 60) and self.db.execute(\n'
                '                "SELECT quantity FROM receipts WHERE request_id = \'R2\'").fetchone() in [(20,), (21,)]:\n'
                '            with self.db:\n'
                '                self.db.execute("UPDATE orders SET received = 80 WHERE order_id = \'A\'")\n'
                '                self.db.execute("UPDATE receipts SET quantity = 20, result = 80 WHERE request_id = \'R2\'")\n'
                '        return result\n\n')
            deferred_write_mutants.append((f"write restored by replay: {corrupt}", wrapper, 1))
        validation = '        if type(quantity) is not int or quantity <= 0:\n            raise ValueError("invalid quantity")\n'
        late_validation = receive.replace(validation, '').replace(
            '            order = self.db.execute(',
            '            if type(quantity) is not int or quantity <= 0:\n'
            '                raise ValueError("invalid quantity")\n'
            '            order = self.db.execute(')
        nullable_validation = receive.replace(
            'if type(quantity) is not int or quantity <= 0:',
            'if quantity is not None and (type(quantity) is not int or quantity <= 0):')
        single_receipt_cap = receive.replace('quantity <= 0:', 'quantity <= 0 or quantity > 60:')
        fixed_order_capacity = receive.replace('if result > ordered:', 'if result > 100:')
        earliest_order_result = receive.replace('                return receipt[2]',
            '                return self.db.execute(\n'
            '                    "SELECT MIN(result) FROM receipts WHERE order_id = ?",\n'
            '                    (order_id,)).fetchone()[0]')
        initial_integral_float = receive.replace(
            'if type(quantity) is not int or quantity <= 0:',
            'if type(quantity) not in (int, float) or quantity <= 0 or int(quantity) != quantity:').replace(
            '            if receipt is not None:\n',
            '            if receipt is not None:\n'
            '                if type(quantity) is not int:\n'
            '                    raise ValueError("invalid replay quantity")\n')
        receipt_total = 'COALESCE((SELECT MAX(result) FROM receipts WHERE order_id = orders.order_id), 0)'
        hidden_stock = receive.replace('SELECT ordered, received FROM orders',
                                       f'SELECT ordered, {receipt_total} FROM orders').replace(
            insertion, '            self.db.execute("UPDATE orders SET received = 0 WHERE order_id = ?",\n'
            '                            (order_id,))\n' + insertion)
        receipt_based_getter = ('    def received(self, order_id):\n'
                        f'        row = self.db.execute("SELECT {receipt_total} FROM orders WHERE order_id = ?",\n'
                        '                              (order_id,)).fetchone()\n'
                        '        if row is None:\n            raise KeyError(order_id)\n'
                        '        return row[0]\n\n')
        hidden_stock += receipt_based_getter
        restored_rejections = []
        for name, before, after, corrupt, restore in (
                ("invalid order", 'quantity is None', 'type(quantity) is int and quantity == 0',
                 "UPDATE orders SET received = 1 WHERE order_id = 'A'",
                 "UPDATE orders SET received = 0 WHERE order_id = 'A'"),
                ("invalid receipt", 'quantity is None', 'type(quantity) is int and quantity == 0',
                 "INSERT INTO receipts VALUES ('invalid', 'A', 1, 1)",
                 "DELETE FROM receipts WHERE request_id = 'invalid'"),
                ("invalid other order", 'quantity is None', 'type(quantity) is int and quantity == 0',
                 "UPDATE orders SET received = 1 WHERE order_id = 'B'",
                 "UPDATE orders SET received = 0 WHERE order_id = 'B'"),
                ("conflict", '(order_id, quantity) == ("A", 30)', '(order_id, quantity) == ("B", 20)',
                 "UPDATE orders SET received = 21 WHERE order_id = 'A'",
                 "UPDATE orders SET received = 20 WHERE order_id = 'A'"),
                ("invalid replay", 'request_id == "single" and type(quantity) is bool',
                 'request_id == "single" and type(quantity) is float and quantity == 1.0',
                 "UPDATE orders SET received = 2 WHERE order_id = 'A'",
                 "UPDATE orders SET received = 1 WHERE order_id = 'A'"),
                ("invalid replay other order", 'request_id == "single" and type(quantity) is bool',
                 'request_id == "single" and type(quantity) is float and quantity == 1.0',
                 "UPDATE orders SET received = 1 WHERE order_id = 'B'",
                 "UPDATE orders SET received = 0 WHERE order_id = 'B'")):
            mutation = (f'        if {before}:\n            with self.db:\n'
                        f'                self.db.execute({corrupt!r})\n'
                        f'        elif {after}:\n            with self.db:\n'
                        f'                self.db.execute({restore!r})\n')
            restored_rejections.append((f"restored {name} write", receive.replace(validation, mutation + validation), 1))
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory)
            for name, implementation, expected_exit in (
                    ("valid", receive, 0), ("missing writes", broken, 1), ("missing receipt", missing_receipt, 1),
                    ("validation after replay", late_validation, 1),
                    ("nullable quantity", nullable_validation, 1),
                    ("unapproved per-receipt cap", single_receipt_cap, 1),
                    ("fixed order capacity", fixed_order_capacity, 1),
                    ("replay returns earliest order result", earliest_order_result, 1),
                    ("initial integral float", initial_integral_float, 1), *restored_rejections, *recovery_mutants,
                    ("receipt-based getter with persisted stock", receive + receipt_based_getter, 0),
                    ("unpersisted stock hidden by receipt totals", hidden_stock, 1),
                    *competing_mutants, *failure_other_order_mutants, *deferred_write_mutants):
                with self.subTest(candidate=name):
                    source = baseline[:start] + implementation + baseline[end:]
                    inventory = candidate / "inventory.py"
                    inventory.write_text(source, encoding="utf-8")
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "evals/receipt_oracle.py"), str(candidate)],
                        capture_output=True, text=True, timeout=30)
                    self.assertIn("Ran 7 tests", result.stderr)
                    self.assertEqual(result.returncode, expected_exit, result.stderr)
                    self.assertEqual(inventory.read_text(encoding="utf-8"), source)

    def test_receipt_inspection_releases_database_connection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stock.db"
            connection = sqlite3.connect(path)
            try:
                connection.execute("CREATE TABLE receipts (request_id, order_id, quantity, result)")
                case = oracle.ReceiptContractTests()
                case.path = path
                with patch.object(oracle.sqlite3, "connect", return_value=connection):
                    self.assertEqual(case.receipt_rows(), [])
                # Transaction completion alone does not release the connection/file.
                with self.assertRaises(sqlite3.ProgrammingError):
                    connection.execute("SELECT 1")
            finally:
                connection.close()


if __name__ == "__main__":
    unittest.main()
