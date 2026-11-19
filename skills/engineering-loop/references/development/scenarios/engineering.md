# Engineering and shared-capability scenario index

Stage: 03. Area: engineering/shared capability. Use actual library, CLI, build or generation work rather than forcing every repository into frontend/backend categories. Read matching sections and their execution bodies only. The [development core](../core.md) and all effective project instructions remain required; execution baselines are available and specialized team standards stay project-bound.

Identify language, tools, versions and consumers from the affected module's configuration and representative implementation. [Stack bindings](../stacks.md) are conditional; no new tool installation or framework follows from selecting a scenario. Source/configuration implementation stays distinct from publication or applying external operational changes.

## E1 Shared libraries and SDKs

- **ID / match:** `dev.engineering.libraries`; public APIs, compatibility, examples or actual consumers of a shared library/SDK. Exclude an internal helper with no changed public/consumer boundary.
- **Read:** [library/SDK execution](../engineering/libraries.md), with the [development core](../core.md) and maintained library contracts; use [project.md](../../project.md) only for missing/conflicting ownership or conventions.
- **Conditional rules:** [R1 data fidelity](../rules/data-fidelity.md) for serialization/representation and [R8 SDK transport](../rules/sdk-transport.md) for transport-affecting dependencies; follow release guidance only for authorized publication/consumer cutover work.
- **Verify:** the changed API through representative consumers and examples, distinguishing compatible source/build checks from runtime compatibility claims.
- **Pending:** language-specific public API, compatibility and example standards; implementation does not authorize publishing a package.

## E2 Scripts and CLI

- **ID / match:** `dev.engineering.cli`; command parameters, input/output, exit status or execution-environment behavior. Exclude changing global host configuration merely to make a command run.
- **Read:** [script/CLI execution](../engineering/cli.md) and the project's actual command/runtime contract; [verification](../../verification.md) governs native prerequisite results and evidence.
- **Conditional rules:** [R3 read-only](../rules/read-only.md) for inspection promises; [R4 async/idempotency](../rules/async-idempotency.md) for retried effects; [R1](../rules/data-fidelity.md) when serialization changes values.
- **Verify:** native terminal results and relevant valid/invalid inputs from the actual working environment; later command success cannot erase a failed prerequisite.
- **Pending:** supported shells, output/error format, encoding and platform conventions; no universal shell or new CLI is imposed.

## E3 Build and dependencies

- **ID / match:** `dev.engineering.build`; build configuration, lockfiles, transitive dependencies or generated artifacts. Exclude running an unrelated build or treating release authority as implied.
- **Read:** [build/dependency execution](../engineering/build.md), maintained dependency policies and owning build checks; use [project.md](../../project.md) for unresolved enforcement/commands.
- **Conditional rules:** [R8](../rules/sdk-transport.md) for SDK dependency exclusions/replacement; affected runtime/media rules only when the changed build could invalidate that specific claim.
- **Verify:** the resulting artifact/dependency path and required native results; successful compilation is insufficient when the changed boundary is actual transport or runtime behavior.
- **Pending:** build-system, lockfile, dependency approval and artifact conventions for the actual repository.

## E4 Tooling and generated code

- **ID / match:** `dev.engineering.codegen`; generators, generated-source inventories, reproducible generation or generated contract consistency. Exclude manual edits to unrelated generated files or adding scaffolding without a current need.
- **Read:** [generation/tooling execution](../engineering/codegen.md) and the maintained source/command; use its existing contract check rather than inventing a parallel manifest.
- **Conditional rules:** [R1](../rules/data-fidelity.md) for generated types/serialization; [R2 access](../rules/access.md) or [R8](../rules/sdk-transport.md) only when generation changes those actual boundaries.
- **Verify:** regenerate from the authoritative source and reconcile the expected output inventory, owning checks and applicable consumers; a tidy file list alone is not coverage.
- **Pending:** generator versions, regeneration policy and generated-file ownership; keep source authority and legitimate manual exceptions explicit.

## Team additions — pending

No additional team-specific engineering standard is supplied here yet. Add the actual tool/version, source, trigger, verification and valid exception; do not populate unrelated languages or toolchains by default.
