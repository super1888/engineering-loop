# 05 Release and verification · 发布与验证

## Enter

Use after the entrypoint's MCP gate for release preparation, authorized deployment or cutover, verification of an identified release in its target environment, or recovery governed by that release. Use [continuous operations](06-operations.md) for an independent incident or maintenance request.

## Inputs

Identify the target environment, actual authority, relevant artifact and configuration versions, applicable acceptance evidence and existing runbook. Check the prerequisites, recovery evidence and observation window relevant to the proposed release work.

## Execution and focused references

Read [release.md](../release.md) for preparation, publication, migration, cutover and existing-consumer compatibility. Use [verification.md](../verification.md) for the applicable evidence boundaries and the relevant [operations.md](../operations.md) guidance when the release depends on operational readiness, restore evidence or a handoff.

Apply the [common challenge](../grill.md) to the artifact, target, impact and recovery assumption. Investigate available evidence before asking; preserve existing authorization and resolve only missing material decisions. Preparation does not itself authorize deployment, destructive repair or external notifications.

## PMS

Follow [pms.md](../pms.md) when applicable. Bind release work to the actual deliverable and dependencies. Create additional verification tasks only under the project's policy and existing authority. For authorized updates, record the observed outcome, blockers and pending synchronization, then read back the changed fields.

## Deliverables

Keep the release plan or actual release and verification record in its maintained location. Identify the target, artifact, action, recovery prerequisites, actual observations and untested boundaries. Record the handoff and owner when the release calls for one.

When a new structured record is needed and the project has no applicable format, adapt the [release, deployment and verification record](../../templates/release-record.md).

## Exit and return

Complete the requested preparation or establish the required deployed-path and recovery evidence for executed work. For a failure, follow the release's authorized recovery path or return the affected work to [development](03-development.md), [design](02-design.md) or [requirements](01-requirements.md). Route ongoing work after handoff and independent runtime incidents to [continuous operations](06-operations.md) when applicable. Use [learning.md](../learning.md) for a demonstrated lesson or requested retrospective.
