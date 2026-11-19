# Frontend scenario index

Stage: 03. Area: frontend. Routing entries and linked execution baselines below are available; framework, component and team-specific bindings remain partial or pending. Read the matching entry and its selected body, not every linked baseline. The [development core](../core.md), effective project instructions and their required full reads still apply.

Identify the affected module's framework, component library and versions from maintained configuration and representative code. Use [stack bindings](../stacks.md) only when specialist stack guidance is needed; this index does not supply React/Vue conventions. A request for UI design only belongs to [stage 02](../../stages/02-design.md). “Admin/backend page” is not a backend-code trigger.

## F1 Components and styles

- **ID / match:** `dev.frontend.components`; component copy, tokens, themes, variants, button states, icons or spacing in an existing authorized interface slice. Exclude backend-only work and an unrelated redesign.
- **Read:** [Component/copy/style execution](../frontend/components.md); use [template matching](../templates.md) only when component/style reuse is needed.
- **Conditional rules:** [R9 rendered UI](../rules/rendered-ui.md) for visual/interaction claims; [R2 access](../rules/access.md) only if action availability or resource permission changes.
- **Verify:** use scoped consistency checks for a settled copy-only edit and preserve the existing action. Render the affected target/state when the claim concerns appearance or interaction; source tokens alone do not prove those claims.
- **Pending:** team tokens, approved component variants, button-template IDs, parameters and examples are not yet cataloged; add them under the pending additions section.

## F2 Forms and editing

- **ID / match:** `dev.frontend.forms`; field validation, drafts, submit/cancel behavior or retaining input after failure. Exclude a copy-only change with unchanged editing behavior.
- **Read:** [Form/editing execution](../frontend/forms.md), retaining the applicable UI and shared-boundary sources it selects.
- **Conditional rules:** [R4 async/idempotency](../rules/async-idempotency.md) for duplicate submission or unknown completion; [R5 concurrent edits](../rules/concurrent-edits.md) for stale-page saves; follow the actual server boundary through [I4](integration.md#i4-writes-and-outcome-reconciliation) when involved.
- **Verify:** accepted, rejected and relevant failure/return paths, including retained input and the accepted completion signal.
- **Pending:** field components, validation presentation and form-library conventions; preserve the project's maintained patterns meanwhile.

## F3 Lists and tables

- **ID / match:** `dev.frontend.collections`; filtering, pagination, sorting, selection, batch actions or empty results. Exclude an unrelated table merely because the project contains one.
- **Read:** [List/table execution](../frontend/collections.md) for query, row-action and returned-result behavior.
- **Conditional rules:** [R1 data fidelity](../rules/data-fidelity.md) when identifiers/quantities cross a representation boundary; [R2 access](../rules/access.md) for scoped rows/actions; [R4](../rules/async-idempotency.md) for stateful batch submissions.
- **Verify:** the affected query/action result and supported return context with realistic long, missing and empty values.
- **Pending:** table packages, query-state conventions, selection semantics and batch-action presentation; business semantics require accepted examples.

## F4 Routing and navigation

- **ID / match:** `dev.frontend.navigation`; route parameters, return paths, context retention or page access. Exclude styling changes that preserve navigation.
- **Read:** [Navigation execution](../frontend/navigation.md) for route identity, state ownership and supported return paths.
- **Conditional rules:** [R1](../rules/data-fidelity.md) for encoded identifiers and serialization; [R2](../rules/access.md) when route access depends on an actor/resource; use [I7](integration.md#i7-state-and-cache-coordination) only for an actual cross-page state boundary.
- **Verify:** entry, action, completion and supported back/return paths retain the agreed context and permissions.
- **Pending:** project router, URL/query ownership and navigation-component conventions.

## F5 State and asynchronous UI

- **ID / match:** `dev.frontend.async-state`; loading/errors, duplicate actions, late responses, cache refresh or asynchronous feedback. Exclude a synchronous local edit with no such boundary.
- **Read:** [Asynchronous UI execution](../frontend/async-state.md) for operation ownership, response order and visible completion.
- **Conditional rules:** [R4](../rules/async-idempotency.md) for operation ownership/retry; [R5](../rules/concurrent-edits.md) for competing persisted edits; [R9](../rules/rendered-ui.md) for feedback/focus claims. Add [I5](integration.md#i5-asynchronous-business-flows) only when the accepted business completion protocol is involved.
- **Verify:** relevant transition order and visible final/return state; a callback or cache-invalidation spy is insufficient for a visible-result claim.
- **Pending:** state/query libraries, cancellation conventions and notification components; do not invent polling or recovery policy.

## F6 Files and media

- **ID / match:** `dev.frontend.files`; upload, preview, progress, cancel, resume or download. Exclude a metadata-only change unrelated to file behavior.
- **Read:** [File/media execution](../frontend/files.md), selecting storage/access or generated-output checks only for the affected claim.
- **Conditional rules:** [R7 uploads](../rules/uploads.md) for file identity, direct storage, resume or quota; [R2](../rules/access.md) for signed/owned resources; [I6](integration.md#i6-file-and-storage-flows) for the actual storage/service chain.
- **Verify:** accepted file identity, the affected success/failure/recovery path and observable output; distinguish preview from stored or generated-artifact validity.
- **Pending:** upload widgets, media presentation and download conventions, without broadening accepted capabilities.

## F7 Accessibility and target devices

- **ID / match:** `dev.frontend.accessibility-targets`; keyboard/focus, control names, status feedback, zoom, long content or overflow on the affected target. Exclude automatic expansion to unrequested devices.
- **Read:** [Accessibility/target execution](../frontend/accessibility-targets.md), retaining the target-device and evidence gates.
- **Conditional rules:** [R9](../rules/rendered-ui.md), with its relevant visual/accessibility checks. Preserve existing mobile behavior and explicit target requirements.
- **Verify:** the actual target, representative state, rendered role/name and relevant keyboard/status behavior; report inaccessible/unrun evidence honestly.
- **Pending:** supported-browser/device policy and project accessibility thresholds; the desktop default is not permission to remove existing behavior.

## F8 Frontend engineering

- **ID / match:** `dev.frontend.engineering`; frontend build, resource paths, dependency changes, runtime compatibility or performance diagnosis. Exclude deployment execution, which follows stage 05 authority.
- **Read:** [Frontend-engineering execution](../frontend/engineering.md); add an affected [engineering scenario](engineering.md) only for a real shared tooling/build boundary.
- **Conditional rules:** [R8 SDK transport](../rules/sdk-transport.md) only for an affected SDK dependency/transport boundary; [R9](../rules/rendered-ui.md) when the claim concerns the running interface; identify release compatibility work through stage 05 when applicable.
- **Verify:** the actual affected build/runtime path and a discriminating performance/compatibility observation, not package metadata alone.
- **Pending:** bundler, resource, performance-budget and browser-support standards supplied by the project.

## Team additions — pending

No additional team-specific frontend standard is supplied here yet. Add accepted details with applicability, source/version, a check and a legitimate nearby exception; keep general routing and shared risks in their existing homes.
