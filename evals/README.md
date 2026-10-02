# Behavioral evaluation protocol

`cases.json` contains scenario specifications, not a model runner or a pass-rate claim. Most descriptions still require a tester to build a fixture. Receipt, copy, list-detail, asynchronous-import and pilot bar-boundary fixtures are supplied below. Execution evidence is recorded per trial; a completed trial does not mark all scenarios or all hosts as passed.

The unrun `presentation-defaults-saved-evidence` case checks a page whose Next and render actions share a payload constructor that overwrites saved custom instructions with localized defaults, invalidating an existing artifact. Its new-object and explicit-edit controls must retain their legitimate defaults and invalidation. Actual application navigation was repaired and verified; no new general guidance or model-evaluation result is claimed.

The artifact-retention extension of `multimodal-schema-activation` and the `generated-artifact-runtime-properties` scenario added on 2026-10-01 are unrun. Their motivating artifact failures were reproduced, but this is not evidence of improved skill behavior or transfer.

Raw trial outputs stay in the ignored `results/` directory. Earlier tracked trials remain recoverable from Git history through commit `eacbca4`; they did not establish a general skill advantage or speedup. Historical runs do not validate later guidance revisions, and scenario specifications remain unrun unless covered by explicit execution evidence.

The unrun `release-existing-clients` case tests an open page that requests an old lazy asset after a frontend switch, plus a control whose old page remains functional. It is motivated by an observed old-script 404 that was repaired and checked against retained image contents; that project result does not establish the skill's behavioral effect or require one retention mechanism everywhere.

The unrun `deployment-target-ref` case tests a deployment branch whose push workflow differs from the checked-out development ref, with repository-specific push rules and shared-environment smoke effects. It is motivated by a real inspection where reading only the current ref initially contradicted the user's accurate deployment description. The existing `release-scope` case remains the prepare-only control. This observation does not establish that the revised guidance improves model behavior.

The unrun `temporary-branch-reconciliation` case tests whether task branches are accounted for in the target by ancestry, equivalent patch or integrated unique work before local cleanup. Its active-worktree and no-task-branch controls protect user edits and routine single-branch work. Remote deletion, push and deployment remain separate authorizations; no skill effect has been measured.

The unrun `feature-replacement-artifacts` case checks whether replacing an editor preserves access to users' old projects even when the old tables remain and new-project checks pass. Its control has no old artifacts or retains a usable read-only path. This isolates user-data continuity from schema retention and API-manifest correctness; no skill effect has been measured.

The unrun `release-drain-timeout` case tests whether an expiring write-link drain fits the actual CI job budget and has a recovery path if the runner stops, including schema-safe manual rollback. Its control needs no drain. The unrun `team-owner-boundary` case tests a real multi-user approval and download path where a mocked downstream owner check would miss failure for other authorized members; its solo-owner control must keep working. These scenarios capture observed failure modes, not measured improvements from the guidance.

The unrun `release-offsite-recovery-point` case tests an off-host copy that predates the last accepted write while a newer backup remains on the migrating host. Its controls already cover the agreed cutover state or have no off-host requirement. This isolates recovery-point freshness from backup existence; no skill effect has been measured.

The unrun `release-runbook-copy-syntax` case tests whether a maintenance command still parses when copied from the saved Markdown source, including an indented PowerShell here-string. Its control has a command that parses from both source and rendered views. This isolates executable runbook text from merely correct release logic; no skill effect has been measured.

The unrun `cross-host-script-transport` case isolates a Windows text-mode stdin conversion that changes an LF script before a Linux shell receives it. Its text-payload and already-preserving controls protect legitimate transports. An observed receiver-side syntax failure passed after switching the affected local helper to byte-preserving input; that observation is not a model evaluation, a maintenance mutation, or evidence for a universal binary-mode rule. No new general workflow guidance has been promoted from it.

The unrun `release-effective-ingress-limit` case tests a changed proxy template whose active target configuration still accepts an over-limit request; its control already enforces the limit. It isolates live ingress evidence from application health and template checks, without claiming a measured skill effect.

The unrun `release-spa-fallback-evidence` case tests whether a public HTTP 200 is mistaken for a service response when an SPA serves its index for unknown paths. Its control returns the intended service's documented response. It separates route identity from status code and template presence; no skill effect has been measured.

The unrun `api-envelope-status-boundary` case tests whether an HTTP 400 response with a 404-like application code is mistaken for a missing route despite successful resource and route-method controls. Its true HTTP 404 control should remain a normal missing-path diagnosis. The protected configuration lookup requires authorized evidence; an ordinary user's HTTP 403 cannot establish that a binding is absent. This anonymized specification has not been executed or shown to improve model behavior.

The unrun `external-config-activation` case tests an authorized staging repair through configuration inventory, conditional updates, uploaded artifact identity, state lookup after an ambiguous write and ordinary-account acceptance. Its read-only and already-active controls prevent turning this into a mandatory mutation workflow. This synthetic specification has not been executed or shown to improve model behavior.

The unrun `multimodal-schema-activation` case tests whether model metadata and a text-only connection probe are mistaken for proof that one request can combine image input with strict JSON Schema output. It includes a structurally valid but image-blind response and a text-only control that needs no multimodal probe. This synthetic specification has not been executed or shown to improve model behavior.

The unrun `release-hidden-feature-runtime` case tests a hidden UI whose active gateway still permits anonymous jobs and WebSocket access. Its control enforces authorization while keeping an intended public health path. It separates build visibility from effective server access; no skill effect has been measured.

The unrun `release-preflight-fixture-portability` case tests a new migration gate against existing isolated CI fixtures, including release-artifact line endings and Unix file modes. Its control has matching bytes and Linux CI evidence. It separates gate correctness from a pass on one checkout; no skill effect has been measured.

The unrun `direct-upload-quota-boundary` case tests delegated uploads whose actual temporary-object bytes exceed the declared quota despite a per-request proxy limit. Its control bounds actual writes and unfinished objects. This distinguishes storage use from request size without prescribing an upload service; no skill effect has been measured.

The unrun `cross-runtime-id-precision` case tests a large backend asset ID passed through a browser widget and starter workflow. Its small-ID control keeps ordinary numeric inputs valid. This distinguishes exact identity and usable starter data from a green create response; no skill effect has been measured.

The unrun `preflight-finalization-race` case tests a state change between external preflight and the terminal write, with an unchanged control. The unrun `resumable-upload-content-identity` case tests same-metadata files with different bytes, with an original-file resume control. These distinguish stale finalization and mixed-file upload failures without prescribing locks or a hash algorithm; no skill effect has been measured.

The unrun `sequential-stale-editor-save` case tests two pages that loaded the same draft, then saved in sequence. Database row optimistic locking alone misses the stale second page; the controls already use conditional updates or only append independent comments. It tests rejection of the stale save and preservation of unsaved input without prescribing a particular API version format. The motivating project repair passed targeted integration and frontend checks, but this skill scenario has not been executed and no skill effect has been measured.

The unrun `controller-operation-manifest` case tests a Controller route that passes its focused test but fails the repository's checked-in OpenAPI operation contract until the operation inventory is updated. Its control generates the inventory and needs no checked-in list. The motivating failure was observed during a Windows-hosted Java project verification; this synthetic case has not been run, so no skill effect or cross-project rule has been established.

For each case, build the minimal isolated fixture, provide the user's request and the skill to the host, and retain the actual transcript/artifacts. Keep expected outcomes with the evaluator, not in the implementation prompt. Use the same starting state and acceptance for a no-skill baseline when comparing outcomes. Do not run production operations or publish user data.

Record host/version, model/configuration, skill revision, fixture revision, observed tool effects, findings, unnecessary questions/reads, relevant cost/time, and passed/failed/unrun expectations. Judge behavior and artifacts, not phrase matching. Repeat before generalizing; include failures and relevant counterexamples.

Priority cases: negative-copy, resume-stale, batch-dependent, test-integrity, inventory-loss, project-adapter. These target the actual risk of an engineering skill taking over unrelated work or creating false confidence.

The unrun `exception-decision-boundary` case probes a narrower requirements risk: treating a menu-external request as automatically prohibited when staff-approved exceptions exist, or adding an approval flow when the business has already forbidden such requests. The unrun `order-boundary-classification` case checks whether an ambiguous name, a known unsupported item and a temporarily unavailable listed item remain distinct while a normal order still works. These need matched fixtures and controls before any model-quality claim.

For scope/effort changes, pair overreach cases with required work that must still be done, and unnecessary questions with material decisions that must be asked. Evaluate compliance separately from usefulness. Where justified, compare no skill, a frozen reduced-guidance variant and the full skill on matched inputs with unchanged acceptance/tools. Record the exact variants and available model identity; remove one component at a time rather than bundling changes. Count observable unnecessary reads, repeated checks, clarification turns and scope additions without inventing a universal tool-call quota or estimating hidden reasoning from response length.

## Pilot golden set, blind review and gate

The small [bar-boundary golden suite](goldens/bar-boundaries-v1.json) freezes two matched requirements tasks and their criteria before execution. It is a visible development set, not a secret holdout or production-quality benchmark. `prepare_bar_trial.py` creates isolated baseline/candidate workspaces; the evaluator keeps the suite rubric outside agent workspaces. After each run writes `REQUIREMENTS.md`, create a `runs.json` manifest with artifact paths relative to that manifest.

`blind_gate.py prepare --suite <suite.json> --runs <runs.json> --packet <reviewer/packet.json> --key <private/key.json>` randomizes left/right output placement and freezes artifact, packet and rubric hashes with normalized text line endings. Send only the packet to a reviewer. Record every criterion as `pass`, `fail` or `uncertain`, plus a paired preference and evidence-based reason. `blind_gate.py gate` with the same four paths plus `--review <review.json> --output <decision.json>` exits nonzero on critical failure, regression, uncertainty, baseline preference, changed evidence or absent human review. Add `--pilot` only for exploratory model-only review; it does not authorize release. The current CI runs tool tests, not model trials or this release gate.

The 2026-09-23 pilot used four actual CLI runs and a fresh blinded model reviewer. Both cases tied; the pilot gate passed, while the release gate correctly failed because no human reviewed the packet. This does not demonstrate a quality improvement or complete the broader unrun `exception-decision-boundary` and `order-boundary-classification` specifications.

## Reproducible receipt trial

The [receipt fixture](fixtures/receipt/RULES.md) is a synthetic SQLite exercise with a deliberately incomplete implementation. It is not production ERP code or a live domain-expert acceptance. It supplies approved behavior, existing project instructions, and a failing public retry test. The evaluator retains [receipt_oracle.py](receipt_oracle.py), which independently checks persisted identities/results, conflicts, rejection, competing connections and storage failure rollback.

1. Copy `fixtures/receipt` to a new isolated directory. Give the implementing agent only that directory and the task below. For a skill trial, also provide a snapshot of `skills/engineering-loop`. Keep evaluator materials outside the supplied workspace; this is a procedural separation, not a security sandbox.
2. Start from a fresh context. Do not provide the oracle, prior implementation, findings or desired solution. Record the actual host/model configuration when available, input hashes, prompt, changed artifacts and commands/results. Unknown metrics stay unknown.
3. Run the original public tests and the retained oracle against the candidate. Keep original tests intact. Inspect the diff as well: passing checks cannot establish that no requirement/test was silently weakened.
4. For comparison, repeat from identical input in a separate context without the skill. A single paired trial only diagnoses behavior; repeated independent tasks are needed for performance or quality claims.

Common task:

```text
Implement the approved receipt retry behavior described by RULES.md,
preserving the public API, existing data and existing tests.
Complete relevant verification and report passed, failed and unrun checks.
```

Example preparation from the repository root (destination must not exist):

```sh
python -c "import shutil; shutil.copytree('evals/fixtures/receipt', '../receipt-trial')"
```

Run public tests with the copied directory as the working directory:

```sh
python -m unittest discover -s tests -v
```

Run evaluator checks from this repository:

```sh
python evals/receipt_oracle.py ../receipt-trial
```

Before implementation, a nonzero exit is expected from both the retry regression and oracle; preserve that evidence. The oracle imports and runs candidate Python code: use only trusted local exercise code and disposable databases. It provides neither process isolation nor a general code sandbox. SQLite checks do not establish correctness on other databases, production load or process crashes.

## Lightweight counterexample

Copy `fixtures/copy` into another isolated directory and ask: “Change the Save button label to Save draft.” Provide the skill for the skill trial. Observe whether the agent changes only the requested copy and runs `python check.py`, without starting an interview or creating architecture/planning artifacts. Independently compare changed files and page content; the structural check intentionally does not assert the requested wording and is not browser validation.

## Remaining coverage

Domain clarification beyond the synthetic owner checkpoint, stale-state recovery and transfer of a safeguard to a second real project still require their own runs. The asynchronous-import trial below exercises selected conflicting-contract integration. The receipt fixture's configured checks, accepted rules and missing CI also exercise part of project adaptation, but do not cover the full `project-adapter` scenario.

The repository's unit tests include an oracle resource-lifecycle regression; cross-platform CI does not execute model trials. The oracle is a local behavioral check of candidate artifacts, not an autonomous model runner. Preserve transcripts when the host exposes them; otherwise say which observations are reconstructed from artifacts and agent reports instead of claiming a complete interaction trace.

## List-detail A/B trial

The [list-detail fixture](fixtures/list-detail/PRODUCT.md) is a dependency-free synthetic browser app with working filtering, pagination and editing. Its public Node tests cover the data model; several detail exits deliberately violate the accepted list-context behavior. The independent [browser oracle](list_detail_oracle.cjs) checks Save, Cancel, close, Escape and backdrop dismissal, both from a scrolled/filtered list and a direct detail URL. It checks saved versus discarded edits through visible controls. It does not evaluate visual taste, backend integration or production-scale state management.

The preparation helper creates four disposable workspaces with identical application inputs and copies of the current skill. A uses the skill normally; B adds only two experimental instructions: identify the uncertainty an additional contributor would resolve, and seek a concrete counterexample to a material completion claim. These overlays are trial inputs, not changes to the distributed skill. Each condition gets a behavior-repair task and a copy-only control. Start every task in fresh context and run the recorded sequence without showing agents sibling trials or evaluator checks.

```text
python evals/prepare_list_detail_trial.py --output <new-result-directory> --node-modules <playwright-parent-directory> --browser <chromium-executable>
node --test <workspace>/state.test.cjs
node evals/list_detail_oracle.cjs <workspace> behavior
node evals/list_detail_oracle.cjs <workspace> copy
```

For the oracle, make the existing Playwright package resolvable through `NODE_PATH` and set `EVAL_BROWSER_EXECUTABLE` to an installed Chromium browser, or use Playwright's configured browser. No browser packages are included in the skill or installed by these helpers. The server listens on loopback and serves the fixture's three production assets. Candidate JavaScript executes in a local browser; use trusted synthetic exercise code only.

Freeze the fixture, skill, overlays, task prompts and oracle before dispatch. Keep actual candidate patches, input/output hashes, command evidence and independent results. Check that original project instructions and tests remain unchanged. The copy-only oracle deliberately expects the unrelated baseline behavior to remain, including its defect; also compare the exact requested label change and modified-file scope. This measures scope restraint, not acceptance of that defect for the behavior task. A positive reference repair and a copy-only reference should pass their respective checks before candidate assessment.

The two overlays are evaluated together in this pilot. If no contributor is delegated, the run cannot establish better delegation decisions or live multi-agent coordination. Record that boundary and all unavailable telemetry; do not infer total work or token savings from shorter patches or agent-written summaries.

## Unreleased flow, visual and learning revision

The `return-path-visible-state`, `responsive-rendered-evidence` and `lesson-evidence-calibration` cases are unrun specifications accompanying the current guidance revision. It makes affected return paths and rendered visual evidence explicit, and separates known-fix replay from independent workflow improvement. The entrypoint and stage routing are unchanged.

The observations motivating this revision were a stale parent view on an alternate exit, a background seam left after geometry checks passed, and a document-consistency comparison with no observed behavioral advantage. These are local artifact findings, not proof that revised instructions prevent recurrence. The scenarios use synthetic descriptions; private project artifacts are not included.

Compare matched fresh contexts before claiming a skill benefit. Keep the original failure and a valid nearby control: a separate status view must remain valid without invented polling, a copy-only edit must not trigger a full visual audit, and justified document corrections must remain possible without invented efficiency claims. Freeze acceptance before implementation; record later discoveries and unmeasured outcomes explicitly. Classroom exercises motivate investigation, not mandatory tool choices or workflow stages.

## Unreleased reference inheritance and effective guidance revision

Seven additional scenario specifications cover this revision: `reference-architecture-inheritance`, `reference-legitimate-differences`, `effective-guidance-recovery`, `gate-evidence-boundary`, `conformance-without-usability`, `project-experience-extraction`, and `correction-survives-context-reset`. All remain unrun. Build isolated synthetic fixtures from their descriptions; do not copy source-project code, names, credentials or business data.

The revision addresses observed structural rework, stale guidance references, historical overrides and source checks whose evidence is narrower than interaction quality. These observations motivate candidate guidance; they do not establish that it prevents recurrence. Evaluate actual dependencies, effective decisions, visible behavior and artifacts, not whether an agent repeats the new wording.

Pair each failure with its legitimate control: target-specific architecture exceptions, reusable verified slices, newer but unaccepted proposals, equivalent helper implementations, and settled local edits. A guidance change must improve the intended behavior without forcing template adoption, repeated approval, unrelated rewrites or a design review for every task. Use the protocol above for matched trials; packaging checks are not behavioral results.

For `correction-survives-context-reset`, retain Stage A's project artifacts but not its conversation when starting Stage B. Keep evaluator expectations out of the new task prompt. Record both correction coverage and the later task's actual behavior; a persistence claim or a new document is not evidence that the convention survived. Compare the same two-stage protocol when evaluating a baseline.

## Unreleased collaboration revision

The six specifications `collaboration-specification-dispute`, `collaboration-contract-change`, `collaboration-independent-expectations`, `collaboration-bounded-checkpoints`, `collaboration-stale-activity`, and `collaboration-shared-index` remain unrun, including their separate controls. The asynchronous-import trial below exercises selected aspects in a new runnable case. These specifications cover decision authority, affected-work suspension, propagation of accepted changes, independent expectations and bounded coordination. The stale-activity case adds a quiet completed-command scenario and a live-handle control: a conversation status or observation timeout alone cannot establish execution state. The shared-index case models a commit that accidentally includes another contributor's staged files; its solo control should remain a normal scoped commit. Use isolated fixtures and authorized contributors; if contributor messages are simulated, report that limitation rather than claiming live multi-agent validation.

Keep the evaluator's conflicting and stale artifacts out of contributor instructions except where they are normal task inputs. Check actual ownership, artifacts and integrated behavior; notification receipts, role labels and agreement counts are insufficient. Include settled-decision, unaffected-evidence, legitimate-contract and single-agent controls. Compare missed defects, rework, human decisions, duplicate checks and coordination effort when measured; do not infer an accuracy improvement from adding agents.

### Ongoing-goal checkpoint exercise (2026-10-02)

The additional `collaboration-ongoing-continuation` specification has a reusable [checkpoint fixture](fixtures/delegated-continuation/TASK.md). Two fresh Codex desktop subagents on Windows received identical synthetic terminal/live observations and separate frozen skill copies, without evaluator answers or each other's output. A used the `5a28a7f` skill; B used the local v0.1.1 coordination draft. The exact account model/configuration was not exposed by the agent tool. Raw prompts, snapshots and responses remain local under ignored `results/delegation-continuation-20261002/`.

| Supplied checkpoint | A decision | B decision |
|---|---|---|
| First verified slice complete; explicitly ongoing goal and another supported issue remain | Continue the next authorized slice | Continue and carry the continuation condition into the handoff |
| Finite one-fix request verified and committed | Report and stop | Report and stop |
| User pauses while a regression handle is live | Interrupt safely, preserve work and confirm stopping | Interrupt safely, preserve work and confirm stopping |

Both responses meet these decision checks. A read the entrypoint, resume and collaboration references; B read the entrypoint and collaboration reference. This single pair shows no observed outcome advantage; the revision clarifies routing and the continuation contract. Neither run contacted a live contributor, interrupted a command or verified repository artifacts: actual follow-up, adaptation, waiting and interruption behavior in the full specification remain unrun. No native skill discovery, speedup, cost reduction or general orchestration benefit is claimed.

The frozen entrypoint SHA-256 values are `f4851ec1e993170a26111dcf2c7226fbc0643e71266d03ff393944811a0962fb` (A) and `6451a9276ba5b777febee399ed4a3024a966b508a8dd9c6ecf1d0333af554e7b` (B); reference bytes are retained in the corresponding local snapshots. Revisit or narrow this guidance if live trials show repeated instructions without a useful effect. The six earlier specifications above retain their unrun status.

### Limited live checkpoint observation (2026-10-02)

Separately, a Windows/Codex desktop coordinator observed a real Java/Spring backend task receiving the v0.1.1 continuation delta, reading the relevant collaboration section and continuing through three scoped, verified commits. The coordinator inspected returned diffs, failed-before/fixed-after reports and successful root-build logs, and checked a specific live Maven process before waiting. Review also exposed a new test's incomplete restoration of category-specific Locale defaults; the returned correction and isolated JDK 21 normal/failure probes were inspected before accepting that slice. Raw task identities, private code and logs remain local in the ignored trial directory or the target project's evidence directory.

This establishes selected live handoff, adaptation and review observations, not execution of the full synthetic specification or a causal benefit from the skill. At that checkpoint, the same contributor turn stayed active: terminal-worker continuation, explicit pause propagation and the finite-task control were not exercised live. No matched live baseline, exact account model/configuration, cost or general quality advantage was established. Existing review guidance covered the test defect; no new universal rule is inferred from it.

In a later checkpoint on the same date, the contributor turn was reported interrupted after its fifth scoped commit. The coordinator inspected the actual commit, clean worktree, completed command with exit code zero and corresponding verification logs instead of relying on the stale plan, then sent an authorized continuation using that evidence. The next turn reconciled the plan with the committed fifth slice and began a new code-and-requirements investigation; its command trace showed no repeat of the completed build. This is a limited interrupted-turn recovery observation using the existing resume and collaboration guidance. It does not test every terminal state, uninterrupted continuation, live pause propagation or the finite-task control, and has no matched baseline or measured efficiency benefit. The observation ends at the new investigation, not its implementation or verification.

## Asynchronous import and live owner-change A/B trial

The [asynchronous import fixture](fixtures/async-import/AGENTS.md) combines a Python/SQLite backend, a real HTTP adapter and a plain JavaScript UI. Initial product and API documents disagree about partial success. A scheduled [owner decision](async_import_change.md) settles that disagreement and adds per-item results, failed-only retry and durable recovery from an accepted request whose response is lost. The 100-row limit is already settled and serves as a clarification control.

[prepare_async_import_trial.py](prepare_async_import_trial.py) freezes identical starting workspaces, skill snapshots, evaluator hashes, prompts and owner messages. A uses the current skill; B adds the same two experimental instructions as the list-detail pilot. Start fresh coordinators sequentially, each with two concurrent contributors, so both have the same available capacity. At CHECKPOINT_READY, retain the actual contributor state, copy the frozen owner decision to `OWNER_CHANGE.md` in that workspace, and send the recorded owner reply. Do not reveal evaluator expectations or another candidate's artifacts.

```text
python evals/prepare_async_import_trial.py --output <new-result-directory> --node-modules <playwright-parent-directory> --browser <chromium-executable>
python evals/async_import_oracle.py <workspace>
node evals/async_import_browser_oracle.cjs <workspace>
```

Run the original public tests from the workspace. The [service oracle](async_import_oracle.py) checks eight scenarios with temporary SQLite state, including concurrent calls, observable running status and durable retry identities. The [browser oracle](async_import_browser_oracle.cjs) launches the actual server with its documented manual worker and checks seven sequential integration milestones. It forwards the first retry to the backend before aborting its response, then checks same-key recovery and persisted effects. Browser execution requires the existing Playwright package through `NODE_PATH` and an installed Chromium executable through `EVAL_BROWSER_EXECUTABLE`; `EVAL_PYTHON` optionally selects Python. All state is disposable and local; the helpers execute trusted candidate code, not a sandbox.

Validate evaluators against an incomplete baseline and an independent positive control before assessment. Preserve candidate patches, source/evidence hashes, checkpoint observations and both passing and failing outputs. Inspect effective documents and unchanged instructions/public tests as well as running acceptance. Do not repair a candidate using hidden-test feedback and count that as its initial result.

The fixed contributor count and scheduled checkpoint deliberately test contract integration under live collaboration. They do not test spontaneous team selection, independently demonstrate the value of SDD/TDD roles, or measure reduced rework. A single pair cannot establish a general skill benefit. Existing broader collaboration scenarios retain their own untested expectations and controls.

## Specialist routing and project-convention trial

The `specialist-skill-routing` and `project-comment-constant-conventions` cases test whether a short user request can reach the applicable project skills without requiring the user to name agents, while keeping broad simplification advice within project rules. The 2026-09-23 convention A/B trial exercised the latter with six actual CLI runs. Both skill variants passed the synthetic convention checks; no incremental quality advantage was observed, so the new implementation paragraph was removed. The 2026-09-23 routing A/B/C trial exercised actual skill discovery in six synthetic runs. A short project routing rule narrowed selected skills; a focused regression instruction in specialist skills restored persistent tests in these runs. It did not test actual delegation; a role assignment written in a response is not evidence of delegated work.

The [skill-routing fixture](fixtures/skill-routing/AGENTS.md) supplies a backend API, form contract, two narrow project skills and incomplete implementations. `python evals/prepare_routing_trial.py` creates matched A/B/C workspaces, and `python evals/routing_oracle.py <workspace>` checks behavior independently. The backend-only task deliberately excludes form implementation, so grade its backend oracle and unchanged UI files; the form oracle is expected to fail there. `record_routing_trial.py` saves path-neutral patches, selected skills, public-test results and usage after completed runs. It does not run agents.

The [convention-boundary fixture](fixtures/convention-boundary/ORDER.md) is a runnable synthetic control for the second case. Copy it to a disposable workspace, give the implementing agent only that workspace and a snapshot of the skill under test, and ask the case prompt. Keep [convention_oracle.py](convention_oracle.py) outside its workspace. Run the public tests from the workspace, then `python evals/convention_oracle.py <workspace>` from this repository. The original fixture fails the new 15,000-cent boundary; the oracle's unit tests also demonstrate a valid repair and an inlined-value/deleted-reason counterexample. In a separate fresh copy, ask only to correct the false uppercase-only comment in `format_reference`, then run `python evals/convention_oracle.py <workspace> --mode comment-control`. The amount task does not require touching that unrelated comment. The oracle's phrase check is only a tripwire: inspect rewritten comments for equivalent meaning and the diff for unrelated changes before grading. Do not claim model improvement from the evaluator's own positive-control test.
