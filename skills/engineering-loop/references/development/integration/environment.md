# I8 Identify and exercise the intended integration target

**ID:** `dev.integration.environment` · **Status:** available execution baseline; target setup and compatibility policy remain pending.

Use for actual target identity, address/configuration, transport or producer/consumer compatibility. Applying a release or cutover follows [stage 05](../../stages/05-release.md). Independent runtime diagnosis or configuration repair follows [stage 06](../../stages/06-operations.md). Check the applicable authorization before applying changes outside the local workspace.

## Inputs

Identify the intended target and its authority, producer/consumer artifact or image versions, relevant configuration identity, required capabilities and owning setup/check commands. Keep credentials in the established channel; a listening port or HTTP 200 alone does not identify the intended project/runtime.

## Execute

1. Establish the actual process/project/artifact and configuration behind the target before judging its behavior. Reconcile stale handoff addresses or versions rather than recreating a runtime merely to match a note.
2. Verify required commands/dependencies from the execution context that will run the check. A coordinator's installed tool or successful parent process does not prove a delegated process has the same environment.
3. Exercise a narrow authorized connection and the affected capability through the actual adapter/protocol. Distinguish name resolution, TLS/authentication, transport, application health and task behavior instead of treating one success as all of them.
4. For replaced SDK dependencies, apply [R8](../rules/sdk-transport.md) on the resulting runtime/classpath. A loopback transport check need not invoke a paid provider, and does not establish provider acceptance.
5. Check each prerequisite command's actual result before dependent actions. If a necessary environment/capability is unavailable, report the exact gap and stop dependent work; continue independent authorized checks where useful.

## Verify

- Retain the actual artifact/configuration/target identity, command or request, observed capability and scope of result without exposing secrets.
- Include a relevant mismatch or failure control where it distinguishes a wrong target, unavailable dependency or incompatible consumer; do not disrupt a shared environment merely to manufacture a negative case.
- Separate simulated clients, real local integration, provider behavior and production evidence. Do not disable protection, change global configuration or install a toolchain solely to obtain a green result.

## Deliver

Link target/artifact/configuration identity, commands/results, observed connection/capability and remaining setup gaps through the existing [delivery record](../delivery.md). Use [project guidance](../../project.md) only for missing/conflicting maintained setup or ownership.

## Team bindings — pending

Bind actual local integration setup, environment references, compatibility policy and owning commands. Keep private endpoints, member bindings and credentials in project/host configuration rather than this shared skill.
