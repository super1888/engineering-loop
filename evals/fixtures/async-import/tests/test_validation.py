from pathlib import Path
import tempfile
import unittest

from backend.service import ImportService


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.service = ImportService(Path(self.directory.name) / 'test.db')

    def test_invalid_input_is_rejected_without_records(self):
        for rows in ([], [{'rowId': 'a', 'name': ''}], [{'rowId': 1, 'name': 'A'}], [{}]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                self.service.submit('request', rows)
        self.assertEqual(self.service.records(), [])

    def test_duplicate_rows_and_missing_request_identity_are_rejected(self):
        with self.assertRaises(ValueError):
            self.service.submit('request', [{'rowId': 'a', 'name': 'A'}, {'rowId': 'a', 'name': 'B'}])
        with self.assertRaises(ValueError):
            self.service.submit('', [{'rowId': 'a', 'name': 'A'}])
