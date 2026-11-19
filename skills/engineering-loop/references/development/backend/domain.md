# B2 Domain and service changes

**ID:** `dev.backend.domain` · **Status:** available execution baseline; project-specific layering and domain policy remain project-owned.

## Scope and inputs

Use when business invariants, responsibility, dependency direction or data-write ownership change. Gather the accepted examples, effective domain terms, current callers, authoritative state and representative implementation. A settled local detail needs no architecture workshop.

## Execute

1. State the invariant as an observable accepted/rejected example, including which actor owns the decision and which data proves it. Keep unknown policy unresolved.
2. Trace where the current path checks the invariant and performs each effect. Reuse established module/service responsibilities; names and folders alone do not establish conformance.
3. Place the change at the maintained responsibility boundary and account for affected callers. Do not duplicate business decisions in transport and persistence merely to make each layer appear complete.
4. Preserve necessary validation, permissions and recovery. Apply [R2](../rules/access.md), [R3](../rules/read-only.md) or [R6](../rules/split-transactions.md) only when the corresponding boundary changes.
5. Verify one representative slice before replicating it. If a new abstraction, service or architecture choice is necessary, establish the missing capability and maintenance cost; a consequential new commitment needs its authorized decision.

## Verify

- Check the ordinary successful example, relevant invariant violation and resulting durable state/effects against independently accepted expectations.
- Confirm the affected dependency/write ownership through actual calls; an equivalent existing implementation may be valid without matching a preferred class layout.
- Check applicable callers for the same demonstrated cause without expanding a local correction into an unrelated repository audit.

## Deliver and bind

Record the invariant, responsibility/caller changes, representative implementation, tests and remaining decisions using [delivery evidence](../delivery.md). Use [project guidance](../../project.md) for missing or conflicting conventions. Concrete module layout, service patterns and business exceptions remain bound to project-owned sources.
