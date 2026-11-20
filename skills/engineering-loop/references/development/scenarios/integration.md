# Integration scenario index

Stage: 03. Area: integration. Select a scenario when an actual producer/consumer, actor, state or environment boundary is involved; touching two folders is insufficient. Read only matched sections and necessary details. The [development core](../core.md), effective project instructions and their mandatory reads remain required.

Resolve each side's actual stack/version and maintained contract independently. Consult [stack bindings](../stacks.md) only for needed specialist guidance. Each matched entry now links an available execution baseline; concrete team protocols remain partial or pending. Selecting integration does not require all frontend/backend indexes or create extra PMS cards.

## I1 Interface alignment

- **ID / match:** `dev.integration.contracts`; fields, nulls, enums, validation or error meanings crossing an actual API boundary. Exclude two independent edits with unchanged shared contracts.
- **Read:** [interface-alignment execution](../integration/contracts.md) for this matched scenario only.
- **Existing guidance:** [development core](../core.md), the maintained API contract and its owning checks; [project.md](../../project.md) only for a missing/conflicting owner or convention.
- **Conditional rules:** [R1 data fidelity](../rules/data-fidelity.md) for representation and [R2 access](../rules/access.md) for actor-dependent behavior; add only affected [B1](backend.md#b1-apis-and-contracts) or client scenario details.
- **Verify:** producer and actual consumer against accepted normal/rejected examples; source/schema validity alone does not prove their runtime combination.
- **Pending:** team API examples, generated-client policy and contract-test commands.

## I2 Identity and access chain

- **ID / match:** `dev.integration.access-chain`; identity/role propagation, owned resources or rejection across services/clients. Exclude an unrelated actor or presentation-only label.
- **Read:** [identity/access-chain execution](../integration/access-chain.md) for this matched scenario only.
- **Existing guidance:** [R2 access](../rules/access.md), including the applicable cross-user/role checks and the actual project authorization contract.
- **Conditional rules:** [R3 read-only](../rules/read-only.md) for inspection chains that might mutate; [R5 concurrent edits](../rules/concurrent-edits.md) if final access depends on mutable facts.
- **Verify:** intended authorized actors and an unauthorized control through the affected downstream path without relaxing its public ownership boundary.
- **Pending:** identity handoff, tenant/role mapping and service credential conventions; the connection actor is not automatically the responsible user.

## I3 Cross-boundary data representation

- **ID / match:** `dev.integration.data-representation`; identifiers, amounts, time values, precision or serialization crossing actual consumers. Exclude an unchanged local value that cannot cross the relevant boundary.
- **Read:** [cross-representation execution](../integration/data-representation.md) for this matched scenario only.
- **Existing guidance:** [R1 data fidelity](../rules/data-fidelity.md) and accepted domain/API examples; project-specific amount/time semantics must come from maintained decisions.
- **Conditional rules:** add the actual display, persistence or SDK scenario only when it participates in the round trip; do not preload whole frontend/backend guides.
- **Verify:** meaningful boundary values through the real affected request, state and storage/consumer path, including relevant null-versus-zero distinctions.
- **Pending:** currency/rounding, timezone, enum and serialization conventions; do not infer business semantics from a data type alone.

## I4 Writes and outcome reconciliation

- **ID / match:** `dev.integration.write-outcomes`; duplicate requests, timeouts with unknown results, version conflicts or checking actual committed state. Exclude a read whose authoritative outcome is already established and unchanged.
- **Read:** [write/outcome reconciliation](../integration/outcome-reconciliation.md) for this matched scenario only.
- **Existing guidance:** [R4 async/idempotency](../rules/async-idempotency.md) and the maintained operation identity/result protocol.
- **Conditional rules:** [R5](../rules/concurrent-edits.md) for competing/stale edits; [R6 split transactions](../rules/split-transactions.md) for separate commits; [R2](../rules/access.md) if ownership affects the write or reconciliation path.
- **Verify:** stored state and operation identity after relevant retry/unknown-result cases; a thrown call does not establish durable absence.
- **Pending:** project idempotency keys, reconciliation endpoints and conflict presentation; preserve accepted user input and authority.

## I5 Asynchronous business flows

- **ID / match:** `dev.integration.async-flow`; acceptance versus completion, polling/callbacks, queues or recovery across components. Exclude an accepted synchronous flow with no asynchronous boundary.
- **Read:** [asynchronous-chain execution](../integration/async-flows.md) for this matched scenario only.
- **Existing guidance:** [R4](../rules/async-idempotency.md) and the accepted completion/return contract; [UI slice](../../ui.md#test-the-uncertain-decision-before-replication) only for affected client feedback.
- **Conditional rules:** [R6](../rules/split-transactions.md) for separately durable steps and [R5](../rules/concurrent-edits.md) for competing state transitions; read only their applicable boundaries.
- **Verify:** observable accepted/completed/failed states and actual durable effects through the supported return path, distinguishing simulated state from service integration.
- **Pending:** callback, status-view, queue and recovery protocols; missing policy does not authorize adding polling or new states.

## I6 File and storage flows

- **ID / match:** `dev.integration.storage`; signed access, file ownership, delegated upload, resume identity or actual storage quota. Exclude an unchanged local preview that never crosses storage/access boundaries.
- **Read:** [file/storage-chain execution](../integration/files.md) for this matched scenario only.
- **Existing guidance:** [R7 uploads](../rules/uploads.md); use the maintained storage and file-identity contracts.
- **Conditional rules:** [R2](../rules/access.md) for cross-user/signed access; [R4](../rules/async-idempotency.md) for retry/result reconciliation; use generated-artifact checks only for actual output-property claims.
- **Verify:** accepted content identity, actual actor access and bytes accepted/retained by storage, including relevant unfinished objects.
- **Pending:** storage adapters, signed URL, upload-session and download contracts; declared size alone is not a quota check.

## I7 State and cache coordination

- **ID / match:** `dev.integration.state-cache`; cross-page/module state, cache refresh, reload recovery or persistence visibility. Exclude a local variable update with no affected consumer/return path.
- **Read:** [state/cache execution](../integration/state-cache.md) for this matched scenario only.
- **Existing guidance:** [verification](../../verification.md) for actual visible outcomes and relevant [rendered behavior](../../ui.md#accept-the-rendered-behavior).
- **Conditional rules:** [R5](../rules/concurrent-edits.md) for stale writes, [R4](../rules/async-idempotency.md) for asynchronous ownership and [R9 rendered UI](../rules/rendered-ui.md) for visible feedback claims.
- **Verify:** the supported return/reload path shows the committed result and retains expected context; an invalidation spy alone is insufficient.
- **Pending:** cache ownership, query keys and cross-module invalidation conventions supplied by the project.

## I8 Environment and dependency connectivity

- **ID / match:** `dev.integration.environment`; actual target identity, addresses/configuration, transport or producer/consumer version compatibility. Exclude deployment execution or global configuration changes without their separate authority.
- **Read:** [environment/connectivity execution](../integration/environment.md) for this matched scenario only.
- **Existing guidance:** maintained project environment/commands, [verification](../../verification.md) and [project.md](../../project.md) only for missing/conflicting conventions.
- **Conditional rules:** [R8 SDK transport](../rules/sdk-transport.md) for changed transitive dependencies. Use [stage 05](../../stages/05-release.md) for release and cutover work and [stage 06](../../stages/06-operations.md) for independent runtime incidents or authorized external runtime repairs.
- **Verify:** the actual artifact/configuration/target and affected real connection; a port, HTTP 200 or mocked client alone does not identify the intended runtime or capability.
- **Pending:** target-environment bindings, local integration setup and version compatibility policy; retain unavailable evidence as a limit.

## Team additions — pending

No additional team-specific integration protocol is supplied here yet. Add maintained contracts, ownership, representative examples, checks and legitimate exceptions without copying every producer/consumer convention into this index.
