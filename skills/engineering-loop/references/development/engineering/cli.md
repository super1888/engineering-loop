# E2 Scripts and command-line behavior

**ID:** `dev.engineering.cli` · Execution baseline available; project runtime/CLI policy remains bound locally.

## Scope and inputs

Use for an accepted CLI argument, input/output, exit-status or script behavior change. Identify the actual interpreter/version, working directory, environment prerequisites, caller and existing stdout/stderr/encoding contract. A documentation-only command example needs consistency checks, not an unrelated runtime matrix.

## Execute

1. Reproduce the invocation from its intended directory with representative input. Distinguish missing runtime/configuration from application failure before changing behavior.
2. Validate arguments and input at the existing boundary before dependent side effects. Preserve intended noninteractive use, help/error behavior and accepted stdin/file conventions.
3. Preserve the contract for data output versus diagnostics; do not silently change a machine-readable consumer to prose or expose credentials through logs/arguments.
4. Check required native subprocess results before launching dependent work. A later successful command or shell setting does not establish that a failed prerequisite passed; preserve an intentional negative result when it matches the test contract.
5. For process creation, retain the owned handle and defined cancellation/termination behavior. Do not invent retry delays, daemonization or background scheduling to hide a failure.

## Verify and deliver

Exercise the affected normal invocation and a relevant invalid-input/prerequisite failure, checking exit status, observable output and unintended writes. Verify quoting/Unicode or a second platform only when the changed contract includes that boundary. A string assertion about a command is not proof it ran successfully.

Record actual invocation/runtime, result and side-effect scope through the [delivery record](../delivery.md). State unsupported or unrun environments without claiming cross-platform certification.

## Project bindings

Bind supported runtimes, argument/parser conventions, output schema, encoding, native command policy and command-level checks. Reuse established tools; no shell/parser library is selected by this baseline.
