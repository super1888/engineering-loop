# 06 Continuous operations · 持续运维

## Enter

Use after the entrypoint's MCP gate for operating or maintaining an existing service, diagnosing an operational event, establishing readiness, applying an authorized independent runtime configuration repair or verifying recovery. Enter directly for an actual operating task. For an identified release's cutover, deployed-version validation or release-specific rollback, use [release and verification](05-release.md).

## Inputs

Establish the actual service and environment, observed impact or maintenance outcome, relevant version and configuration, available operational evidence, maintained runbook and action authority. For recovery, confirm the applicable prerequisites and expected business outcome.

## Execution and focused references

Read [operations.md](../operations.md) for incident diagnosis, maintenance, readiness, configuration and recovery. Read the applicable [verification.md](../verification.md) guidance for evidence of the affected service and business path. Use the least invasive check that can distinguish the leading hypotheses and preserve the requested read or action scope.

Apply the [common challenge](../grill.md) to the runtime identity, impact, leading hypothesis and evidence needed for a recovery claim. Resolve only material unknowns. Confirm authority before repairs, external configuration changes, restores or notifications.

## PMS

Follow [pms.md](../pms.md) when a task reference, operation or tracking policy applies. Bind authorized work to the relevant event or maintenance deliverable. Record actual impact, findings, recovery evidence, blockers and any pending synchronization. Read back authorized updates.

## Deliverables

Use the existing incident, maintenance or readiness record. Identify the runtime and configuration, observed impact, checked hypotheses, actions taken, business-path evidence and outstanding limits. Capture the next action and owner when work remains. Keep secrets in their established channel.

## Exit and return

For an investigation, report the supported conclusion and remaining uncertainty. For an executed recovery, verify the affected service and business path. Route a scoped code repair to [development](03-development.md), release work to [stage 05](05-release.md), and a newly discovered business need to [requirements](01-requirements.md) when authorized. Apply [learning.md](../learning.md) for a demonstrated lesson or requested retrospective.
