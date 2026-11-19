# F3 Lists and tables

**ID:** `dev.frontend.collections` · **Status:** available execution baseline; team table/query conventions remain pending.

## Scope and inputs

Use for affected filtering, pagination, sorting, selection, batch actions or collection states. Identify query ownership, row identity, accepted ordering/pagination semantics, applicable permissions and the selected action's result. An unrelated table elsewhere does not enter this scope.

Use the applicable [representative-content guidance](../../ui.md#start-with-a-task-and-representative-content) and [rendered behavior requirements](../../ui.md#accept-the-rendered-behavior) for actual interface claims, without restarting an accepted design.

## Execute

1. Trace query state from controls/URL through the actual request to displayed rows and totals. Preserve the project's ownership of filters, sort and page state; confirm what changes after a filter update instead of assuming a reset policy.
2. Use stable resource identity for row actions and selection. Distinguish a page selection from all matching records only when the feature supports both; do not silently broaden a batch operation.
3. Keep no results, loading, failed lookup and unavailable action distinct when relevant. Use representative long, missing and zero-valued content to check information density without inventing additional columns or states.
4. For batch writes, reconcile per-item/whole-operation outcomes against the actual contract. Apply [R4](../rules/async-idempotency.md) to unknown or repeated results and [R2](../rules/access.md) to actor-scoped rows/actions.
5. After a supported edit or return navigation, refresh/reconcile the affected result through the existing mechanism. Do not equate an invalidation callback with the updated rows the user sees or add global refresh behavior unnecessarily.

## Verify

- Check the affected query, sort/page transition and visible row/action result using independently known sample data.
- Cover relevant empty/error and return states; inspect long content on the accepted target with [R9](../rules/rendered-ui.md) when making layout claims.
- Use [R1](../rules/data-fidelity.md) when row identifiers or quantities cross representation boundaries. Measure an actual performance defect before changing pagination strategy or imposing limits.

## Deliver

Record changed query/action semantics, row identity/selection scope and observed returned results through [delivery records](../delivery.md). Report unsupported query combinations rather than treating one successful page as total coverage.

## Team binding — pending

Table package, query-state conventions, page-size policy, selection semantics and batch-action presentation remain project choices grounded in accepted examples.
