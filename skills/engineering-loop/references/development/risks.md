# Conditional development risk index

Inspect these trigger summaries for the current change, then read only matching bodies. These are shared rules across professional scenes and stacks, not nine mandatory full reads. A rule's nearby exception cannot waive applicable project instructions, required full reads or another genuinely affected boundary. Unknown applicability calls for a focused fact check, not an assumed exclusion.

**Status:** available existing guidance or a focused pointer to its maintained source. Concrete stack standards, role matrices and component conventions are not supplied by this index.

| ID | Trigger | Nearby exclusion / boundary | Body |
|---|---|---|---|
| R1 | Values may lose identity or precision across representations | A label-only edit with unchanged value flow | [Data fidelity](rules/data-fidelity.md) |
| R2 | Identity, role, resource ownership or a shared-user access path changes | Formatting with no access-path change | [Access](rules/access.md) |
| R3 | The accepted flow promises read-only behavior and delegates calls | An intentionally mutating flow retains its authorized writes | [Read-only effects](rules/read-only.md) |
| R4 | Stateful/async transitions, retries, duplicates or result-unknown recovery | Pure deterministic formatting without state/effects | [Async and idempotency](rules/async-idempotency.md) |
| R5 | Mutable preconditions or stale/concurrent saves can invalidate a write | Existing equivalent protection or append-only work needs no second protocol | [Concurrent edits](rules/concurrent-edits.md) |
| R6 | A reservation and its work item commit separately | One atomic transaction with authoritative rollback | [Split transactions](rules/split-transactions.md) |
| R7 | Upload content identity, resumability, direct storage or quota is affected | Unchanged metadata display does not itself alter an upload protocol | [Uploads](rules/uploads.md) |
| R8 | An SDK transitive dependency is excluded or replaced on an affected path | Unaffected pure serialization needs no transport probe | [SDK transport](rules/sdk-transport.md) |
| R9 | A conclusion concerns rendered layout, interaction or accessibility | Nonvisual metadata changes need no unrelated rendering matrix | [Rendered UI](rules/rendered-ui.md) |

The stable machine-readable rule IDs are `dev.risk.data-fidelity`, `dev.risk.access`, `dev.risk.read-only`, `dev.risk.async-idempotency`, `dev.risk.concurrent-edits`, `dev.risk.split-transactions`, `dev.risk.uploads`, `dev.risk.sdk-transport` and `dev.risk.rendered-ui`; R1–R9 are navigation labels. Each body owns its trigger, exclusion and evidence pointer. Missing project-specific detail remains a gap to investigate only when the current action depends on it.
