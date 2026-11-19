# I4 Reconcile writes and unknown outcomes

**ID:** `dev.integration.write-outcomes` · **Status:** available execution baseline; project operation protocol remains pending.

Use when retries, duplicates, uncertain responses, version conflicts or actual committed-state checks cross components. An authoritative unchanged read result needs no new write protocol. Apply [R4](../rules/async-idempotency.md), adding [R5](../rules/concurrent-edits.md) or [R6](../rules/split-transactions.md) only when their boundaries apply.

## Inputs

Identify the intended operation/effect, existing operation identity, request payload, observed editing base where relevant, authoritative state/read-back path, affected actors and producer/consumer artifact/configuration versions. Establish accepted duplicate, conflict and unknown-result outcomes.

## Execute

1. Trace request acceptance, durable effect and response production separately. Record what is known after an error; a thrown or timed-out call does not establish that nothing committed.
2. Reconcile the existing operation against authoritative state before repeating a non-idempotent action. Preserve the established operation identity and inspect actual service guarantees; do not claim exactly-once behavior from a local search-before-write convention.
3. For stale/concurrent edits, carry the accepted observed version to the final update boundary and preserve the user's unsaved input on rejection under R5. Reuse equivalent existing protection.
4. When multiple durable steps commit separately, follow R6 before releasing a reservation or declaring absence. Do not replay already-verified implementation merely to repair a pending synchronization.
5. During integration verification, establish the affected identity and fields from an authoritative write result or the existing read-back path, preserving unrelated concurrent changes. This is not a requirement to add a second production request after every write. Verify access to reconciliation under [R2](../rules/access.md) when ownership matters.

## Verify

- Exercise the accepted successful path and relevant duplicate/unknown-result or stale-version ordering, then inspect durable effects and operation identity.
- Confirm that rejected/conflicting work does not cause the prohibited duplicate or overwrite, while the valid operation remains possible.
- Distinguish mocked responses, actual service/database behavior and untested races. An assignment/read-back sequence is not an atomic lock.

## Deliver

Record operation/artifact identity, known outcome, reconciliation evidence, pending update or conflict and next authorized step in the existing [delivery record](../delivery.md). Do not label an unresolved result as success or absence.

## Team bindings — pending

Bind actual idempotency keys, reconciliation endpoints, version/conflict protocol and accepted recovery decisions. Missing policy does not authorize a new retry or cancellation rule.
