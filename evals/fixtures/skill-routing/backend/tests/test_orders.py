import unittest

from backend.orders import create_order


class OrderTests(unittest.TestCase):
    def test_creates_order_with_server_id(self):
        store = []
        self.assertEqual(create_order(store, {"item_name": " Pen ", "quantity": 2}),
                         {"id": 1, "item_name": "Pen", "quantity": 2})
        self.assertEqual(len(store), 1)

    def test_rejects_invalid_quantity_without_storage(self):
        store = []
        with self.assertRaises(ValueError):
            create_order(store, {"item_name": "Pen", "quantity": 0})
        self.assertEqual(store, [])


if __name__ == "__main__":
    unittest.main()
