# Behavioral evaluation protocol

`cases.json` contains scenario specifications, not a model runner or a pass-rate claim. Most descriptions still require a tester to build a fixture. Two small fixtures are now supplied below. Execution evidence is recorded per trial; a completed trial does not mark all scenarios or all hosts as passed.

Recorded run: [2026-09-21 local receipt/control and copy trials](results/2026-09-21-local/report.md). Both receipt conditions passed the selected oracle; no skill advantage or speedup was established.

That report identifies its own skill snapshot. The later [autonomy and effort-boundary revision](../docs/讨论决策与后续验证.md) has structural/distribution validation only; its new behavioral scenarios remain unrun.

For each case, build the minimal isolated fixture, provide the user's request and the skill to the host, and retain the actual transcript/artifacts. Keep expected outcomes with the evaluator, not in the implementation prompt. Use the same starting state and acceptance for a no-skill baseline when comparing outcomes. Do not run production operations or publish user data.

Record host/version, model/configuration, skill revision, fixture revision, observed tool effects, findings, unnecessary questions/reads, relevant cost/time, and passed/failed/unrun expectations. Judge behavior and artifacts, not phrase matching. Repeat before generalizing; include failures and relevant counterexamples.

Priority cases: negative-copy, resume-stale, batch-dependent, test-integrity, inventory-loss, project-adapter. These target the actual risk of an engineering skill taking over unrelated work or creating false confidence.

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

Domain clarification, stale-state recovery, integration of conflicting contracts and transfer of a safeguard to a second real project still require their own runs. The fixture's configured checks, accepted rules and missing CI also exercise part of project adaptation, but do not cover the full `project-adapter` scenario.

The repository's unit tests include an oracle resource-lifecycle regression; cross-platform CI does not execute model trials. The oracle is a local behavioral check of candidate artifacts, not an autonomous model runner. Preserve transcripts when the host exposes them; otherwise say which observations are reconstructed from artifacts and agent reports instead of claiming a complete interaction trace.

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

The four specifications `collaboration-specification-dispute`, `collaboration-contract-change`, `collaboration-independent-expectations`, and `collaboration-bounded-checkpoints` remain unrun. They exercise decision authority, affected-work suspension, propagation of accepted changes, independent expectations and bounded coordination. Use isolated fixtures and authorized contributors; if contributor messages are simulated, report that limitation rather than claiming live multi-agent validation.

Keep the evaluator's conflicting and stale artifacts out of contributor instructions except where they are normal task inputs. Check actual ownership, artifacts and integrated behavior; notification receipts, role labels and agreement counts are insufficient. Include settled-decision, unaffected-evidence, legitimate-contract and single-agent controls. Compare missed defects, rework, human decisions, duplicate checks and coordination effort when measured; do not infer an accuracy improvement from adding agents.
