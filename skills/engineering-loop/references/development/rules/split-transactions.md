# R6 Separately committed reservations and work

**ID:** `dev.risk.split-transactions` · **Status:** available existing boundary guidance.

**Trigger:** The reservation and its work item commit in separate transactions. Read the actual commit/callback and contender boundaries before interpreting an exception as absence.

When a reservation and its work item commit in separate transactions, a thrown call does not prove the work item is absent: a post-commit callback can fail, or another contender using the same operation identity can commit. Release the reservation only after the durable absence of work and the absence of a still-committing contender are established at a coordinated boundary. Otherwise retain its operation identity for retry or reconciliation, and define how a genuinely orphaned reservation is eventually settled. This extra coordination is unnecessary when both facts share one atomic transaction and rollback is authoritative.

**Nearby exception:** One atomic transaction with authoritative rollback does not need this split-commit coordination protocol.

**Verification:** Read and apply [Split transactions](../../verification-boundaries.md#split-transactions) for the real isolation/independent-connection evidence boundary. A mocked exception alone cannot prove absence or safe release. Apply [R4](async-idempotency.md) when the operation's retry/state contract also changes.
