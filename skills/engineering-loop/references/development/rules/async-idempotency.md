# R4 Async state, idempotency and unknown results

**ID:** `dev.risk.async-idempotency` · **Status:** available existing boundary guidance.

**Trigger:** The slice changes stateful or asynchronous behavior, scheduling, duplicate calls, retries, partial failure or recovery after an unknown result. Inspect the actual effect and operation identity before selecting a recovery behavior.

For stateful or asynchronous changes, identify operation ownership, transitions, idempotency, result-unknown behavior, and recovery. Consider real boundary behavior when transactions, caches, queues, authentication, or external services interact. Verify actual scheduling rather than equating configured threads with throughput.

**Conditional links:** Read [R6](split-transactions.md) only when reservation/work commits are separate; [R5](concurrent-edits.md) when mutable preconditions or stale saves also apply. Do not preload either because the word "async" appears.

**Nearby exception:** Pure deterministic formatting with no operation state or external effect needs no retry protocol, scheduler or idempotency store.

**Verification:** Apply the relevant state, duplicate-call, unknown-result and recovery checks in [verification.md](../../verification.md). A framework-specific queue or retry standard is pending team detail; use the effective project contract instead of inventing one.
