"""Real local backup controls, not a model recovery evaluation."""
from contextlib import closing
import hashlib
from pathlib import Path
import shutil
import sqlite3
import tempfile
import unittest

import test_operations_readiness as readiness


class BackupRestoreTests(unittest.TestCase):
    start = readiness.OperationsReadinessTests.start
    stop = staticmethod(readiness.OperationsReadinessTests.stop)
    request = staticmethod(readiness.OperationsReadinessTests.request)
    complete = readiness.OperationsReadinessTests.complete

    def test_restore_separate_snapshot_preserves_boundary_and_accepts_new_work(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original, backup, restored = [root / name for name in ('original.db', 'backup.db', 'restored.db')]
            process, base = self.start(original, manual=False)
            self.request(base, '/jobs', 'before-backup')
            before = self.complete(base, ['before-backup'])
            source = sqlite3.connect(original)
            destination = sqlite3.connect(backup)
            try:
                source.backup(destination)
            finally:
                destination.close()
                source.close()
            frozen = hashlib.sha256(backup.read_bytes()).hexdigest()
            self.request(base, '/jobs', 'after-backup')
            after = self.complete(base, ['before-backup', 'after-backup'])
            self.stop(process)
            # Restarting the original is deliberately not accepted as restoring the snapshot.
            process, base = self.start(original, manual=True)
            self.assertEqual(self.request(base, '/jobs')[1], after)
            self.assertNotEqual(self.request(base, '/jobs')[1], before)
            self.stop(process)
            shutil.copyfile(backup, restored)
            self.assertFalse(original.samefile(restored))
            self.assertFalse(backup.samefile(restored))
            process, base = self.start(restored, manual=False)
            self.assertEqual(self.request(base, '/jobs')[1], before)
            self.request(base, '/jobs', 'before-backup')
            self.assertEqual(self.request(base, '/jobs')[1], before)
            self.request(base, '/jobs', 'new-after-restore')
            recovered = self.complete(base, ['before-backup', 'new-after-restore'])
            self.stop(process)
            process, base = self.start(restored, manual=True)
            self.assertEqual(self.request(base, '/jobs')[1], recovered)
            self.stop(process)
            self.assertEqual(hashlib.sha256(backup.read_bytes()).hexdigest(), frozen)
            with closing(sqlite3.connect(original)) as db:
                self.assertEqual(db.execute('SELECT request_id FROM outputs ORDER BY request_id').fetchall(),
                                 [('after-backup',), ('before-backup',)])


if __name__ == '__main__':
    unittest.main()
