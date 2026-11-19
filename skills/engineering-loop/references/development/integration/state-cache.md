# I7 Verify state and cache consumers

**ID:** `dev.integration.state-cache` · **Status:** available execution baseline; project cache ownership remains pending.

Use when a changed persisted result must appear across pages, modules, refreshes or return paths. A local variable with no affected consumer does not require cross-module invalidation. Use the evidence boundaries in [verification](../../verification.md).

## Inputs

Identify the authoritative state/version, mutation owner, affected readers/caches, supported entry/return/reload paths and artifact/configuration versions. Reuse accepted context-retention and unsaved-input decisions; locate actual cache keys and ownership from the implementation rather than inventing a new store.

## Execute

1. Trace the write to persistence and each affected read/projection/cache. Distinguish an optimistic local value, invalidation signal, refetch result and committed state.
2. Reuse the existing ownership and invalidation mechanism at the changed boundary. Do not add global refreshes, duplicate stores or broad cache clearing when a scoped update preserves the accepted contract.
3. Inspect transition order and operation identity when asynchronous responses can affect the result; apply [R4](../rules/async-idempotency.md) where relevant.
4. Preserve editing base and unsaved input where another client can change the resource, applying [R5](../rules/concurrent-edits.md) only for that actual write boundary.
5. Follow the affected supported return/reload paths. For visible claims, use [rendered behavior](../../ui.md#accept-the-rendered-behavior) and [R9](../rules/rendered-ui.md); a callback or invalidation spy alone is insufficient.

## Verify

- Confirm the authoritative committed result and what the affected consumer sees after the supported action/return path, preserving accepted filters/context.
- Use a relevant delayed response, repeated navigation or stale-edit example when it can distinguish the reported defect; do not impose every ordering on a synchronous local edit.
- Verify the intended path without relying on an unrelated forced full refresh. Separate store/unit assertions, rendered interaction and real persistence integration.

## Deliver

Record affected writers/readers, artifact identity, tested paths and ordering, actual stored/visible outcomes and gaps in the existing [delivery record](../delivery.md). Keep detailed cache conventions at their maintained source.

## Team bindings — pending

Bind query/store ownership, cache-key conventions, update/invalidation policy and supported recovery behavior. No universal state library or cache framework is required.
