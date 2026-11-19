# Record the actual development deliverable

Use for a tracked deliverable, handoff or requested implementation/verification document. Reuse the project's existing task/document format; a small local change can retain the necessary facts in its response. This record does not require a new planning folder, document, task per component or extra approval.

## Before execution

Identify the accepted outcome/non-goals, actual task when applicable, owner/dependencies and affected artifact. Link authoritative requirements/design/contracts instead of copying their history. Mark unresolved business choices and which action depends on them; do not invent responsibility, dates, effort or completion policy.

Read [pms.md](../pms.md) for task lookup/creation/claiming or an applicable tracking policy. Reuse a matching task before authorized creation; frontend/backend/integration branches may contribute to one accepted functional deliverable. Separate cards only when the project's ownership, dependency or acceptance policy calls for them.

## Evidence record

Keep the relevant fields in the maintained record, scaling detail to the slice:

```text
Outcome and scope: accepted behavior, exclusions, remaining decisions
Artifact identity: code/document/build revision, affected paths, maintained links
Applicable agreement: requirement/contract/design and relevant project conventions
Execution result: actual changed behavior, supported failure/return paths
Checks: command or method, passed/failed/unrun, scope, environment/configuration
Remaining work: blockers, acceptance owner, pending actions and next slice
Task synchronization: actual task identity, observed state and unsynchronized updates
```

Use the selected execution body's concrete examples to establish its claims. A screenshot proves only its observed target/state; mocks, static checks, real service integration and human acceptance are different evidence levels. Unknown or skipped required checks remain a gap, not an implied pass.

## Return to PMS or handoff

Within existing authorization, link actual artifact/version and evidence to the intended task, state blockers accurately, and use the project's returned workflow states. Read back affected fields after writes. The responsible member, execution agent and reviewer are distinct facts; do not reassign or mark done solely because code was committed or a branch finished.

For an unknown write result, reconcile before retrying; for a failed connection/synchronization retain the artifact and pending update, report the limit and restore the gate before downstream execution. Do not replay completed implementation to repair a task record. Existing project review/commit/release stop points still govern delivery.

## Project-specific bindings still needed

Exact task-title convention, document location/template, owner mapping, required PMS fields, review/acceptance roles and status transitions come from the selected project. This reusable record supplies no private team/project IDs or new workflow schema.
