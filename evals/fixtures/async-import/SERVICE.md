# Stable exercise interfaces

`backend.service.ImportService(db_path, processor=None)` initializes the schema and is safe to create again on the same SQLite path. The default processor returns the row name. An injected processor receives a dict containing rowId and name, returns the imported name, and may raise RuntimeError for a transient row failure.

- `submit(request_id, rows)` validates and returns a batch snapshot. ValueError means rejected input or a conflicting request identity; KeyError means a missing batch. Do not rename these entrypoints.
- `snapshot(batch_id)` returns the current snapshot.
- `process_next()` processes one queued batch, including its queued rows, and returns whether work was found. All persisted side effects and attempts must correspond to that work. Distinct service instances may use the same database; workers must not duplicate a claimed item.
- `retry(batch_id, request_id)` is reserved for an owner-approved later contract; revision 1 may raise NotImplementedError.
- `records()` returns imported rows as dictionaries with batchId, rowId and name. It is a read-only exercise inspection method.

SQLite tables are already created by backend/storage.py. Keep their names and existing columns so retained state is inspectable; additional columns/tables are allowed when justified. No live database is used.

server.py provides the HTTP/static adapter and a background worker. For deterministic local tests only, `--manual-worker` disables automatic scheduling and reads `process` commands from stdin. `--fail-once-row beta` injects one RuntimeError for that row identity before succeeding on later processing. These are local harness controls, not public HTTP endpoints. Preserve both modes and the CLI while changing the application.

The UI has existing ids: rows, submit, status, message, results, retry. Retain them for accessibility/test continuity. The results table displays the current batch's row identifiers and states when a contract supplies them. Keep user-entered form values intact after request failures.
