# Backend scenario index

Stage: 03. Area: backend. The routing entries and linked base rules are available; stack, framework and team-specific standards remain partial or pending. Read only matching sections and their necessary references. The [development core](../core.md) and every effective project instruction remain applicable.

Resolve language/framework/database versions from the affected module's maintained configuration and representative code. [Stack bindings](../stacks.md) are conditional pointers, not a supplied universal backend architecture. A browser “admin/backend page” alone does not select this index; require an actual service/data boundary.

## B1 APIs and contracts

- **ID / match:** `dev.backend.api`; routes, request/response models, validation, error semantics or OpenAPI operations. Exclude frontend-only copy/style changes.
- **Existing guidance:** [development core](../core.md), including the applicable API-operation inventory/contract gate; consult [project contracts](../../project.md) when ownership or conventions are missing.
- **Conditional rules:** [R1 data fidelity](../rules/data-fidelity.md) for representation changes; [R2 access](../rules/access.md) for authorization boundaries; [I1](integration.md#i1-interface-alignment) when consumers must be reconciled.
- **Verify:** the changed contract and owning checks with accepted/rejected examples and relevant callers, not just a successful route registration.
- **Pending:** endpoint naming, DTO/error conventions and API package choices, bound to maintained project contracts.

## B2 Domain and services

- **ID / match:** `dev.backend.domain`; business invariants, responsibilities, dependency direction or data-write ownership. Exclude a settled local detail that does not change these boundaries.
- **Existing guidance:** [development core](../core.md); read [project/reference architecture](../../project.md) for missing conventions or an explicitly inherited architecture.
- **Conditional rules:** [R2](../rules/access.md), [R3 read-only](../rules/read-only.md) or [R6 split transactions](../rules/split-transactions.md) only when the respective ownership/effect/commit boundary is involved.
- **Verify:** one representative accepted slice against effective responsibilities and actual calls; a folder/class name is insufficient.
- **Pending:** project-specific layering, module layout and domain conventions; do not impose a parallel framework.

## B3 Data and persistence

- **ID / match:** `dev.backend.persistence`; queries, constraints, field changes, conversions or migration code. Exclude an unrelated database because the service happens to use it.
- **Existing guidance:** [development core](../core.md) and maintained schema/data ownership; use [project.md](../../project.md) only for unresolved conventions.
- **Conditional rules:** [R1](../rules/data-fidelity.md) for conversions, [R3](../rules/read-only.md) for read-only promises, [R5 concurrent edits](../rules/concurrent-edits.md) or [R6](../rules/split-transactions.md) for actual update/transaction boundaries. Executing a migration follows release authority.
- **Verify:** stored state, constraints and relevant rejection/rollback behavior in the appropriate environment; distinguish models/mocks from real database claims.
- **Pending:** ORM, database, schema-change and migration standards supplied by the project.

## B4 Transactions and concurrency

- **ID / match:** `dev.backend.concurrency`; atomicity, isolation, lock order, version guards or uncertain commit results. Exclude an unaffected pure/read-only transformation.
- **Existing guidance:** [development core](../core.md); read [R5](../rules/concurrent-edits.md) for competing updates and [R6](../rules/split-transactions.md) when work and reservation commit separately.
- **Conditional rules:** [R2](../rules/access.md) for mutable authorization at state change; [R4 async/idempotency](../rules/async-idempotency.md) for same-operation retries or unknown outcomes. Preserve each rule's actual trigger and nearby exception.
- **Verify:** relevant ordering, durable results and actual transaction boundaries; distinguish stale-page sequential updates from simultaneous database transactions.
- **Pending:** project transaction annotations, isolation defaults, lock order and database-specific conventions.

## B5 Identity and access

- **ID / match:** `dev.backend.access`; authentication actor, roles, resource ownership, tenant or cross-user access. Exclude frontend presentation-only visibility that does not change access behavior.
- **Existing guidance:** [R2 access](../rules/access.md); use maintained project authorization contracts and [project.md](../../project.md) only for a missing/conflicting owner or rule.
- **Conditional rules:** [R3](../rules/read-only.md) for downstream effects on an inspection path; [R5](../rules/concurrent-edits.md) when changing mutable facts can invalidate a final access decision; [I2](integration.md#i2-identity-and-access-chain) for a service-spanning actor chain.
- **Verify:** authorized and unauthorized actors through the real affected resource path, preserving public ownership boundaries and rejection precedence.
- **Pending:** authentication/authorization libraries, tenant conventions and permission matrices; unknown business policy stays unresolved.

## B6 Asynchronous work and jobs

- **ID / match:** `dev.backend.async-jobs`; state transitions, schedulers, queues, retries, idempotency or recovery. Exclude a synchronous path without stateful/async effects.
- **Existing guidance:** [R4](../rules/async-idempotency.md) and the project's actual workflow/protocol; use [development core](../core.md) for diagnosis and slicing.
- **Conditional rules:** [R6](../rules/split-transactions.md) for separately committed work/reservations; [R5](../rules/concurrent-edits.md) for competing finalization; [I5](integration.md#i5-asynchronous-business-flows) when completion crosses services or clients.
- **Verify:** accepted transitions, duplicate/unknown-outcome recovery and durable effects; configured threads alone do not prove scheduling or throughput.
- **Pending:** queue/job framework, retry, observability and worker conventions; do not invent lifecycle semantics.

## B7 External services and SDKs

- **ID / match:** `dev.backend.external-services`; adapters, requests, callbacks, protocol failures or transport/dependency changes. Exclude an unaffected local transformation.
- **Existing guidance:** [development core](../core.md), maintained external contracts and relevant [verification](../../verification.md) boundary selection.
- **Conditional rules:** [R8](../rules/sdk-transport.md) when dependency replacement affects real transport; [R4](../rules/async-idempotency.md) for callback/retry/unknown results; [R2](../rules/access.md) for credentials/actor access. Read media capability checks only if that combination is actually requested.
- **Verify:** the intended adapter and affected protocol/transport path; distinguish loopback transport, mocks and actual provider acceptance.
- **Pending:** service packages, callback conventions and provider-specific standards; connection success does not prove every capability combination.

## B8 Configuration and runtime code

- **ID / match:** `dev.backend.runtime-code`; configuration binding, feature switches, startup dependencies, logging or health-related code. Exclude applying external production configuration without corresponding authority.
- **Existing guidance:** [development core](../core.md) and relevant maintained project/runtime conventions; [engineering scenarios](engineering.md) only when their build/tool boundary is involved.
- **Conditional rules:** [R3](../rules/read-only.md) for initialization/inspection side effects; [R4](../rules/async-idempotency.md) for retained background work. Actual incident investigation or deployed configuration repair enters the [stage-05 operations branch](../../stages/05-release.md).
- **Verify:** the affected actual startup/runtime combination and retained required paths; a successful isolated unit check does not prove application readiness.
- **Pending:** configuration, feature-switch, logging and health standards for the actual runtime.

## Team additions — pending

No additional team-specific backend standard is supplied here yet. Fill accepted stack/domain details with scope, maintained source/version, an applicable check and a valid exception; shared rules remain single-source references.
