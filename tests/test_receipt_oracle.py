import importlib.util
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("receipt_oracle", ROOT / "evals/receipt_oracle.py")
oracle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oracle)


class OracleResourceTests(unittest.TestCase):
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
