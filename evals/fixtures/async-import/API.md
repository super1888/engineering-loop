# Batch API — revision 1

POST /api/batches with `{ "requestId": "client-operation", "rows": [{ "rowId": "alpha", "name": "Ada" }] }` accepts work with HTTP 202. The response includes batchId and status QUEUED. GET /api/batches/{batchId} returns batchId, status, total, succeeded and failed. Status values are QUEUED, RUNNING, SUCCEEDED, PARTIAL and FAILED.

Processing is atomic for the whole batch: if any row fails, all imported rows from that batch must roll back. This describes revision 1 behavior and has the same authority as PRODUCT.md until an owner decision resolves any disagreement.

An identical repeated requestId returns the original batch identity; different data with that requestId returns 409. Input errors return 400 and missing batches return 404. Row identifiers are strings and must not be converted to numeric identifiers. Validation rejects empty rows, duplicate rowIds or blank names before accepting work.

An older example mentions a maximum of 50 rows; consult the maintained decisions for the active limit.
