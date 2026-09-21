# Local behavioral trial — 2026-09-21

## Outcome

Both receipt candidates passed all seven evaluator tests and reported 13 passing local tests with inspectable command/output evidence. The skill trial and control produced similar transaction-based solutions. **This run shows no correctness advantage or speedup attributable to the skill.** The copy trial stayed scoped to the requested label.

This was one synthetic task per condition, run through Codex desktop collaboration agents with fresh conversation context and inherited model configuration. Exact resolved model/sampling identifiers, token cost, end-to-end elapsed time and human review effort were not exposed or measured. Native skill discovery, Claude Code and production ERP work were not tested.

## Inputs and artifacts

- Repository starting revision: `f587e08362bbe80b18023b4fc183d9734fafe909`; skill changes were an uncommitted snapshot identified by per-file hashes in [manifest.json](manifest.json).
- Both receipt agents received identical copies of the [fixture](../../fixtures/receipt/RULES.md), already-approved rules and the same implementation task. Only the skill condition received the skill snapshot. Full dispatch prompts, with local paths replaced by placeholders, are in [prompts.txt](prompts.txt).
- The implementing agents were instructed not to inspect sibling or evaluator material. This was procedural isolation, not a security boundary. Complete host transcripts were unavailable; preserved evidence consists of dispatched prompts, artifacts, agent-written command records and independent checks. Their reports alone cannot prove every interaction or absence of hidden context.
- [With-skill patch](with-skill.patch), [control patch](without-skill.patch) and [copy patch](copy.patch) reproduce the source changes. Each was applied to a fresh fixture copy with `git apply`, exit 0; reproduced source texts matched the candidate. Source hashes are in the manifest.
- Parent inspection confirmed both receipt candidates preserved `AGENTS.md`, `RULES.md` and all original tests byte-for-byte. The skill candidate updated the existing `WORK.md`; the control left it unchanged. This isolated difference is not a general workflow-quality result.

## Observed checks

| Check | Result | Evidence |
|---|---|---|
| Original receipt public suite | Expected failure: 1 of 3 tests | [Baseline](baseline-public.txt) |
| Final oracle against original fixture | Expected failure: 14 assertions across 7 test methods; no cleanup error | [Negative control](baseline-oracle-final.txt) |
| With-skill local suite | 13 passed, exit 0; agent-recorded baseline/red/final outputs | [Agent evidence](with-skill-agent.txt) |
| Control local suite | 13 passed, exit 0; agent-recorded baseline/final outputs | [Agent evidence](without-skill-agent.txt) |
| With-skill independent oracle | 7 passed, exit 0 | [Parent-run output](with-skill-oracle-final.txt) |
| Control independent oracle | 7 passed, exit 0 | [Parent-run output](without-skill-oracle-final.txt) |
| Copy task | Only label bytes changed; structural check exit 0; no extra project files | [Parent check](copy-check.txt) and [patch](copy.patch) |
| Oracle without a candidate argument | Exit 1 with usage message | [Output](oracle-missing-argument.txt) |

Outputs preserve observed results; local repository, user and runtime paths are redacted, and trailing whitespace in text logs is normalized. Patch context whitespace is preserved, with a narrow Git attribute exception for that artifact format; source-code whitespace checks remain active. Test durations in the logs measure test execution only, not development speed. Agent suites were not rerun merely to duplicate already inspectable evidence; the parent ran the separate oracle and inspected preserved tests/artifacts.

Repository validation also passed: distribution/link checks, five unit tests with one additional symlink test skipped by host permissions, skill-creator structural validation, Python syntax checks and offline packaging. Commands and results are in [repository checks](repository-checks.txt). A separate read-only review found no actionable standards/specification issue in the inspected change; it did not run tests or reproduce the trial. No new remote CI run is claimed.

## Real failure found in the evaluation helper

The first oracle run encountered Windows cleanup errors in both candidates because the evaluator's own inspection connections were not closed. The SQLite transaction context did not close those connections. See [initial output](with-skill-oracle.txt); the control encountered the same seven cleanup errors. This was an evaluator defect, not candidate rejection.

A focused regression failed before the correction ([red](oracle-resource-red.txt)) and passed after it ([green](oracle-resource-green.txt)). The helper now closes its connections explicitly. All business assertions stayed unchanged; both candidates were evaluated again with that corrected helper, and the original defective fixture still failed. The final oracle hash is in the manifest.

The demonstrated lesson is preserved locally in [project lessons](../../../docs/LESSONS.md), with its executable regression. It was not promoted into a universal skill rule.

## Limits and next evidence

The receipt oracle covers selected SQLite interleavings, reopen/retry behavior and injected transaction failure, not production capacity, process-kill recovery, other databases, authentication, HTTP/UI or financial correctness. Business policies were pre-approved by the fixture author, not a live domain expert. The copy check is static, not a browser test.

The broader scenario catalog remains partially unexecuted. Domain clarification, stale-state recovery, conflicting contributors and safeguard adoption in a second real project need separate trials. No claim of cross-project prevention, lower long-term maintenance cost, overall behavioral pass rate or improved speed follows from this run.
