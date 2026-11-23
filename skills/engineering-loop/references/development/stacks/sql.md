# SQL schema, index and transaction rules

**ID:** `dev.stack.sql` · **Status:** available, adapted from public sources and unconfirmed for the team. Use when a change adds or alters a table, index, constraint, migration or locking query on PostgreSQL or MySQL. Project instructions and the team stack rules win where they differ. Applying a migration stays under [stage 05](../../stages/05-release.md).

The lock-avoiding steps matter for a table that already holds production data. A new table or a confirmed new installation does not need them.

## Both engines

- Composite index: equality columns first, then the range or sort column. A range predicate stops later columns from filtering. A non-unique single-column index that is the leftmost prefix of a composite one is redundant.
- Index every column used as a foreign key or join key, and the selective columns an `UPDATE` or `DELETE` filters on.
- Keep the indexed column bare in a predicate: no function, arithmetic or implicit type conversion on it.
- Page by keyset: `WHERE (sort columns) > (cursor)` on an index, with every sort column in the cursor, ending in a unique one. `OFFSET` reads and discards every skipped row. On MySQL write the comparison in expanded form; a row-value inequality is not used as an index range.
- Keep a transaction short. No HTTP, model, storage or broker call inside it.
- Lock rows in one consistent order (by primary key) in every transaction that touches the same set.
- Replace select-then-insert with one atomic upsert on a unique key.
- Change a column type in steps: add the new column, write both, backfill, move reads, stop writing the old one, drop it in a later release.

## PostgreSQL

- Create or drop an index on a live table with `CONCURRENTLY`, which cannot run inside a transaction. In Alembic use `postgresql_concurrently=True` inside an autocommit block, in `downgrade` as well.
- Add a unique constraint by building the unique index concurrently, then attaching it with `ADD CONSTRAINT … USING INDEX`.
- Add a foreign key or check constraint as `NOT VALID`, and run `VALIDATE CONSTRAINT` in a later migration.
- `ADD CONSTRAINT IF NOT EXISTS` does not exist. Guard a rerunnable constraint with a catalog check.
- A foreign key creates no index on the referencing column. Add it.
- When queries always carry the same filter (not deleted, pending), use a partial index with that predicate. Add `INCLUDE` columns only for a frequent query the index can then answer alone.
- Claim queue rows with `FOR UPDATE SKIP LOCKED` inside the single statement that marks them taken.

## MySQL (InnoDB)

- The primary key is the clustered index. Keep it monotonic: an auto-increment `BIGINT` or a time-ordered identifier. A random UUID as primary key splits pages and widens every secondary index.
- State `ALGORITHM` on an `ALTER TABLE`, and `LOCK=NONE` with `INPLACE`, so it fails instead of silently copying the table. Adding an index is in-place, not instant; a column type change copies.
- An in-place change still waits for open transactions at its start and end. A long transaction blocks it.
- When a table is too large for built-in online DDL, raise it with the owner and use the project's existing schema-change procedure. Do not install a tool.
- Under the default isolation level a locking read of a range, or of a row that does not exist, also locks the gap. Check-then-insert under `FOR UPDATE` can deadlock; rely on a unique key instead.
- Retry a deadlock (error 1213) only as the whole transaction, with bounded backoff, and only when it has no effect outside the database.
- Do not change the isolation level globally.

## Verify

Read the query plan for the changed query on realistic volume, and state the lock each migration statement takes. An empty test database shows neither. Record steps left unapplied in the [delivery record](../delivery.md).
