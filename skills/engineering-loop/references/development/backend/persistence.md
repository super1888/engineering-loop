# B3 Data and persistence changes

**ID:** `dev.backend.persistence` · **Status:** available execution baseline; database, ORM and migration conventions remain project bindings.

## Scope and inputs

Use for query, constraint, field, conversion or migration-code changes. Identify the actual schema/model, data owner, affected callers, relevant data volume and supported installation/upgrade state. Merely using a database does not require a schema task.

## Execute

1. Trace API/domain fields to stored columns and conversions; preserve the established repository/query boundary and parameter handling. Apply [R1](../rules/data-fidelity.md) when conversion can change a value's meaning or precision.
2. Scope reads/writes to the requested actor, resource and result set. Check actual filtering, ordering, pagination and indexes where the changed query depends on them; do not infer correctness from method names or fetch unrelated data by convenience.
3. Locate the constraints that enforce uniqueness, ownership and atomic state changes. Keep required guarantees at an enforceable boundary and select [R5](../rules/concurrent-edits.md) or [R6](../rules/split-transactions.md) only for the actual update/commit model.
4. For schema changes, follow the project's authoritative baseline, upgrade and generation policy. Establish whether historical data/clients exist before choosing compatibility work; do not silently rewrite a released migration or impose upgrades on a confirmed new installation.
5. Separate preparing migration code from applying it. Record prerequisites, data impact and necessary recovery. Apply a release migration under [stage 05](../../stages/05-release.md) authority and route an independent live maintenance or recovery task to [stage 06](../../stages/06-operations.md).

## Verify

- Inspect the stored result and relevant constraint/rejection path, not only the returned DTO or mocked query call. Use [R3](../rules/read-only.md) if the accepted flow promises no writes.
- Where schema evolution is part of acceptance, exercise the required empty/current/historical-data and rerun paths in an explicitly configured environment; select only paths supported by the actual project contract.
- Distinguish model/ORM checks from real database ordering, isolation and query behavior through [verification](../../verification.md).

## Deliver and bind

Record affected entities/queries, schema and migration identities, data assumptions, actual checks and unapplied steps using [delivery evidence](../delivery.md). Bind ORM/database versions, schema ownership and deployment commands to maintained project sources; no default migration tool or dialect is prescribed here.
