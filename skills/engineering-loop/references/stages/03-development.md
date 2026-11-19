# 03 Development and integration · 开发与联调

## Enter

Use after the entrypoint's MCP gate for an authorized implementation slice, reproducible defect or cross-module/system integration. Frontend, backend and integration are focused work within this stage, not additional project phases.

## Inputs

Reuse the effective behavior, applicable design/contracts, current code and project commands, relevant callers and task dependencies. An already clear local fix needs no new PRD or design round; investigate a missing prerequisite only when the next action depends on it.

## Execution and focused references

Read [implementation.md](../implementation.md) for slice selection, defect diagnosis and affected engineering boundaries. For frontend interaction or visual changes, also read the applicable [ui.md](../ui.md) guidance; for missing conventions or inherited architecture, use [project.md](../project.md).

Select an available project specialist by the affected stack through [specialists.md](../specialists.md) only when needed. Read [collaboration.md](../collaboration.md) for shared ownership or integration; use [verification.md](../verification.md) for applicable checks without waiting for a separate project-wide testing phase.

Apply the [common challenge](../grill.md) to the affected contracts, state and failure example. Check code and accepted decisions first; ask only a consequential unresolved choice. Do not invent business policy to unblock implementation.

## PMS

Use [pms.md](../pms.md) when applicable. Reuse or create authorized tasks at independently deliverable behavior boundaries; identify actual integration dependencies rather than copying one integration card per module. Resolve responsible ownership before claiming and read back mutations; a stage label is not a board state or an exclusive lock.

## Deliverables

Produce the scoped code/configuration changes, relevant regression or integration checks, artifact/version identity and remaining limits. Update maintained contracts or documentation when the change requires them; use project conventions for paths and templates.

## Exit and return

The slice must implement its accepted behavior and pass its required checks. Return a consequential behavior/design conflict to [requirements](01-requirements.md) or [design](02-design.md), affecting only dependent work. Enter [testing and acceptance](04-testing.md) when broader verification or acceptance is required; a verified local change does not require unrelated stages.
