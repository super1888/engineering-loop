# I2 Verify identity and access across a chain

**ID:** `dev.integration.access-chain` · **Status:** available execution baseline; project permission policy remains pending.

Use when identity, roles or owned/shared resources cross a service/client boundary. A presentation-only label does not require a new permission matrix. Apply the shared [R2 access rule](../rules/access.md).

## Inputs

Identify each caller, the intended authenticated actor, target resource and owning boundary; name the affected producer/consumer artifact/configuration versions. Obtain accepted allowed/rejected examples and the existing identity/permission contract. Keep test credentials in their established secret channel.

## Execute

1. Trace how the actor is established and propagated at each call. Distinguish the connection account, human assignee, delegated service identity and effective resource actor; do not substitute one for another.
2. Identify where role, tenant or ownership decisions are enforced. A client-supplied identity, hidden button or successful upstream membership check does not establish downstream resource access.
3. Follow each changed read/write to its final protected boundary. If mutable facts can invalidate a later decision, apply [R5](../rules/concurrent-edits.md) without inventing a second protection protocol.
4. Preserve the ordinary authorized/shared-user path while rejecting the relevant unauthorized path. Resolve an unknown business permission with its owner rather than broadening a role to make the test pass.
5. For a promised inspection path, trace delegated effects under [R3](../rules/read-only.md); access investigation does not grant repair or production-write authority.

## Verify

- Exercise an intended authorized actor and a relevant unauthorized actor through the affected downstream resource path, not only the first controller.
- Check the expected rejection and protected persistent effects where relevant; a 401/403/404 alone does not prove that no forbidden action occurred.
- Include an allowed shared-resource control when sharing is accepted. Do not relax the public ownership boundary or expose tokens in logs, screenshots or records.

## Deliver

Keep actor/resource roles, exercised path, artifact/environment identity, allowed/rejected observations and unresolved policy in the existing [delivery record](../delivery.md), using safe references instead of credential values.

## Team bindings — pending

Bind actual identity handoff, service credentials, tenant/role mapping, permission owner and permitted test identities. This baseline does not supply a universal role model.
