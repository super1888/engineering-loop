# Team Python / FastAPI service rules

**ID:** `dev.stack.python-fastapi` · **Status:** partial. Extracted on 2026-11-21 from the one team service on this stack, keeping rules that are generic to the stack. Two come from recorded incidents. Confirmation as the cross-project standard is pending.

Use when the affected module is a Python service on FastAPI and SQLAlchemy. An existing project's effective instructions and checks win where they differ. Baseline observed: Python 3.12, FastAPI, Pydantic 2, SQLAlchemy 2 with synchronous sessions, Alembic, PostgreSQL; confirm the module's own versions first.

## Concurrency and transactions (B4)

- Use synchronous SQLAlchemy sessions with plain `def` routes and dependencies wherever the database is touched. Never touch the database on the event-loop thread. An `async def` that takes a session is the sign of a miss. Recorded incident: an `async` auth dependency doing synchronous database work stalled the process once concurrency exceeded the pool, and serial tests did not show it.
- Read a response built from several queries inside one snapshot, such as one read-only repeatable-read transaction. Recorded incident: under read committed an endpoint returned an old version with a new cursor, so clients missed an update.
- Update with `If-Match`: `UPDATE … WHERE version = :v`, zero rows is a failed precondition, and a missing header is rejected. See [R5](../rules/concurrent-edits.md).

## Structure (B2)

- Enforce layering with import-linter: outer layers (API, runtime, infrastructure) depend on the application layer, which depends on the domain. The domain imports no framework, infrastructure or environment access. The application layer does not import SQLAlchemy or `os`. Wiring lives in one bootstrap module and environment variables are read in one settings module.
- Change a status only through one pure domain transition function, with a parametrized test of every legal and illegal pair.
- Inject the clock and the ID generator. No `datetime.now()` or `uuid4()` in the domain or application layer.

## Access (B5)

- Return 404 for a resource the caller cannot see and 403 only for one that is visible but not permitted. Take the organisation and actor from the session and reject a body that carries them. See [R2](../rules/access.md).

## Persistence (B3)

- Hand-write Alembic migrations and never edit a committed one. Do not commit raw autogenerate output. A `downgrade` either works or raises. Test the full run from an empty database.

## Testing and checks

- Run database tests on real PostgreSQL only, and fail when it is missing instead of skipping. No SQLite and no mocked session.
- Do not add `skip`, `xfail`, `# type: ignore` or `# noqa` without a reason on the line and disclosure in the delivery record.
- Keep `ruff`, `mypy --strict` and the import contracts green without weakening them.
