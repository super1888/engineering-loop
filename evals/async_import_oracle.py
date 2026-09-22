"""Independent revision-2 checks for a trusted synthetic candidate directory.

Usage: python evals/async_import_oracle.py PATH_TO_CANDIDATE
The checks use only the documented service and retained SQLite inspection schema.
No candidate source is rewritten. unittest diagnostics are retained on stderr.
"""

import argparse
from collections import Counter
from contextlib import closing
import importlib
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import unittest


SERVICE = None


class RevisionTwoTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="async-import-oracle-")
        self.addCleanup(directory.cleanup)
        self.db = Path(directory.name) / "state.sqlite"
        self.service = SERVICE(self.db)

    def sql(self, statement, parameters=()):
        with closing(sqlite3.connect(self.db, timeout=5)) as connection:
            connection.row_factory = sqlite3.Row
            return [dict(row) for row in connection.execute(statement, parameters)]

    def persisted_items(self, batch_id):
        return {row["row_id"]: row for row in self.sql(
            "SELECT batch_id, row_id, name, status, attempts, error, output FROM items WHERE batch_id = ?", (batch_id,))}

    def persisted_records(self, batch_id):
        return sorted(self.sql(
            "SELECT batch_id, row_id, name FROM records WHERE batch_id = ?",
            (batch_id,)), key=lambda row: row["row_id"])

    def check_snapshot(self, snapshot, batch_id, expected):
        """expected maps original row IDs to (status, attempts)."""
        self.assertIsInstance(snapshot, dict)
        self.assertEqual(snapshot.get("contractVersion"), 2, snapshot)
        self.assertEqual(snapshot.get("batchId"), batch_id, snapshot)
        self.assertIsInstance(batch_id, str)
        self.assertTrue(batch_id.strip())
        self.assertEqual(snapshot.get("total"), len(expected), snapshot)
        items = snapshot.get("items")
        self.assertIsInstance(items, list, snapshot)
        self.assertEqual(len(items), len(expected), snapshot)
        self.assertTrue(all(isinstance(item, dict) for item in items), snapshot)
        self.assertEqual({item.get("rowId") for item in items}, set(expected), snapshot)
        counts = Counter(status for status, _ in expected.values())
        self.assertEqual(snapshot.get("succeeded"), counts["SUCCEEDED"], snapshot)
        self.assertEqual(snapshot.get("failed"), counts["FAILED"], snapshot)
        if counts["QUEUED"]:
            status = "QUEUED"
        elif counts["FAILED"] and counts["SUCCEEDED"]:
            status = "PARTIAL"
        elif counts["FAILED"]:
            status = "FAILED"
        else:
            status = "SUCCEEDED"
        self.assertEqual(snapshot.get("status"), status, snapshot)
        stored = self.persisted_items(batch_id)
        self.assertEqual(set(stored), set(expected))
        self.assertEqual(self.sql("SELECT status FROM batches WHERE id = ?", (batch_id,)),
                         [{"status": status}])
        for item in items:
            identity = item["rowId"]
            self.assertIsInstance(identity, str)
            self.assertEqual(item.get("status"), expected[identity][0], item)
            self.assertIs(type(item.get("attempts")), int, item)
            self.assertEqual(item["attempts"], expected[identity][1], item)
            self.assertIn("error", item)
            if item["status"] == "SUCCEEDED":
                self.assertIsNone(item["error"], item)
            elif item["status"] == "FAILED":
                self.assertIsInstance(item["error"], str, item)
                self.assertTrue(item["error"].strip(), item)
            self.assertEqual((stored[identity]["status"], stored[identity]["attempts"],
                              stored[identity]["error"]),
                             (item["status"], item["attempts"], item["error"]))
        return {item["rowId"]: item for item in items}

    def check_records(self, batch_id, names):
        expected = [{"batch_id": batch_id, "row_id": row_id, "name": name}
                    for row_id, name in sorted(names.items())]
        self.assertEqual(self.persisted_records(batch_id), expected)
        public = sorted((row["rowId"], row["name"]) for row in self.service.records()
                        if row["batchId"] == batch_id)
        self.assertEqual(public, sorted(names.items()))
        stored = self.persisted_items(batch_id)
        for row_id, name in names.items():
            self.assertEqual(stored[row_id]["output"], name)

    def prepare_partial(self, failures=1, request_id="submission"):
        calls = Counter()
        lock = threading.Lock()

        def processor(row):
            with lock:
                calls[row["rowId"]] += 1
                attempt = calls[row["rowId"]]
            if row["rowId"] == "beta" and attempt <= failures:
                raise RuntimeError("temporary failure for beta")
            return "imported:" + row["name"]

        service = SERVICE(self.db, processor)
        rows = [{"rowId": "alpha", "name": "Ada"}, {"rowId": "beta", "name": "Ben"}]
        receipt = service.submit(request_id, rows)
        batch = receipt["batchId"]
        self.check_snapshot(receipt, batch, {"alpha": ("QUEUED", 0), "beta": ("QUEUED", 0)})
        self.check_records(batch, {})
        self.assertTrue(service.process_next())
        self.check_snapshot(service.snapshot(batch), batch,
                            {"alpha": ("SUCCEEDED", 1), "beta": ("FAILED", 1)})
        self.check_records(batch, {"alpha": "imported:Ada"})
        return service, batch, processor, calls

    def test_partial_success_preserves_opaque_row_ids_after_reopen(self):
        rows = [{"rowId": identity, "name": "name:" + identity}
                for identity in ("001", "1", "row/雪 ?#", "beta")]

        def processor(row):
            if row["rowId"] == "beta":
                raise RuntimeError("unavailable row beta")
            return "output:" + row["name"]

        service = SERVICE(self.db, processor)
        receipt = service.submit("opaque-identities", rows)
        batch = receipt["batchId"]
        self.check_snapshot(receipt, batch, {row["rowId"]: ("QUEUED", 0) for row in rows})
        self.assertTrue(service.process_next())
        expected = {row["rowId"]: ("FAILED" if row["rowId"] == "beta" else "SUCCEEDED", 1)
                    for row in rows}
        self.check_snapshot(SERVICE(self.db).snapshot(batch), batch, expected)
        self.check_records(batch, {row["rowId"]: "output:" + row["name"]
                                   for row in rows if row["rowId"] != "beta"})
        self.assertFalse(service.process_next(), "Settled failures must await explicit retry")

    def test_submission_identity_survives_processing_and_reopen(self):
        rows = [{"rowId": "a", "name": "Ada"}]
        first = self.service.submit("same-submit", rows)
        batch = first["batchId"]
        self.check_snapshot(self.service.submit("same-submit", rows), batch, {"a": ("QUEUED", 0)})
        self.assertTrue(self.service.process_next())
        reopened = SERVICE(self.db)
        self.check_snapshot(reopened.submit("same-submit", rows), batch, {"a": ("SUCCEEDED", 1)})
        with self.assertRaises(ValueError, msg="Changed payload must conflict"):
            reopened.submit("same-submit", [{"rowId": "a", "name": "Changed"}])
        self.assertEqual(len(self.sql("SELECT id FROM batches")), 1)
        self.assertFalse(reopened.process_next())
        self.check_records(batch, {"a": "Ada"})

    def test_failed_only_retry_and_lost_response_replay_after_reopen(self):
        service, batch, processor, calls = self.prepare_partial()
        before = self.persisted_items(batch)
        receipt = service.retry(batch, "lost-response")
        self.check_snapshot(receipt, batch, {"alpha": ("SUCCEEDED", 1), "beta": ("QUEUED", 1)})
        queued = self.persisted_items(batch)
        self.assertEqual(queued["alpha"], before["alpha"], "Successful item changed during retry")
        self.assertEqual(queued["beta"]["error"], before["beta"]["error"], "Retry erased error early")
        self.check_records(batch, {"alpha": "imported:Ada"})
        self.assertTrue(service.process_next())
        done = {"alpha": ("SUCCEEDED", 1), "beta": ("SUCCEEDED", 2)}
        self.check_snapshot(service.snapshot(batch), batch, done)
        settled = self.persisted_items(batch)
        reopened = SERVICE(self.db, processor)
        self.check_snapshot(reopened.retry(batch, "lost-response"), batch, done)
        self.check_snapshot(reopened.retry(batch, "new-noop"), batch, done)
        self.assertFalse(reopened.process_next())
        self.assertEqual(self.persisted_items(batch), settled)
        self.assertEqual(calls, {"alpha": 1, "beta": 2})
        self.check_records(batch, {"alpha": "imported:Ada", "beta": "imported:Ben"})

    def test_retry_that_fails_again_requires_new_identity(self):
        service, batch, processor, calls = self.prepare_partial(failures=2)
        service.retry(batch, "retry-1")
        self.assertTrue(service.process_next())
        failed_again = {"alpha": ("SUCCEEDED", 1), "beta": ("FAILED", 2)}
        self.check_snapshot(service.snapshot(batch), batch, failed_again)
        reopened = SERVICE(self.db, processor)
        self.check_snapshot(reopened.retry(batch, "retry-1"), batch, failed_again)
        self.assertFalse(reopened.process_next(), "An accepted retry identity must stay consumed after failure")
        self.check_snapshot(reopened.retry(batch, "retry-2"), batch,
                            {"alpha": ("SUCCEEDED", 1), "beta": ("QUEUED", 2)})
        self.assertTrue(reopened.process_next())
        self.check_snapshot(reopened.snapshot(batch), batch,
                            {"alpha": ("SUCCEEDED", 1), "beta": ("SUCCEEDED", 3)})
        self.assertEqual(calls, {"alpha": 1, "beta": 3})
        self.check_records(batch, {"alpha": "imported:Ada", "beta": "imported:Ben"})

    def test_all_failed_and_retry_id_is_scoped_to_batch(self):
        def failing(row):
            raise RuntimeError("processor temporarily offline")

        service = SERVICE(self.db, failing)
        batches = []
        for number in range(2):
            batch = service.submit("submit-" + str(number), [{"rowId": "same-row", "name": "A"}])["batchId"]
            batches.append(batch)
            self.assertTrue(service.process_next())
            self.check_snapshot(service.snapshot(batch), batch, {"same-row": ("FAILED", 1)})
            self.check_records(batch, {})
        working = SERVICE(self.db)
        for batch in batches:
            self.check_snapshot(working.retry(batch, "shared-retry-key"), batch, {"same-row": ("QUEUED", 1)})
        self.assertTrue(working.process_next())
        self.assertTrue(working.process_next())
        self.assertFalse(working.process_next())
        for batch in batches:
            self.check_snapshot(working.snapshot(batch), batch, {"same-row": ("SUCCEEDED", 2)})
            self.check_records(batch, {"same-row": "A"})

    def parallel(self, functions):
        barrier = threading.Barrier(len(functions))
        outcomes = [None] * len(functions)

        def run(index, function):
            try:
                barrier.wait(timeout=10)
                outcomes[index] = (True, function())
            except BaseException as error:
                outcomes[index] = (False, repr(error))

        threads = [threading.Thread(target=run, args=(index, function), daemon=True)
                   for index, function in enumerate(functions)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=15)
        self.assertFalse(any(thread.is_alive() for thread in threads), "Concurrent service calls did not settle")
        self.assertTrue(all(result and result[0] for result in outcomes), outcomes)
        return [result[1] for result in outcomes]

    def test_concurrent_retry_calls_and_workers_do_not_duplicate_attempts(self):
        _, batch, processor, calls = self.prepare_partial()
        services = [SERVICE(self.db, processor) for _ in range(6)]
        receipts = self.parallel([lambda service=service: service.retry(batch, "concurrent-key")
                                  for service in services])
        for receipt in receipts:
            self.check_snapshot(receipt, batch, {"alpha": ("SUCCEEDED", 1), "beta": ("QUEUED", 1)})
        self.parallel([service.process_next for service in services])
        expected = {"alpha": ("SUCCEEDED", 1), "beta": ("SUCCEEDED", 2)}
        self.check_snapshot(services[0].snapshot(batch), batch, expected)
        self.assertEqual(calls, {"alpha": 1, "beta": 2})
        self.check_records(batch, {"alpha": "imported:Ada", "beta": "imported:Ben"})
        for service in services:
            self.check_snapshot(service.retry(batch, "concurrent-key"), batch, expected)
            self.assertFalse(service.process_next())

    def test_running_status_is_observable_during_processing(self):
        entered, release = threading.Event(), threading.Event()
        failures = []

        def processor(row):
            entered.set()
            if not release.wait(timeout=15):
                raise RuntimeError("oracle timed out waiting to release processor")
            return row["name"]

        worker = SERVICE(self.db, processor)
        batch = worker.submit("running-state", [{"rowId": "a", "name": "Ada"}])["batchId"]

        def process():
            try:
                worker.process_next()
            except BaseException as error:
                failures.append(repr(error))

        thread = threading.Thread(target=process, daemon=True)
        thread.start()
        try:
            self.assertTrue(entered.wait(timeout=5), "Worker never invoked processor")
            snapshot = self.service.snapshot(batch)
            self.assertEqual(snapshot.get("contractVersion"), 2, snapshot)
            self.assertEqual(snapshot.get("status"), "RUNNING", snapshot)
            self.assertEqual(self.sql("SELECT status FROM batches WHERE id = ?", (batch,)),
                             [{"status": "RUNNING"}])
        finally:
            release.set()
            thread.join(timeout=15)
        self.assertFalse(thread.is_alive())
        self.assertEqual(failures, [])
        self.check_snapshot(worker.snapshot(batch), batch, {"a": ("SUCCEEDED", 1)})

    def test_settled_limit_validation_and_missing_batch(self):
        valid = [{"rowId": str(number), "name": "Name " + str(number)} for number in range(100)]
        invalid_rows = [None, {}, [], valid + [{"rowId": "overflow", "name": "N"}],
                        [{}], [None], [{"rowId": 1, "name": "N"}],
                        [{"rowId": " ", "name": "N"}], [{"rowId": "a", "name": " "}],
                        [{"rowId": "a", "name": 42}],
                        [{"rowId": "a", "name": "A"}, {"rowId": "a", "name": "B"}]]
        for rows in invalid_rows:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                self.service.submit("invalid-rows", rows)
        for request_id in (None, "", " \t", 7):
            with self.subTest(request_id=request_id), self.assertRaises(ValueError):
                self.service.submit(request_id, valid[:1])
        self.assertEqual(self.sql("SELECT * FROM batches"), [], "Invalid input persisted a batch")
        self.assertEqual(self.sql("SELECT * FROM items"), [])
        self.assertEqual(self.sql("SELECT * FROM records"), [])
        receipt = self.service.submit("hundred", valid)
        batch = receipt["batchId"]
        self.check_snapshot(receipt, batch, {row["rowId"]: ("QUEUED", 0) for row in valid})
        for request_id in (None, "", " \t", 7):
            with self.subTest(retry_id=request_id), self.assertRaises(ValueError):
                self.service.retry(batch, request_id)
        with self.assertRaises(KeyError):
            self.service.snapshot("missing-batch")
        with self.assertRaises(KeyError):
            self.service.retry("missing-batch", "valid-retry")
        self.assertTrue(self.service.process_next())
        self.check_snapshot(self.service.snapshot(batch), batch,
                            {row["rowId"]: ("SUCCEEDED", 1) for row in valid})
        self.check_records(batch, {row["rowId"]: row["name"] for row in valid})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()
    candidate = args.candidate.resolve(strict=True)
    if not (candidate / "backend" / "service.py").is_file():
        parser.error("candidate must contain backend/service.py")
    sys.path.insert(0, str(candidate))
    global SERVICE
    module = importlib.import_module("backend.service")
    if not Path(module.__file__).resolve().is_relative_to(candidate):
        raise RuntimeError("Imported backend.service did not come from the candidate directory")
    SERVICE = module.ImportService
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RevisionTwoTests))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
