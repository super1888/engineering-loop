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
| What has actually been demonstrated? | [Current status and limits](STATUS.md) |
| Scenario inventory, including unrun cases | [Case specifications](cases.json), [retained details](DETAILS.md) |
| Receipt, copy-only or integration task | Method sections below |
| Recent product/UI, review or operations samples | [Current status](STATUS.md), report sections below |
| Native helper behavior | Repository tests and the relevant detailed section; not a model-efficacy claim |
| Contributor environment differs from the coordinator | [Reproduction controls](fixtures/delegated-environment/TASK.md), [observations and limits](fixtures/delegated-environment/RESULTS.md) |

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
