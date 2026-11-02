# Delegated environment mechanism observations — 2026-11-02

## Motivation and scope

The [frontend runtime report](../frontend-target-runtime/RESULTS.md) observed a contributor without the host Playwright module path. The [independent review report](../independent-review-trial/RESULTS.md) recorded dispatch failures caused by a protected virtualenv and a sanitized CLI search path. These earlier runs motivate a narrow handoff clarification; they do not demonstrate the new wording’s effect.

The new [repository controls](../../../tests/test_delegated_environment.py) exercise local subprocesses, not a model. Their reusable task description was written after the first mechanism run; no pre-registration or new behavioral comparison is claimed. The macOS guard control and Node module control are independently skip-aware on unsupported environments. No actual browser, paid service, installation or global configuration change is needed.

## Actual observations

On the local macOS host with Python 3.12.16 and Node 24.22.2, both control tests passed, and an independent reviewer separately executed them successfully.

- The coordinator process read and executed a synthetic protected script. Under the actual guard, the child observed `PermissionError`, and interpreter launch against that script failed with an operating-system denial. The same source in the permitted workspace ran successfully using an accessible interpreter; the protected file remained unreadable before and after. A separate script’s explicit started marker and deliberate runtime exception distinguished code execution failure from environment denial.
- A synthetic Node module resolved in a child with its explicit module search path, failed with `MODULE_NOT_FOUND` without that setting, then resolved after the setting was restored. The test changes only process-local environment variables; it neither installs a module globally nor treats host installation as inherited capability.

These results establish the tested permission and module-resolution distinctions. They do not establish that v0.1.16 changes a fresh agent’s behavior, improves task quality, reduces time, or validates every runtime/CLI/browser combination. The missing-CLI incident remains historical evidence rather than a new CLI-control test. Existing specified-directory protection remains narrower than full filesystem or credential isolation.
