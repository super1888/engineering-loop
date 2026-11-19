# B6 Asynchronous work and jobs

**ID:** `dev.backend.async-jobs` · **Status:** available execution baseline; queue, scheduler, retry and recovery policies remain project bindings.

## Scope and inputs

Use for state transitions, scheduling, queued work, duplicate calls, retries or recovery. Identify the operation owner/identity, accepted states, durable work record, acknowledgement versus completion signal, downstream effects and actual retry mechanism. Synchronous pure work needs no job infrastructure.

## Execute

1. Trace acceptance, scheduling, execution, completion and failure/recovery across actual persisted state; use [R4](../rules/async-idempotency.md). A configured worker count does not establish execution or throughput.
2. Preserve the operation identity across retries and unknown outcomes. Reconcile durable work/downstream results before repeating an effect; a timeout does not establish that nothing committed.
3. Locate the ownership/coordination mechanism and legitimate recovery conditions. Do not declare work failed or start a replacement from elapsed time alone when the accepted lease/state contract says otherwise.
4. Apply [R6](../rules/split-transactions.md) for separately committed reservations/work and [R5](../rules/concurrent-edits.md) for competing finalization. Preserve successful ordinary execution and legal transition order.
5. Derive retry, backoff, cancellation and timeout behavior from the existing contract, provider constraint or demonstrated resource requirement. Do not invent fixed delays/counts or expand a feature with unrequested polling/recovery semantics.

## Verify

- Check one ordinary accepted-to-completed path and the affected duplicate, failure or unknown-result recovery ordering, including durable effects and final state.
- Where retries can repeat effects, verify that the same operation does not create an unintended second result and that a legitimately new operation can still proceed.
- Exercise actual scheduling/worker integration when claiming it works; mocked enqueue calls alone do not establish worker execution or downstream completion.

## Deliver and bind

Record the state/ownership contract, operation identity treatment, tested recovery cases and unrun external boundaries using [delivery evidence](../delivery.md). Bind queue/scheduler packages, leases, retry policy and observability to maintained project sources; unknown business recovery choices remain explicit.
