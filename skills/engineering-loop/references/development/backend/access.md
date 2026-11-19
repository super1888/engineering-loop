# B5 Identity and resource access changes

**ID:** `dev.backend.access` · **Status:** available execution baseline; the actual permission matrix and authentication libraries remain project-owned.

## Scope and inputs

Use for authentication actor, role, tenant, resource ownership or shared-user access changes. Identify the requested operation, current actor source, resource boundary and accepted allow/deny examples. Menu visibility or an administrator label alone does not establish a server-side permission.

## Execute

1. Follow the real actor and resource through transport, services and delegated calls using [R2](../rules/access.md); distinguish the connection/service account from the responsible or requesting user.
2. Reuse the maintained server authorization contract at the protected read/write boundary. Keep unresolved permission policy with its authorized owner; do not create a new role or broad allow rule to unblock a feature.
3. Check access before protected effects. When mutable membership or ownership can change before final state transition, select [R5](../rules/concurrent-edits.md) and coordinate the relevant invalidating writers.
4. Trace inspection calls for hidden effects through [R3](../rules/read-only.md) when a read-only promise applies. Preserve existing authorized refresh and audit behavior within its own contract.
5. Preserve intended denial precedence and public resource boundaries. Do not weaken ownership checks merely to make an internal caller or a shared-user workflow succeed; reconcile its legitimate access contract.

## Verify

- Run the intended authorized actor and an unauthorized/cross-resource control through the affected path; include cross-user or cross-role success when the accepted workflow requires it.
- On denial, inspect that protected business state/effects did not change. Permitted security/audit records must follow their own established contract rather than being confused with business writes.
- Check the downstream resource result; a parent-project membership check or middleware spy alone does not prove child-resource access.

## Deliver and bind

Record actor/resource cases, permission source, changed checks and actual state observations using [delivery evidence](../delivery.md). Bind role/tenant mappings, libraries, error behavior and auditing requirements to accepted project policy; no generic matrix is supplied here.
