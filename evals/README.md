# Behavioral evaluation protocol

`cases.json` contains scenario specifications, not a model runner or a pass-rate claim. Most descriptions still require a tester to build a fixture. Receipt, copy, list-detail and asynchronous-import fixtures are supplied below. Execution evidence is recorded per trial; a completed trial does not mark all scenarios or all hosts as passed.

Recorded run: [2026-09-21 local receipt/control and copy trials](results/2026-09-21-local/report.md). Both receipt conditions passed the selected oracle; no skill advantage or speedup was established.

Earlier run: [2026-09-22 list-detail A/B trial](results/2026-09-22-local-ui/report.md). Current guidance and a two-instruction candidate overlay produced identical paired source artifacts and passed the same browser acceptance. No incremental correctness benefit was observed; no candidate delegated work.

Earlier run: [2026-09-22 asynchronous-import A/B trial](results/2026-09-22-async-import/report.md). Both conditions coordinated live backend/frontend contributors through a scheduled contract change and passed the same independent service and browser checks. An evaluator false positive and its correction are retained. No incremental correctness benefit or work reduction was established.

Each report identifies its own skill snapshot and tested scope. Historical runs do not validate all later [guidance revisions](../docs/讨论决策与后续验证.md); scenario specifications remain unrun unless covered by explicit execution evidence.

For each case, build the minimal isolated fixture, provide the user's request and the skill to the host, and retain the actual transcript/artifacts. Keep expected outcomes with the evaluator, not in the implementation prompt. Use the same starting state and acceptance for a no-skill baseline when comparing outcomes. Do not run production operations or publish user data.

Record host/version, model/configuration, skill revision, fixture revision, observed tool effects, findings, unnecessary questions/reads, relevant cost/time, and passed/failed/unrun expectations. Judge behavior and artifacts, not phrase matching. Repeat before generalizing; include failures and relevant counterexamples.

Priority cases: negative-copy, resume-stale, batch-dependent, test-integrity, inventory-loss, project-adapter. These target the actual risk of an engineering skill taking over unrelated work or creating false confidence.

The unrun `exception-decision-boundary` case probes a narrower requirements risk: treating a menu-external request as automatically prohibited when staff-approved exceptions exist, or adding an approval flow when the business has already forbidden such requests. It needs a matched undecided-policy fixture and settled-prohibition control before any model-quality claim.

For scope/effort changes, pair overreach cases with required work that must still be done, and unnecessary questions with material decisions that must be asked. Evaluate compliance separately from usefulness. Where justified, compare no skill, a frozen reduced-guidance variant and the full skill on matched inputs with unchanged acceptance/tools. Record the exact variants and available model identity; remove one component at a time rather than bundling changes. Count observable unnecessary reads, repeated checks, clarification turns and scope additions without inventing a universal tool-call quota or estimating hidden reasoning from response length.

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

The four complete specifications `collaboration-specification-dispute`, `collaboration-contract-change`, `collaboration-independent-expectations`, and `collaboration-bounded-checkpoints` remain unrun, including their separate controls. The asynchronous-import trial below exercises selected aspects in a new runnable case. These specifications cover decision authority, affected-work suspension, propagation of accepted changes, independent expectations and bounded coordination. Use isolated fixtures and authorized contributors; if contributor messages are simulated, report that limitation rather than claiming live multi-agent validation.

Keep the evaluator's conflicting and stale artifacts out of contributor instructions except where they are normal task inputs. Check actual ownership, artifacts and integrated behavior; notification receipts, role labels and agreement counts are insufficient. Include settled-decision, unaffected-evidence, legitimate-contract and single-agent controls. Compare missed defects, rework, human decisions, duplicate checks and coordination effort when measured; do not infer an accuracy improvement from adding agents.

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

The `specialist-skill-routing` and `project-comment-constant-conventions` cases test whether a short user request can reach the applicable project skills without requiring the user to name agents, while keeping broad simplification advice within project rules. The [2026-09-23 convention A/B trial](results/2026-09-23-convention/report.md) exercised the latter with six actual CLI runs. Both skill variants passed the synthetic convention checks; no incremental quality advantage was observed, so the new implementation paragraph was removed. The [2026-09-23 routing A/B/C trial](results/2026-09-23-routing/report.md) exercised actual skill discovery in six synthetic runs. A short project routing rule narrowed selected skills; a focused regression instruction in specialist skills restored persistent tests in these runs. It did not test actual delegation; a role assignment written in a response is not evidence of delegated work.

The [skill-routing fixture](fixtures/skill-routing/AGENTS.md) supplies a backend API, form contract, two narrow project skills and incomplete implementations. `python evals/prepare_routing_trial.py` creates matched A/B/C workspaces, and `python evals/routing_oracle.py <workspace>` checks behavior independently. The backend-only task deliberately excludes form implementation, so grade its backend oracle and unchanged UI files; the form oracle is expected to fail there. `record_routing_trial.py` saves path-neutral patches, selected skills, public-test results and usage after completed runs. It does not run agents.

The [convention-boundary fixture](fixtures/convention-boundary/ORDER.md) is a runnable synthetic control for the second case. Copy it to a disposable workspace, give the implementing agent only that workspace and a snapshot of the skill under test, and ask the case prompt. Keep [convention_oracle.py](convention_oracle.py) outside its workspace. Run the public tests from the workspace, then `python evals/convention_oracle.py <workspace>` from this repository. The original fixture fails the new 15,000-cent boundary; the oracle's unit tests also demonstrate a valid repair and an inlined-value/deleted-reason counterexample. In a separate fresh copy, ask only to correct the false uppercase-only comment in `format_reference`, then run `python evals/convention_oracle.py <workspace> --mode comment-control`. The amount task does not require touching that unrelated comment. The oracle's phrase check is only a tripwire: inspect rewritten comments for equivalent meaning and the diff for unrelated changes before grading. Do not claim model improvement from the evaluator's own positive-control test.
