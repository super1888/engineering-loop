# Verify claims at the appropriate boundary

**Challenge focus:** Which claim, artifact, configuration and environment does the check cover, and what remains failed, unrun or outside its scope?

Select checks from the changed behavior and project requirements. Distinguish document/schema validity, static checks, simulated behavior, real integration, and user acceptance. Reuse a broader check only if it actually executes the required path.

Match the check to the claim: source tokens can protect an implementation convention, dependency checks can reject forbidden calls, and interaction checks can establish visible behavior. Finding a toast API or responsive CSS in source does not prove correct timing, a single notification or usable layout. Prefer behavior assertions when different valid implementations should remain possible; test rendered interaction where source checks cannot distinguish the reported failure.

Test meaningful cross-boundary values and combinations: large identifiers across languages, null versus zero, accepted versus unknown outcomes, competing credentials, duplicate calls, transaction/cache visibility, and persisted state after refresh when relevant. Do not make every example mandatory for every change.

## Select applicable boundary checks

Before concluding verification, read the matching section below when its trigger applies. The detailed gates remain required within their stated scope; moving them does not waive them. Read only relevant sections, not the entire companion reference. A clear local edit need not load unrelated integration or media examples.

| Changed boundary or claim | Focused checks |
|---|---|
| Reservation and work item commit separately | [Split transactions](verification-boundaries.md#split-transactions) |
| Excluded or replaced an SDK transitive dependency | [SDK transport](verification-boundaries.md#sdk-transport-after-dependency-changes) |
| Delegated direct upload or shared-user workflow | [Storage quota](verification-boundaries.md#direct-upload-storage-quotas), [actor access](verification-boundaries.md#cross-user-and-role-access), as applicable |
| Visual/responsive defect or accessibility scan | [Rendered result](verification-boundaries.md#rendered-visual-and-responsive-defects), [accessibility](verification-boundaries.md#accessibility-scans-and-status-feedback), as applicable |
| Image-plus-schema request or media verdict with missing dimensions | [Capability combination](verification-boundaries.md#image-input-with-structured-output), [evidence limits](verification-boundaries.md#incomplete-media-evidence-and-abstention), as applicable |
| Review fails after producing an artifact | [Blocking policy and retained diagnostics](verification-boundaries.md#failed-review-after-artifact-creation) |
| Generated media/document output properties | [Actual runtime and rendering](verification-boundaries.md#generated-media-and-document-properties) |

For integration tests that run only when external services or environment variables are present, inspect the test report as well as the job result. A green CI step with every intended case skipped proves nothing about that boundary. Make the gate fail on a missing report, fewer than the expected cases, or any skipped, failed, or errored case; keep a matched ordinary unit-test job free of unnecessary external setup.

Derive expected results from confirmed domain examples, an independent calculation or an authoritative contract. For a cross-screen state change, verify the visible outcome on affected return paths; a callback or cache-invalidation spy alone does not establish it. Another agent sharing the same mistaken premise is not an independent oracle. For concurrent contributors, verify the affected combined behavior after integration, not only each contribution in isolation.

For delegated verification, provide the effective agreement and independent examples, not just the developer's claimed result. Establish critical expectations before or alongside implementation where useful. If an accepted contract changes during work, reconcile affected tests and invalidate related old evidence before integration; [collaboration.md](collaboration.md) describes ownership and notification. A test agent must not silently choose a new business rule to resolve the conflict.

Use an explicitly configured test environment for real boundaries. Do not treat a mock database, preview page, or synthetic model as proof of real integration. For AI output quality, separate structure from semantics; use independently specified examples and human domain review where needed. Keep evaluation samples/version changes traceable, and retain cases not used for tuning when practical.

When checks fail, classify implementation regression, accepted contract change, fixture weakness, timing/resource instability, or environment/command failure. Preserve the intended assertion. Do not silently update snapshots, remove cases, or broaden tolerances to fit an incorrect result.

When one shell invocation runs several native commands, a later success can hide an earlier failed prerequisite. Check each required native result before dependent writes or verification launches; stop those dependent steps on an unexpected failure. In PowerShell, inspect `$LASTEXITCODE` immediately; `$ErrorActionPreference = 'Stop'` alone does not establish native-command success. An intentional negative check may continue when its actual result matches the expected failure. If an apply helper failed, confirm the intended artifact exists before running final verification; passing checks against the unapplied baseline do not verify the change.

When implementation conforms but observed use fails the intended task, record the scenario and challenged assumption; return to [requirements.md](requirements.md) for a bounded design correction. Separate implementation defects, newly discovered constraints and changed preferences. Green checks do not settle usefulness, and dissatisfaction alone does not authorize unrelated redesign or invalidating unchanged acceptance.

For an enumerable migration or replacement, compare the source set with covered/excluded/remaining items. State limits for claims that cannot be enumerated.

Record command, exit/result, scope, relevant revision or dirty-file snapshot, environment/configuration identity, and limitations without secrets. Report passed, failed, and unrun separately. Related changes invalidate related evidence; an old success count does not establish the new behavior.
