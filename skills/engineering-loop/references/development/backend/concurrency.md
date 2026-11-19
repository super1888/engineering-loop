# B4 Transaction and concurrency changes

**ID:** `dev.backend.concurrency` · **Status:** available execution baseline; transaction annotations, isolation and legal lock order remain project facts.

## Scope and inputs

Use when mutable preconditions, overlapping writers, stale edit bases, atomicity or uncertain commits affect the change. Identify actual transaction entrypoints/propagation, earlier reads, resource ownership, lock/version checks and durable effects. Pure unaffected transformations do not need a transaction protocol.

## Execute

1. Write the relevant ordering as a concrete timeline: actors, observed state/version, competing change, final check, write and commit. Distinguish sequential stale-page saves from simultaneous transactions.
2. Trace effective boundaries through real callers, proxies and callbacks; an annotation or held lock does not itself prove when a read view refreshes or which work joins the transaction.
3. Apply [R5](../rules/concurrent-edits.md) for mutable preconditions or stale saves. Preserve existing equivalent protection rather than adding a second version/locking protocol.
4. Apply [R6](../rules/split-transactions.md) only when reservation/work commit separately and [R4](../rules/async-idempotency.md) for operation retries/unknown outcomes. A thrown call alone is not proof of rollback or absence.
5. Coordinate the writers that can invalidate the final decision, preserving legal lock order and required authorization. Change isolation/locking only to address the demonstrated ordering, not as a project-wide remedy.

## Verify

- Exercise the harmful ordering and a valid success control with independent expectations; inspect affected rows, stored versions and effects, including no extra effect after rejection.
- Use real database isolation and independent connections when claiming database concurrency/rollback behavior; proxy/model tests establish only their tested level.
- For stale editors, verify an unchanged-base success and stale-base rejection with input available for reconciliation where that client flow is affected.

## Deliver and bind

Record the failed timeline, chosen coordination boundary, changed contract, actual environment and checked orderings using [delivery evidence](../delivery.md). Keep project lock order, isolation defaults and retry/transaction framework conventions with their owning sources; a local repair does not authorize a global transaction rewrite.
