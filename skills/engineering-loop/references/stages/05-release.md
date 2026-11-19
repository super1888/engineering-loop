# 05 Release and verification · 发布与验证

## Enter

Use after the entrypoint's MCP gate for release preparation, authorized deployment/cutover, deployed-version verification or an actual operations/readiness task. An incident may enter its operations branch directly; it does not require replaying project phases or creating a release task.

## Inputs

Identify the target environment, actual authority, relevant artifact/configuration version, applicable acceptance evidence and existing runbook. For an incident, begin with observed impact and current runtime identity. Require only the recovery and prerequisite evidence relevant to the proposed action.

## Execution and focused references

Read [release.md](../release.md) for preparation, publication, migration, cutover or existing-consumer compatibility. Read [operations.md](../operations.md) for an incident, operational readiness, external configuration repair or risk-based restore validation. Read [verification.md](../verification.md) for the applicable evidence boundaries; combine guides only when the task crosses them.

Apply the [common challenge](../grill.md) to the artifact, target, impact and recovery assumption. Investigate available evidence before asking; preserve existing authorization and resolve only missing material decisions. Preparation does not itself authorize deployment, destructive repair or external notifications.

## PMS

Follow [pms.md](../pms.md) when applicable. Bind release or maintenance work to its actual deliverable/event and dependencies; create additional verification tasks only under the project's policy and existing authority. Record observed outcome, blockers and pending synchronization, and read back updates. Deployment or moving a card alone is not completion evidence.

## Deliverables

Keep the relevant release/runbook/verification or incident record in its maintained location, identifying the deployed artifact, action, recovery prerequisites, actual observations and untested boundaries. Link artifacts and versions rather than copying secrets or inventing a new document system.

## Exit and return

Complete the requested preparation or establish the required deployed-path/recovery evidence for executed work. Classify a failure and return only its affected work to [development](03-development.md), [design](02-design.md), [requirements](01-requirements.md) or operations diagnosis. Use [learning.md](../learning.md) for a demonstrated lesson or requested retrospective; do not make it a ceremony on every release. Honor finite completion and ongoing-goal checkpoints.
