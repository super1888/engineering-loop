# F5 State and asynchronous UI

**ID:** `dev.frontend.async-state` · **Status:** available execution baseline; state-library conventions remain pending.

## Scope and inputs

Use when loading/error feedback, request ordering, duplicate actions, cache refresh or asynchronous completion changes. Establish the accepted operation identity, state owner, result protocol and visible completion signal. A synchronous local change does not acquire an asynchronous workflow merely because a state library exists.

Retain the relevant [interactive-slice guidance](../../ui.md#test-the-uncertain-decision-before-replication) and [visible result/return-path requirements](../../ui.md#accept-the-rendered-behavior); an accepted direction needs no new design comparison.

## Execute

1. Trace the actual operation from user action through request identity, response and visible state. Separate request accepted, operation complete and result unknown when the contract distinguishes them.
2. Associate a response with the operation/context that produced it. If a later selection supersedes a request, stop an obsolete response from replacing the current view; retain separate valid results when the flow permits concurrent work.
3. Reuse the existing state/cache mechanism and ownership. Local request abort or component unmount does not by itself cancel server work; use the accepted cancellation/recovery contract rather than inventing one.
4. Apply [R4](../rules/async-idempotency.md) for retries/duplicates/unknown outcomes and [R5](../rules/concurrent-edits.md) for competing persisted edits. Follow a real cross-service completion boundary only when it is part of this task.
5. Make the affected transition and result observable without duplicate feedback or lost input. Use the actual status protocol; do not conceal uncertainty with a fixed delay, guessed polling schedule or success notification before completion.

## Verify

- Use an applicable delayed/out-of-order or failure sequence plus a normal sequence with independently expected visible results.
- Follow supported refresh/return paths to the actual persisted or current state. A callback/cache-invalidation spy does not establish the displayed outcome.
- For status, focus or accessibility claims, use [R9](../rules/rendered-ui.md); distinguish DOM state from a verified assistive-technology announcement.

## Deliver

Record state/operation ownership, affected transition ordering, visible completion and recovery evidence through [delivery records](../delivery.md). Report missing protocol decisions and keep dependent behavior waiting rather than inventing polling or retry policy.

## Team binding — pending

State/query packages, cancellation conventions, notification components and cache ownership remain project-specific. Existing accepted mechanisms take precedence over a new global state abstraction.
