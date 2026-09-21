# Verify claims at the appropriate boundary

Select checks from the changed behavior and project requirements. Distinguish document/schema validity, static checks, simulated behavior, real integration, and user acceptance. Reuse a broader check only if it actually executes the required path.

Test meaningful cross-boundary values and combinations: large identifiers across languages, null versus zero, accepted versus unknown outcomes, competing credentials, duplicate calls, transaction/cache visibility, and persisted state after refresh when relevant. Do not make every example mandatory for every change.

Use an explicitly configured test environment for real boundaries. Do not treat a mock database, preview page, or synthetic model as proof of real integration. For AI output quality, separate structure from semantics; use independently specified examples and human domain review where needed. Keep evaluation samples/version changes traceable, and retain cases not used for tuning when practical.

When checks fail, classify implementation regression, accepted contract change, fixture weakness, timing/resource instability, or environment/command failure. Preserve the intended assertion. Do not silently update snapshots, remove cases, or broaden tolerances to fit an incorrect result.

For an enumerable migration or replacement, compare the source set with covered/excluded/remaining items. State limits for claims that cannot be enumerated.

Record command, exit/result, scope, relevant revision or dirty-file snapshot, environment/configuration identity, and limitations without secrets. Report passed, failed, and unrun separately. Related changes invalidate related evidence; an old success count does not establish the new behavior.
