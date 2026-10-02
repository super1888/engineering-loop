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
        validation = '        if type(quantity) is not int or quantity <= 0:\n            raise ValueError("invalid quantity")\n'
        late_validation = receive.replace(validation, '').replace(
            '            order = self.db.execute(',
            '            if type(quantity) is not int or quantity <= 0:\n'
            '                raise ValueError("invalid quantity")\n'
            '            order = self.db.execute(')
        nullable_validation = receive.replace(
            'if type(quantity) is not int or quantity <= 0:',
            'if quantity is not None and (type(quantity) is not int or quantity <= 0):')
        initial_integral_float = receive.replace(
            'if type(quantity) is not int or quantity <= 0:',
            'if type(quantity) not in (int, float) or quantity <= 0 or int(quantity) != quantity:').replace(
            '            if receipt is not None:\n',
            '            if receipt is not None:\n'
            '                if type(quantity) is not int:\n'
            '                    raise ValueError("invalid replay quantity")\n')
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory)
            for name, implementation, expected_exit in (
                    ("valid", receive, 0), ("missing writes", broken, 1), ("missing receipt", missing_receipt, 1),
                    ("validation after replay", late_validation, 1),
                    ("nullable quantity", nullable_validation, 1),
                    ("initial integral float", initial_integral_float, 1)):
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
