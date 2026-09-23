# Demonstrated project lessons

Keep this small. Business/stack defects belong with their executable safeguards; a local incident is not automatically a generic skill rule.

## SQLite transaction completion does not release the connection

- **Trigger and evidence:** During the 2026-09-21 trial, the independent oracle's temporary database cleanup failed on Windows with file-in-use errors for both candidate implementations.
- **Root cause:** The evaluator used an SQLite connection as a transaction context and assumed that leaving it also closed the connection. Its inspection/trigger connections could remain open until collection.
- **Why checks missed it:** Distribution checks did not execute the oracle. The incomplete receipt fixture failed before many inspection paths, so its initial failures did not establish that the evaluator cleaned up a successful run correctly.
- **Correction:** The evaluator explicitly closes the connections it creates; transaction contexts remain around its writes. Candidate implementations and accepted business assertions were not changed to hide the failure.
- **Safeguard:** `python -m unittest discover -s tests -p test_receipt_oracle.py -v` verifies that receipt inspection releases its connection. It failed before the fix and passed after it. The normal root unittest command in existing CI includes this test.
- **Applicability:** Helpers that own SQLite connections and disposable database files, especially where open handles prevent cleanup. Do not apply this as a ban on transaction contexts or manually close a borrowed/shared application connection.
- **Owner and transfer:** Maintainers changing the oracle own this check. For another Python/SQLite project, first inspect connection ownership, then adapt and run the regression there. No second-project adoption has been demonstrated yet.
- **Review condition:** Revisit if the evaluator's persistence or ownership model changes. Remove or replace the check if the failure boundary no longer exists; do not retain an irrelevant rule solely as history.
