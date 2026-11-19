# F2 Forms and editing

**ID:** `dev.frontend.forms` · **Status:** available execution baseline; team form conventions remain pending.

## Scope and inputs

Use when field validation, editing, submit/cancel or failure recovery changes. Establish the accepted field meanings, initial/saved values, validation owner, save result and supported return path. A local copy edit with unchanged editing behavior does not need a new form workflow.

Apply the relevant [UI task guidance](../../ui.md#start-with-a-task-and-representative-content); use a representative [interactive slice](../../ui.md#test-the-uncertain-decision-before-replication) when an interaction decision remains consequentially uncertain.

## Execute

1. Trace values from initial data through editable state, payload construction and saved response. Preserve contract distinctions such as absent, empty, zero and null; a display default must not silently overwrite a saved value.
2. Match client feedback to the maintained validation contract. Client checks improve interaction but do not replace server validation or permission checks; resolve consequential disagreement rather than inventing a field rule.
3. Identify draft, submitting, accepted and completed states only where the flow distinguishes them. Make feedback correspond to the actual result; an accepted request is not proof that asynchronous work finished.
4. Retain editable input after a relevant validation, transport or version-conflict failure. Use the established cancel/exit behavior; do not introduce autosave, unsaved-change dialogs or cancellation policy without a current requirement.
5. Follow [R4](../rules/async-idempotency.md) for duplicate/unknown submission outcomes and [R5](../rules/concurrent-edits.md) for stale editing bases. Inspect the actual API boundary when the repair needs it, preserving successful ordinary saves.

## Verify

- Use an accepted normal example and an applicable rejection/failure example to compare input, payload and visible result independently.
- Follow the affected success/return path and check the saved value rather than a submit callback alone. Verify retained input on the failure path being repaired.
- If conflicts or repeated submissions are in scope, check their actual ordering and durable outcome; do not turn every form change into a concurrency matrix.

## Deliver

Record affected fields and value meanings, changed validation/save boundary, relevant normal/failure results and remaining limits through [delivery records](../delivery.md). Link the maintained contract rather than duplicating its business rules.

## Team binding — pending

Form library, field components, validation presentation, draft ownership and error-message conventions remain bound to the actual project. No new library, persistence model or mandatory document format is supplied here.
