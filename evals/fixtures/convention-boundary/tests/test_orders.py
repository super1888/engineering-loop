import unittest

from orders import accepts_export_total, accepts_order_total, format_reference


class OrderTests(unittest.TestCase):
    def test_current_limit(self):
        for accepts in (accepts_order_total, accepts_export_total):
            self.assertTrue(accepts(10_000))
            self.assertFalse(accepts(0))

    def test_reference_preserves_case(self):
        self.assertEqual(format_reference("ab12"), "ab12")
        with self.assertRaises(ValueError):
            format_reference("abc")


if __name__ == "__main__":
    unittest.main()
