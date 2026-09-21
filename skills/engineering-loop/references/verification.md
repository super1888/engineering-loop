# Verify claims at the appropriate boundary

Select checks from the changed behavior and project requirements. Distinguish document/schema validity, static checks, simulated behavior, real integration, and user acceptance. Reuse a broader check only if it actually executes the required path.

Test meaningful cross-boundary values and combinations: large identifiers across languages, null versus zero, accepted versus unknown outcomes, competing credentials, duplicate calls, transaction/cache visibility, and persisted state after refresh when relevant. Do not make every example mandatory for every change.

Derive expected results from confirmed domain examples, an independent calculation or an authoritative contract. For a cross-screen state change, verify the visible outcome on affected return paths; a callback or cache-invalidation spy alone does not establish it. Another agent sharing the same mistaken premise is not an independent oracle. For concurrent contributors, verify the affected combined behavior after integration, not only each contribution in isolation.

For a visual or responsive defect, reproduce the reported viewport or aspect ratio and inspect the rendered result as well as relevant geometry. Use the project's existing browser/design checks; passing overlap or overflow assertions does not establish visual quality. Include a nearby unaffected layout when useful, without imposing a universal viewport matrix or treating a smaller viewport as actual browser zoom. Scope evidence to the rendered asset and animation state.

Use an explicitly configured test environment for real boundaries. Do not treat a mock database, preview page, or synthetic model as proof of real integration. For AI output quality, separate structure from semantics; use independently specified examples and human domain review where needed. Keep evaluation samples/version changes traceable, and retain cases not used for tuning when practical.

When checks fail, classify implementation regression, accepted contract change, fixture weakness, timing/resource instability, or environment/command failure. Preserve the intended assertion. Do not silently update snapshots, remove cases, or broaden tolerances to fit an incorrect result.

For an enumerable migration or replacement, compare the source set with covered/excluded/remaining items. State limits for claims that cannot be enumerated.

Record command, exit/result, scope, relevant revision or dirty-file snapshot, environment/configuration identity, and limitations without secrets. Report passed, failed, and unrun separately. Related changes invalidate related evidence; an old success count does not establish the new behavior.
