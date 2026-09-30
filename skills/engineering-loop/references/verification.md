# Verify claims at the appropriate boundary

Select checks from the changed behavior and project requirements. Distinguish document/schema validity, static checks, simulated behavior, real integration, and user acceptance. Reuse a broader check only if it actually executes the required path.

Match the check to the claim: source tokens can protect an implementation convention, dependency checks can reject forbidden calls, and interaction checks can establish visible behavior. Finding a toast API or responsive CSS in source does not prove correct timing, a single notification or usable layout. Prefer behavior assertions when different valid implementations should remain possible; test rendered interaction where source checks cannot distinguish the reported failure.

Test meaningful cross-boundary values and combinations: large identifiers across languages, null versus zero, accepted versus unknown outcomes, competing credentials, duplicate calls, transaction/cache visibility, and persisted state after refresh when relevant. Do not make every example mandatory for every change.

For a reservation committed separately from a work item, use the real database isolation level and independent connections to check commit-unknown exceptions, same-key contenders, and rollback/retry orderings. Inspect the resulting reservation, work item, and publication record together; mock-only tests cannot establish whether a release is safe or an orphan is eventually settled. A single atomic transaction with a confirmed rollback does not need this split-transaction gate.

For integration tests that run only when external services or environment variables are present, inspect the test report as well as the job result. A green CI step with every intended case skipped proves nothing about that boundary. Make the gate fail on a missing report, fewer than the expected cases, or any skipped, failed, or errored case; keep a matched ordinary unit-test job free of unnecessary external setup.

When excluding or replacing an SDK's transitive dependency, exercise the real SDK through the affected request path with the resulting classpath. Request serialization and mocked clients can pass while an interceptor fails before transport. A small loopback server can verify local transport without a paid provider call; keep the security constraint intact and distinguish this check from provider acceptance. An unaffected pure serialization change does not require a transport probe.

When a delegated upload writes directly to object storage, verify quota against bytes the storage accepts, including unfinished objects. Declared size and a per-request proxy limit do not by themselves bound retained storage usage.

For a workflow shared by several users or roles, follow the actual actor through downstream services. A project-level membership check does not prove that an owned task or resource can be read by another authorized member; verify the cross-user path and an unauthorized control without relaxing the public ownership boundary.

Derive expected results from confirmed domain examples, an independent calculation or an authoritative contract. For a cross-screen state change, verify the visible outcome on affected return paths; a callback or cache-invalidation spy alone does not establish it. Another agent sharing the same mistaken premise is not an independent oracle. For concurrent contributors, verify the affected combined behavior after integration, not only each contribution in isolation.

For delegated verification, provide the effective agreement and independent examples, not just the developer's claimed result. Establish critical expectations before or alongside implementation where useful. If an accepted contract changes during work, reconcile affected tests and invalidate related old evidence before integration; [collaboration.md](collaboration.md) describes ownership and notification. A test agent must not silently choose a new business rule to resolve the conflict.

For a visual or responsive defect, reproduce the reported viewport or aspect ratio and inspect the rendered result as well as relevant geometry. Use the project's existing browser/design checks; passing overlap or overflow assertions does not establish visual quality. Include a nearby unaffected layout when useful, without imposing a universal viewport matrix or treating a smaller viewport as actual browser zoom. Scope evidence to the rendered asset and animation state.

For accessibility scans, distinguish definite violations, incomplete checks, and manual findings. Inspect incomplete results at the affected element before claiming the scanned scope passed; uncertain contrast over an image does not by itself justify a color change. Check the rendered role and accessible name of labeled wrappers, including UI library components: an `aria-label` attribute on a generic container does not establish a named group. Where the name matters, assert the intended role and name rather than the attribute alone. For changing status messages, also inspect live-region text and `aria-busy` timing; a role/name assertion alone does not prove a screen reader announced the update.

Use an explicitly configured test environment for real boundaries. Do not treat a mock database, preview page, or synthetic model as proof of real integration. For AI output quality, separate structure from semantics; use independently specified examples and human domain review where needed. Keep evaluation samples/version changes traceable, and retain cases not used for tuning when practical.

When a business invocation combines image input with strict JSON Schema output, provider/model capability flags and a successful text-only connection test do not prove that combination works. Before activating that usage, exercise the intended adapter's actual image-plus-schema request with representative samples; check provider acceptance, parsed structure and task-relevant semantics. A text-only usage needs verification of its own text contract, not a multimodal probe.

When checks fail, classify implementation regression, accepted contract change, fixture weakness, timing/resource instability, or environment/command failure. Preserve the intended assertion. Do not silently update snapshots, remove cases, or broaden tolerances to fit an incorrect result.

When implementation conforms but observed use fails the intended task, record the scenario and challenged assumption; return to [requirements.md](requirements.md) for a bounded design correction. Separate implementation defects, newly discovered constraints and changed preferences. Green checks do not settle usefulness, and dissatisfaction alone does not authorize unrelated redesign or invalidating unchanged acceptance.

For an enumerable migration or replacement, compare the source set with covered/excluded/remaining items. State limits for claims that cannot be enumerated.

Record command, exit/result, scope, relevant revision or dirty-file snapshot, environment/configuration identity, and limitations without secrets. Report passed, failed, and unrun separately. Related changes invalidate related evidence; an old success count does not establish the new behavior.
