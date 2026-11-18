# Behavioral evaluation protocol

Start with [current evidence status](STATUS.md). Use this page to select a method or report; read only the relevant section of [detailed protocols and retained history](DETAILS.md). The detailed record preserves prior conclusions, including unrun scenarios and evaluator-only corrections. Packaging checks do not demonstrate model quality, and a model sample does not establish general skill benefit.

## Run and report an evaluation

1. Freeze the accepted behavior, task, counterexample, input revision/hashes and scoring criteria before execution. Use a fresh disposable workspace and context; preserve original tests and keep evaluator answers outside the implementation input.
2. For a comparison, hold task, model/configuration and environment constant where possible. Record differences and unknowns. Separate ordinary valid alternatives from actual failures; do not change acceptance simply to obtain a pass.
3. Inspect actual artifacts, commands, reports and relevant runtime behavior. Distinguish mechanism controls, model decisions, simulated behavior, real integration and user acceptance. A green process or skipped suite alone does not prove the intended boundary ran.
4. Keep raw prompts, outputs, configuration and trial artifacts in ignored `results/` or another local location. Commit concise conditions, actual outcomes, limitations and reusable tasks. Do not include credentials or private project data.
5. Record passed, failed, unrun and uncertain evidence separately. Disclose seeded errors, known repairs, non-blind scoring, missing measurements and limited samples; do not infer causal advantage, speed or transfer without matching evidence.

The full methods below retain their own prerequisites and safety limits. Procedural separation is not a read sandbox. [Specified-directory read protection](#specified-directory-read-guard-macos) is optional and narrower than full filesystem, network or credential isolation.

## Choose evidence by need

| Need | Entry |
|---|---|
| Same-chat questions and explicit stops | [Task and criteria](fixtures/same-chat-continuation/TASK.md), [actual failure and control](fixtures/same-chat-continuation/RESULTS.md) |
| Native project-local skill discovery | [Frozen installation tasks](fixtures/native-discovery/TASK.md), [observed reads and limits](fixtures/native-discovery/RESULTS.md) |
| What has actually been demonstrated? | [Current status and limits](STATUS.md) |
| Which verification boundary applies? | [Core guide](../skills/engineering-loop/references/verification.md), [fresh routing observations](fixtures/verification-routing/RESULTS.md) |
| Scenario inventory, including unrun cases | [Case specifications](cases.json), [retained details](DETAILS.md) |
| Receipt, copy-only or integration task | Method sections below |
| Existing pages across a local frontend release | [Fixture and task](fixtures/release-existing-clients/TASK.md), [actual browser observations](fixtures/release-existing-clients/RESULTS.md) |
| Recent product/UI, review or operations samples | [Current status](STATUS.md), report sections below |
| Native helper behavior | [Maintenance corrections](TOOLING.md), repository tests and the relevant detailed section; not a model-efficacy claim |
| Contributor environment differs from the coordinator | [Reproduction controls](fixtures/delegated-environment/TASK.md), [observations and limits](fixtures/delegated-environment/RESULTS.md), [fresh handoff consumers](fixtures/delegated-environment-transfer/RESULTS.md) |
| Mandatory PMS/MCP connection and challenged skill routing | [Unexecuted v0.1.22 matrix](fixtures/pms-grill-routing/TASK.md); gate, task-write reconciliation and bounded questioning controls |
| Common-core split: connected versus missing MCP | [Controlled native local-copy task](fixtures/core-route/TASK.md); inspect real mock calls, reference reads and exact file changes separately from protocol tests |

## Retained method and report links

The headings below preserve existing inbound anchors. Each link identifies its corresponding detailed section; read that section as needed. The original content and relative links remain in `DETAILS.md`.

## Pilot golden set, blind review and gate

[Protocol, observations and limitations](DETAILS.md#pilot-golden-set-blind-review-and-gate).

## Unreleased native-command gating revision

[Protocol, observations and limitations](DETAILS.md#unreleased-native-command-gating-revision).

## Reproducible receipt trial

[Protocol, observations and limitations](DETAILS.md#reproducible-receipt-trial).

## Lightweight counterexample

[Protocol, observations and limitations](DETAILS.md#lightweight-counterexample).

## Remaining coverage

[Protocol, observations and limitations](DETAILS.md#remaining-coverage).

## List-detail A/B trial

[Protocol, observations and limitations](DETAILS.md#list-detail-ab-trial).

## Unreleased flow, visual and learning revision

[Protocol, observations and limitations](DETAILS.md#unreleased-flow-visual-and-learning-revision).

## Unreleased reference inheritance and effective guidance revision

[Protocol, observations and limitations](DETAILS.md#unreleased-reference-inheritance-and-effective-guidance-revision).

## Unreleased collaboration revision

[Protocol, observations and limitations](DETAILS.md#unreleased-collaboration-revision).

### Ongoing-goal checkpoint exercise (2026-10-02)

[Protocol, observations and limitations](DETAILS.md#ongoing-goal-checkpoint-exercise-2026-10-02).

### Limited live checkpoint observation (2026-10-02)

[Protocol, observations and limitations](DETAILS.md#limited-live-checkpoint-observation-2026-10-02).

## Asynchronous import and live owner-change A/B trial

[Protocol, observations and limitations](DETAILS.md#asynchronous-import-and-live-owner-change-ab-trial).

## Specialist routing and project-convention trial

[Protocol, observations and limitations](DETAILS.md#specialist-routing-and-project-convention-trial).

## Unreleased mandatory PMS gate and challenged routing revision

The v0.1.22 [scenario matrix](fixtures/pms-grill-routing/TASK.md) adds three aggregated cases in [the inventory](cases.json): live MCP identity/project/state gating, authorized task writes with uncertain-result reconciliation, and assumption/boundary/acceptance challenges before every lifecycle or specialist route. Missing tools, failed authentication, denied targets, configuration-only evidence and disconnects block downstream work. Neighboring controls cover reusable current evidence, authorized deduplicated creation, non-atomic claims, analysis-only work and an already-settled edit with zero unnecessary questions but the same mandatory gate.

These are **unexecuted model scenarios**, not live-PMS acceptance or executable gate enforcement. The matrix separates synthetic checkpoint decisions from a future tool-backed trial and requires observable operation order, identities, artifacts and claims rather than text-pattern grading alone. Historical specialist-discovery and lightweight-task samples retain their original versions and limits; they do not validate the new gate. Reusing those tasks against this revision requires a successful controlled MCP baseline or explicitly grading a blocked-gate condition, not silently skipping the prerequisite. No real service writes or general routing/questioning benefit have been established by this addition.

## Common-core controlled local-copy trial

The [frozen task](fixtures/core-route/TASK.md) compares the same approved local button-label edit with synthetic Kaneo reads versus no configured PMS. `core_route_trial.py` prepares equal complete skill/task copies outside the repository, freezes hashes and runs the native CLI with an explicitly tested native tool profile. Preflight controls prove specified reads and external writes denied and workspace operations allowed. The stdlib mock advertises only identity, project and workflow reads; attempted mutations are logged and refused. Credentials remain in the existing private authentication channel, not prompts or committed reports. Tool profiles do not isolate the entire host/catalog/network.

Protocol failure/mutation/input-drift controls in `tests/test_core_route_trial.py` do not establish model conformance. Actual completed command output, ordered mock calls, native preflight records and before/after files must establish the sample result; a path mention or a final "blocked" response cannot erase a forbidden action. Read witnesses require unchanged frozen reference hashes. Record host initialization and unobserved reads as limitations. A small local edit may omit task/specialist details, but never its required MCP gate or common challenge.

[Retained actual observations](fixtures/core-route/RESULTS.md) include all initial harness/approval/shell limitations and the final native-profile pair. The configured-PMS condition completed the exact edit after real reads; the unconfigured-PMS condition refused downstream work without file changes. Host metadata discovery was still available. These two results do not promote the historical matrix or establish general reliability.

## First-round product hypothesis and UI advice comparison (2026-11-02)

[Protocol, observations and limitations](DETAILS.md#first-round-product-hypothesis-and-ui-advice-comparison-2026-11-02).

## Product/UI follow-up and desktop target gate (2026-11-02)

[Protocol, observations and limitations](DETAILS.md#productui-follow-up-and-desktop-target-gate-2026-11-02).

## Desktop target runtime trial (2026-11-02)

[Protocol, observations and limitations](DETAILS.md#desktop-target-runtime-trial-2026-11-02).

## Specified-directory read guard (macOS)

[Protocol, observations and limitations](DETAILS.md#specified-directory-read-guard-macos).

## Independent requirement-informed review (2026-11-02)

[Protocol, observations and limitations](DETAILS.md#independent-requirement-informed-review-2026-11-02).

## Operational readiness and local recovery (2026-11-02)

[Protocol, observations and limitations](DETAILS.md#operational-readiness-and-local-recovery-2026-11-02).

## Independent-destination backup restoration (2026-11-02)

[Protocol, observations and limitations](DETAILS.md#independent-destination-backup-restoration-2026-11-02).
