# Engineering Loop

**Connect the team. Challenge the task. Deliver with evidence.**

[中文](README.zh-CN.md) · [Chinese routing and execution manual](docs/ROUTING.zh-CN.md) · [Stage document templates](skills/engineering-loop/templates/index.md) · [Design](#design) · [Feedback loop](#feedback-loop) · [Install](#install) · [Changelog](CHANGELOG.md) · [How it works](#how-it-works) · [Examples](examples/workflows.md) · [Evaluation](evals/README.md) · [Contribute](CONTRIBUTING.md)

[![Checks](https://github.com/super1888/engineering-loop/actions/workflows/checks.yml/badge.svg)](https://github.com/super1888/engineering-loop/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg)](docs/ROADMAP.md)

A team task and delivery entrypoint for Claude Code and Codex. It requires verified PMS MCP access before routed work, challenges assumptions on every stage or specialist route, and coordinates task creation, claiming, execution and acceptance with traceable evidence.

**Using it in an existing Git repository?** Copy only the complete [`skills/engineering-loop`](skills/engineering-loop/SKILL.md) directory into that project's skill location, including `references/`, `templates/`, `scripts/` and `agents/`. The rest of this repository supports development and evaluation.

**v0.1 is an experimental workflow draft.** Packaging checks do not prove fewer bugs or faster delivery. We publish behavioral scenarios and welcome reproducible counterexamples before expanding the rules.

## The problem

An agent can pass tests while implementing the wrong requirement, resume from an obsolete handoff, or turn a two-line edit into a design ceremony. Engineering Loop addresses those workflow boundaries with one small router and focused references.

- **Batch decisions by dependency.** Research facts first; ask people about meaningful tradeoffs.
- **Resume from current evidence.** Reconcile the handoff, actual code, environment, and accepted decisions.
- **Match process to risk.** Clear local edits stay light; uncertain integration and data changes get deeper checks.
- **Verify the whole slice.** Check the relevant user path, failure/recovery behavior, and missing items.
- **Bound context.** Load the current stage, reuse unchanged context, keep detailed history out of the active summary.
- **Learn locally first.** Prefer a regression or executable check over another universal prompt rule.
- **Connect project rules to enforcement.** Locate domain examples, module/contract owners and active checks before scaling implementation; verify relevant safeguards when transferring lessons.

Routed work requires a configured, authenticated PMS MCP connection; the included adapter targets Kaneo. Install the skill and configure the connection separately: dependency metadata does not install or authenticate a service. No background daemon, mandatory agent team, automatic hook or prescribed application stack is included. These instructions require fail-closed behavior, but host/PMS controls enforce permissions, concurrent claims and state transitions.

## Design

Three layers, each more specific than the last. A task reads only what it matches:

```text
Entry SKILL.md (under 4 KB, an index only)
 ├─ Connect the PMS: verify identity, project and workflow
 ├─ Decide which stage this task is in
 └─ Six stage guides
     01 Requirements → challenge, requirements guide
     02 Design       → architecture, API contract, UI, delivery planning
     03 Development  → scenarios: frontend F1–F8, backend B1–B8, integration I1–I8, engineering E1–E4
                     → stack rules, testing method, diagnosis method, nine risk rules
     04 Testing      → review, security review, verification
     05 Release      → release, migration safety
     06 Operations   → operations, learning
     end of any stage → skill feedback (one usage line, plus a record when something went wrong)
```

| Decision | Reason |
|---|---|
| The entry is only an index | It is read on every task, so each added line is a fixed cost and buries the rules that matter |
| The PMS is required | Fine-grained tasks with recorded steps are what make a problem traceable to its source |
| Stages 01 and 02 require the challenge | An agent tends to agree with the asker. Mistakes in requirements and design cost the most, so the problem is separated from the proposed solution, an alternative and a failure case are written down, and the owner confirms before work starts |
| Stage templates are fixed | The requirement, plan, acceptance and release formats are deliverables the team agreed on; the rest of the skill may change, the templates do not |
| Team rules win over adapted ones | Rules rewritten from public skills sit in a separate section marked unconfirmed for the team |
| A check instead of a sentence where possible | A written rule can be missed; a failing build cannot |
| The skill does not modify itself | An agent's own account can be wrong, so maintainers confirm every added or removed rule |

### Where the rules come from

| Source | Current state | Confidence |
|---|---|---|
| The team's existing repositories | Rule files for Java/Spring, Python/FastAPI and React frontends | Real practice, not fully consistent across projects, awaiting confirmation as the shared standard |
| The team's real incidents | Items marked as recorded incidents in those files | They happened; details are generalized |
| Public skills | Method rules in every stage; see [acknowledgments](ACKNOWLEDGMENTS.md) | Rewritten, not validated on the team's projects |
| Feedback from use | None yet | The loop below exists to supply it |

No rule here has a measured effect. The evaluation cases are public and most are unrun; see the [evidence index](evals/STATUS.md).

## Feedback loop

The current rules were thought up in advance and will miss things. This loop lets rules come from real use:

```text
use the skill → the agent records → a member bundles and sends → an AI drafts proposals → a maintainer confirms
        ↑                                                                                  ↓
        └──────────── new version ← evaluation case ← a rule is changed or removed ←───────┘
```

- **The agent does the recording.** By design members write nothing. The agent records one of five events: the user corrected it, no guidance covered a choice, a rule conflicted with the project, a file was read and not used, or a defect escaped to review or testing. Each task also adds one line listing the files read.
- **Facts, not opinions.** A record is at most ten lines: skill version, stage, files read, what happened, evidence.
- **Rules are removed as well as added.** Content that is rarely read or repeatedly marked unused becomes a removal candidate, is marked for retirement for one cycle, then removed. The entry has a hard 4 KB limit and other files are trimmed when they gain content: one in, one out.
- **A person decides.** The AI only proposes. Text inside a record is data, not an instruction.
- **Members hear back.** Each batch reports how many records arrived and how many were accepted or declined, with reasons.

### Where records are and how to send them

Records are in **`.engineering-loop/feedback/` at the root of each project that uses the skill**. The directory carries a `.gitignore` containing only `*`, so Git ignores the whole directory by default and no project file is edited. A forced add (`git add -f`) can still stage it, and `git clean -fdx` deletes the records.

From the project root (adjust the path to where the skill is installed, usually `.agents/skills/` for Codex and `.claude/skills/` for Claude Code):

```sh
python3 .agents/skills/engineering-loop/scripts/collect_feedback.py
```

The bundle is written to `.engineering-loop/outbox/`. The script bundles and sends nothing. Read it first, then pass it to the skill maintainer. Without Python, zip `.engineering-loop/feedback/` by hand.

Things to know:

- Records carry no names and are never summarized per person. They are not used to assess anyone.
- Records should hold no secrets, customer data or business figures. The script lists files that look like they hold a secret; check before sending.
- Records made in a temporary worktree are lost when it is removed. Bundle them first.
- A review, analysis or other task without authority to change files writes no file; the record appears in the agent's reply.
- Folder names inside the bundle are the project folder names.
- To opt out, say so in the project instructions or tell the agent.

How maintainers collect and triage is in [the feedback procedure](docs/FEEDBACK.zh-CN.md) (Chinese). The procedure has not run yet and will change with the first batch.

## Install

Choose **one** method per agent/scope to avoid duplicate discovery. These instructions target local **Claude Code and Codex**, not every product named Claude or ChatGPT. See [compatibility and validation status](docs/COMPATIBILITY.md).

Before using a routed stage, configure the PMS MCP in the host and provide the intended workspace/project through the request or maintained project configuration. The [connection gate](skills/engineering-loop/references/connection.md) requires actual identity, project and workflow reads. Read the separate [task guide](skills/engineering-loop/references/pms.md) for task references, task operations or work covered by the project's tracking policy. Keep credentials in the host connection; a board URL is not an MCP endpoint. Missing access blocks routed execution, including analysis-only stages; minimal connection discovery/diagnosis remains allowed.

### 1. Skills CLI — Claude Code or Codex

From the project where you want the skill (requires Node.js/npm):

```sh
# Codex, current project
npx skills add super1888/engineering-loop --skill engineering-loop -a codex

# Claude Code, current project
npx skills add super1888/engineering-loop --skill engineering-loop -a claude-code
```

Add `-g` for a personal installation. The CLI is a third-party installer; review its prompts and destination. Use `--skill engineering-loop` with a space. The [Skills CLI documentation](https://github.com/vercel-labs/skills) describes scope, copy/symlink options, updates, and removal.

### 2. Claude Code plugin marketplace

In Claude Code:

```text
/plugin marketplace add super1888/engineering-loop
/plugin install engineering-loop@engineering-loop-marketplace
```

Then invoke the namespaced skill:

```text
/engineering-loop:engineering-loop Plan this change; clarify only unresolved decisions.
```

Follow the installer prompts to reload plugins or restart if required. No MCP server or hooks are included. See [Claude Code marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

### 3. Manual copy — no package manager

Clone or download this repository, then copy **the whole** `skills/engineering-loop` folder, including `references/`, `templates/`, `scripts/` and `agents/`, into one destination:

| Agent | Project scope | Personal scope |
|---|---|---|
| Codex | `<project>/.agents/skills/engineering-loop` | `~/.agents/skills/engineering-loop` |
| Claude Code | `<project>/.claude/skills/engineering-loop` | `~/.claude/skills/engineering-loop` |

Examples from inside a downloaded clone, for a fresh personal Codex installation:

```sh
# macOS / Linux; stop if already installed
test ! -e "$HOME/.agents/skills/engineering-loop" && \
  mkdir -p "$HOME/.agents/skills" && \
  cp -R skills/engineering-loop "$HOME/.agents/skills/engineering-loop"
```

```powershell
# Windows PowerShell; stop if already installed
$destination = Join-Path $HOME '.agents/skills/engineering-loop'
if (Test-Path -LiteralPath $destination) { throw 'Already installed; review before replacing.' }
New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
Copy-Item -LiteralPath 'skills/engineering-loop' -Destination $destination -Recurse
```

For Claude Code, use `.claude/skills` instead. For a project install, use the project's absolute directory instead of your home. The [release ZIP](https://github.com/super1888/engineering-loop/releases/tag/v0.1.0) contains a top-level `engineering-loop/` skill folder for the same destinations.

If the skill does not appear, check the destination and restart the agent. Current documented paths: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

For updates, review upstream changes and replace only this installed skill folder. For removal, use the original installer or remove that folder after checking its path; do not delete the parent skills directory.

## Start here

Codex, with a direct/Skills CLI installation:

```text
$engineering-loop Resume this project. Reconcile current code and accepted decisions,
then give me the next smallest verifiable slice. Do not implement yet.
```

Claude Code, with a direct/Skills CLI installation:

```text
/engineering-loop Implement this approved change. Reuse settled decisions;
ask only material unresolved choices and report evidence for completion.
```

Plugin installations use `/engineering-loop:engineering-loop` instead.

## When it should run

| Request | Expected behavior |
|---|---|
| Explicitly use Engineering Loop | Verify PMS MCP, identify the task's stage, then apply its guidance and challenge |
| Create, claim or update a team task | Read the intended project/task, respect authorization, check the write result |
| Resume a project with uncertain state | Reconcile state, then route |
| Cross-boundary change with unresolved decisions | Clarify the relevant decisions |
| Review or test an approved change | Select the relevant stage/support guide; reuse existing context |
| Explain a function, fix a typo, adjust local copy outside this workflow | Ordinary project workflow; explicit invocation still requires the MCP gate and a proportionate challenge |
| Already-scoped work handled by project guidance | Do not add a competing orchestrator |

Limited [local Codex discovery observations](docs/COMPATIBILITY.md#local-codex-project-copy-discovery-2026-11-02) now distinguish an observed implicit project-entry read from incomplete explicit entry-read evidence; they do not certify other hosts.

Automatic selection remains available through a deliberately scoped description. Selection is host/model-dependent; explicit invocation is the reproducible starting point. The skill is not an always-on hook. For explicit-only configuration, see [compatibility](docs/COMPATIBILITY.md#explicit-only-use).

## How it works

```text
user input + effective project/task context
                    |
       verified PMS MCP connection
                    |
 identify this task's stage; ask only if unresolved
                    |
     read the selected stage's guidance
                    |
 challenge the slice + load relevant specialist details
                    |
 execute -> verify -> authorized PMS evidence write-back
```

The first-level directory follows six project stages. Select the stage for the current task or deliverable. Different modules can be at different stages, and accepted inputs permit direct entry without replaying earlier work.

| Stage | Focused entry |
|---|---|
| 01 Requirements analysis and confirmation | [Problem, evidence and behavior boundaries](skills/engineering-loop/references/stages/01-requirements.md) |
| 02 Solution design and planning | [Product, architecture, UI and delivery planning](skills/engineering-loop/references/stages/02-design.md) · [Architecture selection and tradeoffs](skills/engineering-loop/references/architecture.md) · [Kickoff planning](skills/engineering-loop/references/delivery-planning.md) |
| 03 Development and integration | [Frontend/backend implementation, bug repair and integration](skills/engineering-loop/references/stages/03-development.md) |
| 04 Testing and acceptance | [Test execution, evidence and business acceptance](skills/engineering-loop/references/stages/04-testing.md) |
| 05 Release and validation | [Release preparation, deployment and version verification](skills/engineering-loop/references/stages/05-release.md) |
| 06 Continuous operations | [Incidents, ongoing maintenance and operational readiness](skills/engineering-loop/references/stages/06-operations.md) |

Each stage covers entry conditions, inputs, execution and reference selection, PMS use, deliverables, and exit or return conditions. UI design belongs to stage 02. UI implementation and developer self-checks belong to stage 03. An incident affecting a running service can enter stage 06 directly.

When the current stage needs a document or handoff, use the project's maintained format first. Open the matching stage template when a reusable structure is needed. Keep unknown fields pending, use the common challenge to resolve decision-changing gaps, and keep a concise existing record for a simple change. [Stage template index](skills/engineering-loop/templates/index.md)

Every activated stage and selected specialist still passes the built-in [grill-me-style challenge](skills/engineering-loop/references/grill.md). Investigate facts and reuse decisions before asking about material gaps; settled work can pass with zero questions. Project rules, review, collaboration, recovery and learning are conditional support, rather than additional peer stages. [Specialist selection](skills/engineering-loop/references/specialists.md) and [PMS task operations](skills/engineering-loop/references/pms.md) are read only when applicable. A stage is distinct from a board status, and selecting a stage does not automatically create a task.

All applicable project instructions, full-document requirements and delivery stop points still apply. Read only the selected stage and matching details, reuse valid connection evidence, and preserve effective state/evidence pointers in the established project sources. Stage changes alone do not restart the interview or identical connection probes. Already-loaded content still consumes context.

### Development subroutes

Stage 03 enters the [development router](skills/engineering-loop/references/development/index.md), reads the common [development core](skills/engineering-loop/references/development/core.md), and selects only relevant scenario sections:

| Area | Scenario index |
|---|---|
| Frontend · F1–F8 | [Components, forms, tables, navigation, state, files, accessibility and engineering](skills/engineering-loop/references/development/scenarios/frontend.md) |
| Backend · B1–B8 | [API, domain, persistence, transactions, access, async work, SDKs and runtime code](skills/engineering-loop/references/development/scenarios/backend.md) |
| Integration · I1–I8 | [Contracts, identity, data representation, writes, async flows, files, state and connectivity](skills/engineering-loop/references/development/scenarios/integration.md) |
| Engineering/shared capabilities · E1–E4 | [Libraries, CLI/scripts, builds/dependencies and generated tooling](skills/engineering-loop/references/development/scenarios/engineering.md) |

These 28 scenario entries describe matching conditions, exclusions and checks, and link to individual execution bodies with inputs, concrete steps, verification examples, delivery evidence and remaining project bindings. Read the selected body rather than expanding the whole catalog. Actual module configuration filters [stack-specific guidance](skills/engineering-loop/references/development/stacks.md); conditional React/Vue behavior checks do not replace the project's existing frameworks or libraries. Relevant changes independently select from nine [shared risk rules](skills/engineering-loop/references/development/risks.md), so precision, access, idempotency or concurrency guidance is maintained once rather than copied into each area.

The [delivery record](skills/engineering-loop/references/development/delivery.md) keeps artifact, check and PMS evidence in the project's existing task/document format without adding one card per professional role. The [template contract](skills/engineering-loop/references/development/templates.md) reserves future component/style entries; the intended Frontend-Design-Common source returned an empty repository when inspected. Actual templates and team-specific stack/package choices remain project-bound or pending. Optional missing detail can use maintained project conventions; a missing prerequisite blocks only dependent work. The old [implementation path](skills/engineering-loop/references/implementation.md) remains compatible. Selecting a subroute does not expand authority.

### A small example

Request: “Make batch import faster.”

After verifying the PMS connection and reconciling the authorized task, the agent identifies the actual bottleneck and accepted behavior. It asks about unresolved partial-failure and duplicate-handling choices, implements one recoverable import slice, then checks actual concurrency and user-visible outcomes. It does not assume that a thread count proves throughput or that a timeout means nothing was saved.

See [worked examples](examples/workflows.md) and [design boundaries](docs/DESIGN.md).

For a new project, the [project connection guide](skills/engineering-loop/references/project.md) reuses existing requirements, architecture and checks. It does not impose another tracker or ask every project to load every historical lesson. Domain decisions stay with the people responsible for them; mechanically checkable constraints should reach the project's actual gates.

The [requirements guide](skills/engineering-loop/references/requirements.md) distinguishes confirmed exclusions, authorized exceptions and undecided policies at relevant boundaries. It also separates an unclear request, an unsupported one and temporary unavailability when they have different outcomes. The [order-flow example](examples/workflows.md#a-bounded-order-flow-requirement) shows those distinctions without turning every hypothetical request into a feature.

## Validation and contribution

Per-version changes are in the [changelog](CHANGELOG.md).

```sh
python scripts/check.py
python -m unittest discover -s tests -v
python scripts/package.py --output dist/engineering-loop.zip
```

Python 3.10+ is needed only for repository checks/packaging and local evaluation helpers, not to use the skill. CI runs package checks and helper unit tests on Linux, macOS, and Windows; it does not run models. The [behavioral evaluation cases](evals/cases.json) are only partially exercised, and local trial results have not established a quality advantage or speedup. See [validation status](docs/COMPATIBILITY.md) before making compatibility or performance claims.

We especially want small counterexamples: unnecessary questions, missed decisions, context waste, invalid completion claims, or a project convention the skill accidentally overrides. Use [Issues](https://github.com/super1888/engineering-loop/issues) or [Discussions](https://github.com/super1888/engineering-loop/discussions); remove private code and data first.

The unreleased revisions clarify affected return-path outcomes, rendered evidence for visual defects, and the limits of known-fix replays ([three scenarios](evals/README.md#unreleased-flow-visual-and-learning-revision)). They also cover reference-project inheritance, effective conventions, gate evidence, task usefulness and corrections surviving a new session ([seven scenarios](evals/README.md#unreleased-reference-inheritance-and-effective-guidance-revision)). All ten scenarios remain unrun; historical product checks do not establish a benefit from the revised guidance. The existing stage routes remain in place; no fixed project architecture is imposed.

The optional [collaboration guide](skills/engineering-loop/references/collaboration.md) covers scoped ownership, accepted-change propagation, independent verification and explicitly ongoing goals without requiring a fixed agent team. A completed slice does not end an ongoing goal; finite tasks still stop when complete. Its [evaluation status](evals/README.md#unreleased-collaboration-revision) separates checkpoint exercises from live orchestration; additional agents are not evidence of improved accuracy.

The [release guide](skills/engineering-loop/references/release.md) now checks new preflights against existing isolated CI fixtures and identifies artifact bytes and host-specific permission evidence. Its [portability scenario](evals/README.md) remains unrun.

The unreleased native-command revision checks failed prerequisites before dependent writes or verification, while permitting expected negative checks. Its [isolated shell reproduction](evals/README.md#unreleased-native-command-gating-revision) passed on Windows; fresh-agent transfer and other hosts remain untested.

The [evaluation protocol](evals/README.md) retains reusable fixtures and checks. Raw model transcripts and trial output stay outside the tracked source tree; past trials are available in Git history.

If the workflow helps you, a star helps others discover it. Reproducible feedback helps us improve it.

## Credits and license

Inspired by published work on skill composition, specification-driven development, test-first feedback, and recoverable agent workflows. See [acknowledgments](ACKNOWLEDGMENTS.md). This initial implementation is independently written; it does not bundle those projects.

[MIT](LICENSE). Maintained by [super1888](https://github.com/super1888).

A local v0.1.21 two-turn sample failed to resume an unfinished summary after a restored-file question; its explicit-stop control was respected. See the [actual observations and limits](evals/fixtures/same-chat-continuation/RESULTS.md).
