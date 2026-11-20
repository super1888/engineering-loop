# Compatibility and validation

Last updated: 2026-11-20. Intended targets: local Claude Code and Codex with Agent Skills support. Other compatible hosts may read the same instructions, but are not certified here.

## Unreleased v0.1.27 release and operations routes

The skill and current manual expose six entries. Stage 05 covers an identified release, including cutover, verification and release-specific recovery. Stage 06 covers ongoing operations and independent runtime incidents, readiness and recovery. The recorded evidence is scoped to the tested installation, package and routing cases. [Six-stage cases](../evals/fixtures/six-stage-routing/TASK.md) · [Execution status](../evals/STATUS.md)

## Unreleased v0.1.26 execution baselines

All 28 development catalog entries now point to independent execution bodies. Framework-neutral steps and conditional React/Vue behavior checks retain project-owned libraries, architecture, commands and policies; they are guidance rather than a new framework/runtime implementation. The intended shared-template repository returned empty when inspected, so no template/package compatibility is claimed.

The [current specification](../evals/fixtures/development-details/TASK.md) and [validation record](../evals/fixtures/development-details/RESULTS.md) distinguish source/reference/package checks from actual task/runtime evidence. Older v0.1.25 model samples do not validate these new bodies or a framework's real behavior.

## Unreleased v0.1.25 development subroutes

Stage 03 now enters a fact-based development subrouter: four professional catalogs with 28 scenarios, shared core and nine conditional risks. Framework/stack bindings and the shared component-template catalog have explicit pending slots; no React/Vue standard, actual external template or automatic matcher is implied. Existing implementation guidance is redistributed with its legacy entry path retained. Project-required full reads, MCP, authorization and acceptance remain effective.

See the [current specification](../evals/fixtures/development-routing/TASK.md) and [validation record](../evals/fixtures/development-routing/RESULTS.md). Source review, distribution checks and actual model/task observations are separate evidence levels; no general hit-rate or context-saving claim is established by additional index entries.

## Unreleased v0.1.24 five-stage navigation

The entrypoint now selects the current task's requirements, design/planning, development/integration, testing/acceptance or release/validation stage after the required MCP gate. Each stage indexes inputs, execution, conditional PMS use, deliverables and acceptance/return conditions, applying the common challenge and existing professional guidance. Review, coordination, recovery and learning remain conditional support. Existing guide paths and the Kaneo dependency remain available; no stack/component registry, automatic selector or new deployment authority is added.

See the [acceptance specification](../evals/fixtures/five-stage-routing/TASK.md) and [validation record](../evals/fixtures/five-stage-routing/RESULTS.md) for current checks and limits. Historical v0.1.23 results below retain their original source identity and do not certify this routing change.

## Unreleased v0.1.23 common-core split

The mandatory reads are now the entrypoint, [connection gate](../skills/engineering-loop/references/connection.md) and common [challenge](../skills/engineering-loop/references/grill.md), followed by selected-stage guidance. Task operations and specialist coordination have their own conditional references; all applicable project instructions and required full reads remain effective. The three common source files total 12,007 bytes versus 21,772 in v0.1.22. This is not a token or runtime-cost measurement.

The [controlled local-copy trial](../evals/fixtures/core-route/TASK.md) supplies synthetic PMS reads or no configured synthetic PMS to two otherwise matching native CLI contexts. Its protocol unit checks, source-read guards, actual model/tool events and production access are separate claims. Neither condition grants real PMS writes; the much broader v0.1.22 matrix remains unrun. A copied skill under controlled tools is not a claim of native discovery across hosts or universal route reliability.

[Actual local observations](../evals/fixtures/core-route/RESULTS.md) retain output-path, approval and shell limitations, then a final native-profile pair: actual identity/project/workflow reads preceded the exact approved label edit; without configured PMS, entry/connection reads and read-only metadata discovery ended with refusal and no file changes. The native tool profile passed bounded read/write/network controls without trust, sandbox bypass or global changes. Host metadata was not fully isolated; model identity remains unknown. Two local outcomes do not establish general routing or production write safety.

## Unreleased v0.1.22 connection contract

Routed work now requires an authenticated PMS MCP connection with successful identity, intended-project and workflow reads; the included operation map and Codex dependency metadata name Kaneo. Configure access separately in the host. A board URL is not an MCP endpoint, and a metadata declaration or enabled CLI entry is not a passed connection check. No automatic connection installation, credential change or offline bypass is included. Actual transport and host dependency-metadata behavior remain host-specific; the YAML declaration alone does not establish compatibility.

Every routed stage/specialist also uses an independently written grill-me-style challenge. Existing stage guides remain, but historical lightweight, native-discovery and model results below belong to their recorded versions and do not validate this new gate or route challenge. The [new evaluation matrix](../evals/fixtures/pms-grill-routing/TASK.md) is unrun. Packaging checks cannot prove fail-closed model behavior, atomic task claiming or server-side workflow enforcement.

Local maintenance checks on macOS (2026-11-18), Python 3.12.16 and Node.js 24.22.2: distribution checks and skill structural validation passed; the root unit suite reported `Ran 103 tests` and `OK (skipped=6)` (Windows junction, unavailable PowerShell and browser-fixture setup controls); the 17-entry offline ZIP matched all packaged source bytes. Some skip records are whole fixture classes, so subtracting six from the reported test count is not a passed-test count. These are distribution/tool checks. Live read-only Kaneo calls also returned authenticated identity, the supplied target project and its four workflow states. No task creation, assignment, status mutation, forced-disconnection test or new matrix model run was performed; read success does not establish write permission or enforcement. Private actor/project details are intentionally omitted.

## Installation surfaces

| Surface | Mechanism | Scope |
|---|---|---|
| Codex | `.agents/skills/engineering-loop` | Project or personal |
| Claude Code | `.claude/skills/engineering-loop` | Project or personal |
| Claude Code plugin | Marketplace manifest and root plugin | Chosen by Claude Code installer |
| Skills CLI | `--skill engineering-loop -a codex` or `-a claude-code` | Project by default, personal with `-g` |
| Offline | ZIP / whole-folder copy | Same direct-install locations |

Sources: [Codex documentation](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [Skills CLI](https://github.com/vercel-labs/skills).

## Explicit-only use

Default metadata allows scoped automatic discovery. To require manual invocation in a **local copy**:

- Codex: add `policy: { allow_implicit_invocation: false }` to `agents/openai.yaml`, preserving its other fields.
- Claude Code: add `disable-model-invocation: true` to the YAML frontmatter of `SKILL.md`.

The controls are host-specific. Plugin updates can replace local edits; keep a direct local copy or a fork for a persistent custom policy. This is an optional user choice, not the default distributed behavior.

## Evidence status

### Local Codex project-copy discovery (2026-11-02)

One macOS arm64 CLI build (`0.166.0-alpha.5.1`) was exercised with three complete project-local copies of unreleased v0.1.18, separate CODEX_HOME settings and unchanged HOME. The implicit uncertain-resume sample tool-read the project copy's entrypoint and resume reference and reconciled stale state. The ordinary label edit stayed lightweight. Explicit `$engineering-loop` produced an announcement and resume-reference read, but no visible entrypoint tool read; the predeclared strict read-evidence condition remains unmet, and native body-injection provenance was not captured.

See the [frozen tasks](../evals/fixtures/native-discovery/TASK.md) and [actual observations](../evals/fixtures/native-discovery/RESULTS.md) for hashes, original criteria and audit limits. These local CLI observations do not establish native behavior in the desktop UI, Claude Code or another CLI build, nor reliable automatic selection, complete catalog isolation or a quality benefit. Earlier installation surfaces and historical checks below retain their own scope.

Historical trial reports and raw outputs are available in Git history through commit `eacbca4`; new raw runs remain local. The summaries below do not imply broader model coverage.

Local packaging check on Windows with Python 3.12.3 (2026-10-03): a native directory junction was not reported as a symlink and allowed an outside fixture file into the offline ZIP. Version 0.1.9 rejects its native mount-point reparse tag in both distribution checks and packaging, before traversing its contents or replacing an existing archive. The focused eight-test distribution run passed seven cases, including the native junction, deterministic ZIP and hardlink controls; the symbolic-link case skipped because this host disallowed creating it. The junction test skips on non-Windows hosts; no new cross-platform CI or model result is claimed.

Initial local checks on Windows (2026-09-21):

| Check | Result |
|---|---|
| Skills CLI 1.7.0, local source, isolated project installs | Codex and Claude Code installs completed |
| Skills CLI 1.7.0, GitHub shorthand source, isolated project installs | Both targets completed; all 10 skill files matched source bytes |
| Claude Code 2.1.215 native manifest validation | Plugin and marketplace passed without warnings |
| Codex skill creator structural validation | Passed; installed Codex CLI version: 0.146.1 |
| Distribution unit tests | 4 passed; symlink test skipped because this Windows host disallowed creating it |
| Model behavior and native skill invocation | Not evaluated in these initial installation checks; see the later local trial below |

These installation checks use temporary project directories, not a personal skills folder. See the linked CI runs and release notes for published-source and platform results.

[Initial cross-platform CI](https://github.com/super1888/engineering-loop/actions/runs/35565419870) passed on Windows, macOS, and Linux for commit `73074fa`, using Python 3.12. It ran metadata/link checks, distribution unit tests, and offline packaging. Later runs are available in [Actions](https://github.com/super1888/engineering-loop/actions/workflows/checks.yml).

The release notes record actual packaging, CLI, and installation checks for this version. Native host discovery and model behavior are separate from successful file installation.

Later local trial on Windows (2026-09-21): receipt/control and copy tasks. Explicitly supplied skill files were used by isolated Codex desktop subagents; this does not test native discovery or install invocation. Both receipt candidates passed seven independent evaluator checks, and the copy candidate changed only the label. An evaluator resource defect was reproduced, fixed and regression-tested. The full scenario catalog, Claude Code behavior, production work and cross-project transfer remain unverified. No overall behavioral pass rate, quality advantage or development speedup is claimed.

CI checks links, package structure, metadata consistency, archive contents, archive path safety and the evaluator's connection-release regression. It does not run models or prove automatic trigger accuracy or instruction compliance. This turn ran local checks; a new remote CI result is not claimed.

Additional Windows trials on 2026-09-22 covered list-detail/copy A/B and asynchronous-import/owner-change A/B. The latter used actual backend/frontend contributors, with both candidates passing eight service scenarios and seven sequential browser milestones after an independently checked evaluator correction. These are explicit-file local trials with controlled prompts and roles, not native discovery, full scenario coverage or evidence of lower rework/cost. The two experimental overlay instructions were not promoted to the distributed skill.

The 2026-09-23 convention A/B trial used explicit-file local CLI runs, including a matched Ponytail full-mode pair. Both skill variants preserved the synthetic project's comment and constant and passed the oracle; no added quality benefit was observed. The trial did not test native discovery, automatic routing or the reported HR-project failure, and the CLI did not expose its account-default model identity.

The 2026-09-23 routing A/B/C trial used six fresh local CLI runs against two synthetic order tasks. Matching specialist skills were read and applicable public and independent behavior checks passed. The project routing rule narrowed skill selection; adding a focused regression instruction to specialist skills restored persistent tests in the two tested C runs. This is evidence for skill discovery in those workspaces, not native multi-agent delegation or a general output-quality or cost advantage. The CLI again did not expose its account-default model identity.

The 2026-09-23 bar-boundary golden-set pilot used four fresh local CLI runs and a separate blinded model review. Both pairs tied on the fixed rubric. The pilot gate passed, but the release profile failed for lack of human blinded review. CI covers the gate tool's unit tests, not live model trials or a production release decision; one synthetic trial per arm is too little to establish a quality or cost advantage.

Local personal-folder installation does not imply availability in cloud products or scheduled remote sessions. Follow each host's documentation for those environments. No automatic install, setting mutation, or API call occurs merely from reading this skill.

The 2026-10-02 [coordination observations](../evals/README.md#ongoing-goal-checkpoint-exercise-2026-10-02) combine two fresh simulated checkpoint responses with selected live handoff, adaptation and review evidence from an ongoing backend task. Both simulated variants made the correct continue/stop/pause decisions; no outcome advantage was observed. The live task continued through verified slices. A later interrupted turn resumed from committed artifacts and valid verification, reconciled its stale task state and began the next investigation without repeating the completed build. Pause propagation and the finite-task control remain untested live. This does not validate the full collaboration scenario, native discovery, other hosts or a general quality/cost benefit.
