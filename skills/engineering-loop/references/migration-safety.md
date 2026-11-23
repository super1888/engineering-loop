# Keep a data or schema migration recoverable

Use with [release.md](release.md) when a release changes stored data, a schema or an interface that old and new versions share. The project's migration policy and runbooks take precedence. This guide sets conditions on an authorized migration and authorizes none.

## Expand, then contract

- Add the new structure beside the old one so both the previous and the new version run against it. Removing the old structure belongs to a later release, never the one that introduces the new.
- Give the compatibility window a checkable end condition: a date, a measured threshold, or a list of consumers each confirmed migrated. Until it is met, the old path stays.
- Keep backfill separate from the schema change, in batches that can be rerun.
- Record the step after which redeploying the previous version stops working. From there the only paths are roll-forward or restore.

## Reconcile before cutover

Compare source and target on counts, representative content or checksums, and records written while the backfill ran. An unexplained mismatch stops the cutover. A tolerance counts only if it was agreed before the numbers were seen.

Name the steps at which the cutover can be paused or reversed. A cutover with none is a risk to raise with its owner, not a detail.

## Label every step with one recovery class

| Class | Meaning |
|---|---|
| Rollback | The step can be undone and the previous version works afterwards |
| Roll-forward | Recovery is a further fix in the new state |
| Restore | Recovery returns to a backup or snapshot and loses writes made after its recovery point |
| Irreversible | No recovery exists |

Each step gets exactly one class. Do not write rollback for a step whose real recovery is a restore. For an irreversible step, say whether reversal is impossible or was not built. It runs only after the owner of the affected data acknowledges that named step, unless an approval or project policy already names it; a general release approval is not that acknowledgement. Without it the step waits while other preparation continues.

Never state that a migration can always be rolled back. State up to which step it can, and what applies after.

Put the classes, window end condition, reconciliation result and acknowledgements in the release record's migration and recovery fields.
