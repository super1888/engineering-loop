# Local UI A/B trial — 2026-09-22

## Outcome

Both repair candidates passed all 10 independent browser scenarios, and both copy candidates passed the 10 copy/preservation scenarios. The two repair workspaces are byte-identical, as are the two copy workspaces. **No additional correctness benefit from the two candidate instructions was observed in this pilot.** Neither candidate instruction is promoted into the distributed skill on this evidence.

All four agents reported no delegation or user questions. The copy candidates changed only the requested label and did not repair the unrelated bug. This supports a narrow scope-control observation; it does not establish lower overall effort. No live multi-agent coordination was exercised within a candidate task.

## Experiment

This pilot compares the committed Engineering Loop guidance (A) with the same guidance plus two experimental instructions (B): identify the uncertainty a delegated contributor would resolve, and seek a concrete counterexample to a material completion claim when review is warranted. The overlays are frozen in [inputs.json](inputs.json); the distributed skill was not changed for this experiment.

Each condition receives two tasks from identical application inputs: repair detail-return state, and change only the Save label. Four fresh-context Codex desktop collaboration agents run sequentially in the recorded order: behavior-A, copy-B, behavior-B, copy-A. They inherit the same host model configuration without explicit model overrides. Exact resolved model/sampling identifiers, complete host transcripts, token cost and end-to-end development time are unavailable. Test durations are not development-speed measurements.

Input skill revision is recorded in the manifest, with per-file hashes for the exact skill and the newly authored, initially uncommitted fixture. The fixture, oracle, prompts, overlays and acceptance were fixed before candidate dispatch. Normal product requirements enumerate supported exits and the direct-link exception; agents do not receive the oracle or defect location. File separation is procedural, not a security boundary. Candidate agents may delegate but need not do so; source-project code and real user data are not used.

## Independent acceptance

The fixture uses plain HTML/JavaScript and a Node data-model test. The evaluator launches a real headless Edge browser through Playwright, serves the candidate on loopback and exercises controls. Five exits are tested from a filtered, paginated, scrolled list and from a direct detail URL: Save, Cancel, close button, Escape and backdrop. The oracle verifies visible list state, edited/discarded names on reopening, closure and browser errors. It is independent of candidate-written tests and does not inspect the implementation's chosen repair.

The copy control expects exactly the label change and preserved baseline behavior, including the unrelated return-state defect. Preserving that defect is a scope-control result, not product acceptance for the repair task.

Before dispatch:

- Public Node tests passed 2/2 while browser acceptance failed four list-dismissal paths. Save and all direct-detail exits passed. [Baseline summary](baseline.json) was reconstructed from the parent tool output; it is not a raw stdout transcript.
- An evaluator reference repair passed 10/10: change the four `leaveDetail(false)` calls to `leaveDetail(true)` in a disposable copy. [Positive behavior control](oracle-positive-behavior.json).
- An evaluator reference copy change passed 10/10: change only the button label in another disposable copy. [Positive copy control](oracle-positive-copy.json).

Oracle scope is limited to the supplied three production assets and supported DOM controls. It does not assess visual taste, focus management, persistence across reload, other browsers, exhaustive data/viewport combinations, backend integration or production load.

## Results

| Task | A: current skill | B: candidate overlay | Independent evidence |
|---|---|---|---|
| Return-state repair | 10/10 passed; only app.js changed | 10/10 passed; identical source | [A oracle](behavior-A-oracle.json), [B oracle](behavior-B-oracle.json) |
| Copy-only control | 10/10 passed; only Save label changed | 10/10 passed; identical source | [A oracle](copy-A-oracle.json), [B oracle](copy-B-oracle.json) |
| Original rules and public tests | Preserved byte-for-byte in both tasks | Preserved byte-for-byte in both tasks | [Hashes and integrity results](outcomes.json) |
| Candidate public checks | 2/2 reported passing in each task | 2/2 reported passing in each task | Agent command records below |
| Delegation and questions | None reported in either task | None reported in either task | Agent accounts below; not a complete host transcript |

The parent reused the inspectable public-test evidence and independently ran the retained browser oracle. It checked source scope and original-file integrity, and applied each patch to a fresh fixture copy. All four replayed workspaces matched the corresponding candidate bytes exactly using `git -c core.autocrlf=false apply <patch>`.

| Candidate | Patch | Agent command/output record | Agent account | Agent-authored browser regression snapshot |
|---|---|---|---|---|
| behavior-A | [Patch](behavior-A.patch) | [Commands](behavior-A-commands.txt) | [Account](behavior-A-agent-report.md.txt) | [10-case script](behavior-A-app.browser.test.cjs.txt) |
| behavior-B | [Patch](behavior-B.patch) | [Commands](behavior-B-commands.txt) | [Account](behavior-B-agent-report.md.txt) | [15-case script](behavior-B-browser-check.cjs.txt) |
| copy-A | [Patch](copy-A.patch) | [Commands](copy-A-commands.txt) | [Account](copy-A-agent-report.md.txt) | Not run by candidate |
| copy-B | [Patch](copy-B.patch) | [Commands](copy-B-commands.txt) | [Account](copy-B-agent-report.md.txt) | Not run by candidate |

The regression snapshots are redacted evidence, not portable drop-in runners. The evaluator oracle and candidate patches are the supported reproduction path. Behavior-B exercised both groups and authored 15 browser cases versus A's 10, but this yielded no different final outcome on the frozen acceptance. More tests alone do not establish improved accuracy or justified cost.

## Evidence and interpretation boundaries

Agent command records and final accounts are self-maintained evidence, not complete host interaction transcripts. Parent checks independently assess final browser behavior, source diffs and preservation of original instructions/tests. Local account/machine identifiers and paths are redacted in retained evidence; original candidate hashes and normalized retained evidence hashes are recorded separately. No user intervention is used to guide a candidate toward the hidden checks.

Behavior-A's initial browser test setup used an accessible-name locator that did not resolve. The agent recorded and corrected that locator before reproducing the actual product failures; it retained the acceptance assertions. Its corrected pre-fix matrix failed on the four dismissals and on a second Cancel following Save, then passed after the implementation fix. This test-maintenance work is distinct from product rework and is not hidden as a successful first attempt.

Behavior-B encountered the same initial locator issue and an additional PowerShell write-command error that left the product file unchanged. Its report and command record retain both issues, the corrected pre-fix failure matrix and the passing final checks. These are observed execution costs; one run does not attribute them to the candidate instructions.

The parent initially found a patch-replay byte mismatch: Git converted LF to CRLF. The normalized source was unchanged, and setting `core.autocrlf=false` for replay reproduced the exact bytes for all four patches. No candidate code, oracle assertion or product expectation was changed to resolve this archive issue. Fixture script line endings are also pinned in the repository attributes.

Runtime evidence reports Node 24.14.1, Edge 153.0.4234.48 and Playwright 1.62.1 on Windows. Preparation and artifact collection use Python. Condition names were visible in workspace paths; this was not a blinded trial. Parent oracle work sometimes overlapped a later candidate, so this run cannot support latency comparisons even if timestamps were recovered.

This is one task per condition for each of two task types. The two candidate instructions are tested together, so their individual effects cannot be separated. If neither condition delegates, the result does not evaluate live coordination, stale-contributor propagation or better team decisions. A failure to observe an advantage on this pilot is not proof that the candidate guidance can never help. Wider claims need fresh tasks, repeated matched runs and measured coordination/human effort.

The next useful experiment, if requested, is a task with a real unresolved contract and an independently useful contributor, paired with a settled-decision control. Repeating this known repair would mostly measure replay of the same solution. The broader scenario catalog remains unexecuted except for specifically recorded trials.

Repository distribution/link checks, helper syntax and preparation freeze checks passed. The existing Python suite had five passes and one host-permission skip for symbolic links. [Validation summary](repository-checks.txt) distinguishes these checks from the browser and model-trial evidence.
