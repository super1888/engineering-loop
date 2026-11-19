# I5 Trace asynchronous business completion

**ID:** `dev.integration.async-flow` · **Status:** available execution baseline; queue/status/recovery protocols remain pending.

Use when accepted work completes later across clients, services or workers. Preserve an accepted synchronous flow; missing detail does not authorize polling, callbacks or new states. Apply [R4](../rules/async-idempotency.md).

## Inputs

Identify the operation and responsible producer/consumer/worker, artifact/configuration versions, accepted state transitions, completion signal and supported return path. Locate actual scheduling, status/callback contracts, dependencies and authorized recovery behavior.

## Execute

1. Trace submission, acceptance, scheduling, durable transitions and completion independently. An accepted response is not a completed user outcome.
2. Preserve the established operation identity and ownership through retry, reconnect or handoff. A transport loss or quiet observation is not proof that underlying work failed; reconcile actual state before recovery.
3. Check the real completion mechanism and affected client feedback. Use the existing status view, callback or polling contract; do not add another mechanism or fixed wait/retry count to hide unknown state.
4. Follow independently committed steps through [R6](../rules/split-transactions.md), and competing transitions through [R5](../rules/concurrent-edits.md), only when relevant. Resolve consequential missing failure/recovery policy before dependent effects.
5. Verify the visible completion and supported return behavior using [UI slice guidance](../../ui.md#test-the-uncertain-decision-before-replication) only where the client is affected. A simulated state or configured thread count cannot prove real execution.

## Verify

- Observe the accepted path from submission to the agreed durable/visible result; identify which components and actual environment executed it.
- Exercise a relevant failure, duplicate notification or reconnect/recovery case from the accepted contract, checking retained identity and protected effects.
- Separate scheduling, throughput, service integration and user-acceptance claims. State an unavailable worker or unobserved terminal state as unrun/unknown.

## Deliver

Link operation/artifact identity, observed transitions, completion evidence and unresolved recovery/ownership facts in the existing [delivery record](../delivery.md). Retain a live handle and custodian when ongoing work survives the slice.

## Team bindings — pending

Bind actual queue/status/callback protocols, state owners, timing/resource limits and authorized recovery semantics. This baseline supplies no universal state machine or scheduler.
