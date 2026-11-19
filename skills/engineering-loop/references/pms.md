# Work with PMS tasks

Read for a supplied task reference, a task-management request, or work subject to the project's tracking policy. First pass [connection.md](connection.md); read-only task lookup can then establish the current stage and scope. Apply the common [route challenge](grill.md) before task mutations or delivery execution; reads alone authorize neither. A simple untracked local edit needs the common gate/challenge, not these task-operation details. Keep private bindings and credentials in the host/project configuration.

Challenge the selected task route: is it an existing deliverable or a duplicate? Are scope, responsible member, execution ownership, dependencies and acceptance evidence clear? Which ownership controls are advisory versus enforced?

## Bind work to an effective task

Creation, assignment, dependency changes and progress/evidence updates are task-management routes. Reading this guide is not authorization or a challenge result.

If a task link/number is supplied, read it in the intended workspace/project, including relevant dependencies and maintained acceptance. For an unlinked formal deliverable, search existing tasks in that project and inspect plausible matches before creating anything. Paginate inventories when claiming completeness; search results or one page do not prove absence. Similar titles alone do not establish the same scope or version.

Create only within existing user authorization and the project's task policy. A request to create a task authorizes the necessary creation; an authorized tracked delivery may use its established creation policy without asking again. Analysis, drafting, connection checks or a hypothetical question do not authorize task creation, assignment or execution. If a formal delivery requires a task but neither an existing match nor creation authority is established, resolve that boundary before delivery execution. Do not turn every conversation, document heading, button or internal agent assignment into a PMS task.

Use the project's title convention and delivery granularity. Capture the intended deliverable, scope/exclusions, acceptance examples, relevant dependencies and artifact destination. Preserve unknown owner/date/effort fields rather than inventing them. Keep authoritative documents/code in their maintained locations and link them. Parent-child means ownership; blocking relations mean prerequisites. Unplanned work and missing dependency links cannot count as completed coverage or an overall progress percentage.

After creation or update, check the returned identity and read back the affected fields in the intended project before reporting success. For a timeout/unknown outcome, reconcile the current task, activity and creation results first. Do not blindly retry a create or append duplicate comments. A local search-before-create convention is not a server-side uniqueness guarantee; strict idempotency needs service support.

## Claim, execute and hand off

Before assignment, resolve the intended responsible workspace member; do not use the connection account merely because `whoami` returned it. Re-read current owner, state and blockers, and respect existing ownership. Claim/transfer only within authorization. Read back the resulting owner/state; distinguish a partial assignment/status update from a fully completed transition.

The current Kaneo interface exposes ordinary assignment and status updates, without an exposed conditional version or atomic claim. Read-then-assign-then-read is not a lock. Use an agreed serialized dispatcher where appropriate; strict multi-client exclusion requires a server-side conditional claim/lease or equivalent enforcement. A conflict stops dependent edits for reconciliation. Do not steal ownership, declare an exclusive claim or treat a timed-out agent as a released lock.

PMS assignee represents delivery responsibility. Agent/chat identity, repository/branch/revision, owned files, runtime handles and next step describe execution and handoff; they do not create fictitious team members or automatically replace the assignee. Keep one effective ownership record and use [collaboration.md](collaboration.md) for delegation and integration. Every changed route still uses [grill.md](grill.md), without reopening settled decisions.

## Write evidence, then advance state

Map work onto the project's actual workflow. For a board with `to-do`, `in-progress`, `in-review`, `done`, submit identifiable artifacts and checks for review before the accepted completion transition. This mapping is an example, not a universal column schema. Record passed, failed and unrun checks, scope/version, blockers, remaining items and the authorized acceptance result. Do not weaken acceptance or treat a commit, task creation or moved card as completion evidence. Human acceptance and release authority remain project decisions.

Read back relevant state after writes. If synchronization fails, retain artifact/evidence identity and the pending update, report that PMS is not synchronized, and stop downstream routed work until the gate is restored. Repair the update after reconciling current state; do not repeat verified implementation or replace another person's newer task changes. Use narrow update tools where possible: a fetch/merge/full update can overwrite concurrent fields. Prompts alone cannot prevent bypasses; enforced transition guards belong in the PMS/host.

## Kaneo operation map

Tool names below describe the available adapter; discover the current schema before using it. Another PMS must prove equivalent capabilities rather than inheriting assumed field names.

| Purpose | Kaneo tools and check |
|---|---|
| Required connection | Follow [connection.md](connection.md) before task operations; reuse its valid identity, project and workflow evidence |
| Task lookup | `search`, `get_task` / `get_task_by_ticket_id`, `list_tasks`; scope to the intended project and follow pagination |
| Creation | `create_task`, then `get_task`; check target, deliverable and requested fields |
| Responsibility | `list_workspace_members`, `update_task_assignee`, then `get_task`; current owner/authorization first |
| Dependencies | `get_task_relations`, `create_task_relation`; keep parent/blocks/related semantics distinct |
| Progress/evidence | `update_task_status`, `create_task_comment`, task reads/comments/activity; reconcile unknown outcomes before retry |
| Field updates | `get_task_custom_field_values`, `set_task_custom_field_value`; use actual required options; avoid broad overwrites |

This map is guidance, not evidence that a particular call succeeded. The host exposes and authorizes tools; secrets remain in its connection configuration. Do not add a direct API/credential fallback to bypass a failed required MCP gate.
