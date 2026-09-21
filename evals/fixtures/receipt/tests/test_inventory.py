from pathlib import Path
import tempfile
import unittest

from inventory import Inventory


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.inventory = Inventory(Path(self.directory.name) / "stock.db")
        self.addCleanup(self.inventory.close)
        self.inventory.create_order("A", 100)

    def test_first_receipt(self):
        self.assertEqual(self.inventory.receive("A", 60, "R1"), 60)
        self.assertEqual(self.inventory.received("A"), 60)

    def test_retry_preserves_quantity(self):
        self.inventory.receive("A", 60, "R1")
        self.assertEqual(self.inventory.receive("A", 60, "R1"), 60)
        self.assertEqual(self.inventory.received("A"), 60)

    def test_unknown_order(self):
        with self.assertRaises(KeyError):
            self.inventory.receive("unknown", 1, "R1")


if __name__ == "__main__":
    unittest.main()
