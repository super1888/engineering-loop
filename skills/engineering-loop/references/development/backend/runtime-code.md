# B8 Configuration and runtime-code changes

**ID:** `dev.backend.runtime-code` · **Status:** available execution baseline; configuration schema, feature-switch and observability policy remain project bindings.

## Scope and inputs

Use for configuration binding, feature-switch code, startup dependencies, logging or health-related code. Identify the actual runtime entrypoint, maintained config source/schema, affected mode, required dependencies and current checks. Applying deployed configuration or investigating an actual incident follows [stage 05](../../stages/05-release.md).

## Execute

1. Trace precedence and binding from the maintained source to the runtime consumer. Distinguish an absent, invalid and intentionally disabled value according to the actual contract; do not print secrets while diagnosing it.
2. For a switch, inspect registration/initialization as well as execution. Preserve required non-switched callers and shared services instead of disabling an entire component solely to remove one dependency.
3. Select [R3](../rules/read-only.md) for inspection/initialization effects and [R4](../rules/async-idempotency.md) for retained background work. Keep current work identity and required recovery when changing startup behavior.
4. Change logging/health observations to reflect the affected behavior without exposing sensitive values or weakening an existing readiness threshold to make a failing runtime pass.
5. Keep code/configuration-template edits separate from applying external environment changes. Document required configuration transitions and compatibility; production execution requires its established release/operations authority.

## Verify

- Start the actual affected application/artifact in the relevant changed mode, plus the nearby unaffected mode when a shared registration path can regress it. Do not impose every hypothetical configuration combination.
- Check the intended dependency presence/absence, retained required behavior and observed health/output; an isolated bean or unit-test success does not establish application readiness.
- For logging/health changes, verify useful diagnostics and their sensitive-data boundary; record environment limitations rather than replacing real runtime evidence with metadata.

## Deliver and bind

Record config names/sources without secret values, affected modes, actual artifact/runtime identity, observed checks and unapplied environment steps using [delivery evidence](../delivery.md). Bind logging, health, switch and deployment policies to the project; no platform or global convention is introduced here.
