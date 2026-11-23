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

## Adapted from public sources (unconfirmed for the team)

A team rule above wins where they differ. Nothing here adds a package.

- Declare parameters and dependencies with `Annotated`, and give each shared dependency (session, current actor) one type alias that routes reuse.
- Declare a return type on every route; it filters the response. Use `response_model` when the returned object differs from the public schema. Never return an ORM row whose extra columns would leak.
- `async def` is valid only when everything inside is non-blocking. In doubt, plain `def`, for dependencies as well.
- Put the prefix, tags and shared dependencies on the `APIRouter`, not in `include_router()`. Attach authentication there, so a new route cannot omit it, and mark each public route explicitly.
- Do not introduce `ORJSONResponse` or `UJSONResponse`; current FastAPI deprecates them in favour of a declared return type.
- Request models on write endpoints forbid unknown fields (`extra="forbid"`). Never spread a raw body `dict` into a model or an update.
- Disable or protect `/docs`, `/redoc` and `/openapi.json` in production.
- Verify a JWT's signature against an explicit algorithm allowlist and check `exp`, plus `iss` and `aud` when several services share an issuer. Its payload is readable by the client.
- A URL supplied by a caller and fetched by the server: `http` or `https` only, host allowlist, no loopback, private or metadata address, a timeout, and no redirects unless needed.
- Enforce an upload size limit in the application as well as at the edge. Check the type by content against an allowlist, store under a server-generated name and serve as an attachment. See [R7](../rules/uploads.md).
- Check migration locks and index shape against the [SQL rules](sql.md).
