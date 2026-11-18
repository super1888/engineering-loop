# Connect PMS before routed work

Use for the mandatory connection gate and for reading, creating, claiming or updating team tasks. The entrypoint requires this gate before every selected lifecycle stage or specialist; reuse still-valid evidence rather than repeating it on every tool call. Team configuration identifies the PMS service, workspace/project binding and workflow. A board URL identifies a project, not an MCP endpoint. Do not ship private project IDs, member mappings or credentials in this skill.

## Fail closed on connection and target

Before routed work, establish these facts with actual successful MCP results:

1. **Capability and identity:** the configured PMS tools are present and an authenticated identity read succeeds. Keep the returned actor distinct from the user on whose behalf it acts; a connection account is not automatically the task owner.
2. **Intended target:** resolve the workspace and project from explicit user input or maintained project configuration; read that project and check its returned identity against the intended binding. A remembered previous project is not a default. If the target is ambiguous, ask only the missing target decision.
3. **Workflow:** read the project's actual columns/status values and required field definitions relevant to the next operation. Use actual slugs/options, never guessed labels. Check the existing task and its project when a task reference is supplied.

Retain a compact gate result: actor, target, available required operations, status mapping, successful-read evidence and any limits. Tool registration, a CLI enabled flag, a readable local config, a successful unrelated service call, or a self-written "connected" receipt do not pass the gate. A read proves read access only; it does not establish write permission or atomic claiming. Dependency metadata does not install, authenticate or execute the service.

Missing tools, failed identity, denied/wrong project, unreadable workflow or unavailable required capability leave the gate blocked. Before it passes, permit only the minimal local reads and MCP probes needed to discover the target or diagnose/repair the connection within existing authority. Do not start stage/specialist execution, mutate source or write PMS data, or silently switch to an offline task list. State the failed check and remedy; never expose credentials or change global settings without authorization. Stop requests still take effect immediately.

Evidence is scoped to the current session, credential identity, target and connection. Reuse it while those facts remain valid. Invalidate affected evidence after account/project changes, authentication/transport failures or evidence of access changes; re-establish the gate before further routed work. Preserve completed artifacts and live handles during interruption. Already-produced work must not be replayed just to repair synchronization.

## Bind work to an effective task

The connection section above is read-only preflight. Task creation, assignment, dependency changes and progress/evidence updates below are task-management routes: after the gate passes, complete the relevant [route challenge](grill.md) before their mutations. Reading this guide is not authorization or a challenge result.

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
| Connection gate | `whoami`, `get_project`, `list_project_columns`; use `list_project_custom_fields` for required fields |
| Task lookup | `search`, `get_task` / `get_task_by_ticket_id`, `list_tasks`; scope to the intended project and follow pagination |
| Creation | `create_task`, then `get_task`; check target, deliverable and requested fields |
| Responsibility | `list_workspace_members`, `update_task_assignee`, then `get_task`; current owner/authorization first |
| Dependencies | `get_task_relations`, `create_task_relation`; keep parent/blocks/related semantics distinct |
| Progress/evidence | `update_task_status`, `create_task_comment`, task reads/comments/activity; reconcile unknown outcomes before retry |
| Field updates | `get_task_custom_field_values`, `set_task_custom_field_value`; use actual required options; avoid broad overwrites |

This map is guidance, not evidence that a particular call succeeded. The host exposes and authorizes tools; secrets remain in its connection configuration. Do not add a direct API/credential fallback to bypass a failed required MCP gate.
