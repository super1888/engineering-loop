# Engineering Loop

**Clear decisions. Small changes. Evidence before done.**

[中文](README.zh-CN.md) · [Install](#install) · [How it works](#how-it-works) · [Examples](examples/workflows.md) · [Evaluation](evals/README.md) · [Contribute](CONTRIBUTING.md)

[![Checks](https://github.com/super1888/engineering-loop/actions/workflows/checks.yml/badge.svg)](https://github.com/super1888/engineering-loop/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg)](docs/ROADMAP.md)

A portable skill for Claude Code and Codex that coordinates a software change from requirements to operations. It keeps human decisions explicit, loads stage guidance only when needed, and ties completion claims to evidence.

**Using it in an existing Git repository?** Copy only the complete [`skills/engineering-loop`](skills/engineering-loop/SKILL.md) directory into that project's skill location. Keep its `references/` and `agents/` subfolders; the rest of this repository is for development and evaluation.

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

No runtime dependency, background daemon, API key, mandatory agents, hooks, or prescribed tech stack. This is guidance, not a permission system or a guarantee of correctness.

## Install

Choose **one** method per agent/scope to avoid duplicate discovery. These instructions target local **Claude Code and Codex**, not every product named Claude or ChatGPT. See [compatibility and validation status](docs/COMPATIBILITY.md).

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

Clone or download this repository, then copy **the whole** `skills/engineering-loop` folder, including `references/` and `agents/`, into one destination:

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
| Explicitly use Engineering Loop | Enter the requested stage |
| Resume a project with uncertain state | Reconcile state, then route |
| Cross-boundary change with unresolved decisions | Clarify the relevant decisions |
| Review or test an approved change | Enter that stage; reuse existing context |
| Explain a function, fix a typo, adjust local copy | Ordinary project workflow; no lifecycle ceremony |
| Already-scoped work handled by project guidance | Do not add a competing orchestrator |

Automatic selection remains available through a deliberately scoped description. Selection is host/model-dependent; explicit invocation is the reproducible starting point. The skill is not an always-on hook. For explicit-only configuration, see [compatibility](docs/COMPATIBILITY.md#explicit-only-use).

## How it works

```text
effective project state + user intent
                 |
       bounded outcome / next slice
                 |
  requirements -> implement -> review / verify -> release -> operate
        ^                        |                            |
        +---- material change ---+---- demonstrated lesson ---+
```

Enter at the needed stage. Verification starts with requirements and continues during implementation; the arrows do not mandate a waterfall or approval at every step.

The entrypoint routes to a single relevant reference. It does not read all documentation, create a new planning directory, or restart the interview on each message. Long-running work keeps a small effective state and evidence pointers in the project's existing location. Already-loaded conversation content still consumes context.

### A small example

Request: “Make batch import faster.”

The agent first identifies the actual bottleneck and accepted behavior. It asks about unresolved partial-failure and duplicate-handling choices, implements one recoverable import slice, then checks actual concurrency and user-visible outcomes. It does not assume that a thread count proves throughput or that a timeout means nothing was saved.

See [worked examples](examples/workflows.md) and [design boundaries](docs/DESIGN.md).

For a new project, the [project connection guide](skills/engineering-loop/references/project.md) reuses existing requirements, architecture and checks. It does not impose another tracker or ask every project to load every historical lesson. Domain decisions stay with the people responsible for them; mechanically checkable constraints should reach the project's actual gates.

The [requirements guide](skills/engineering-loop/references/requirements.md) distinguishes confirmed exclusions, authorized exceptions and undecided policies at relevant boundaries. It also separates an unclear request, an unsupported one and temporary unavailability when they have different outcomes. The [order-flow example](examples/workflows.md#a-bounded-order-flow-requirement) shows those distinctions without turning every hypothetical request into a feature.

## Validation and contribution

```sh
python scripts/check.py
python -m unittest discover -s tests -v
python scripts/package.py --output dist/engineering-loop.zip
```

Python 3.10+ is needed only for repository checks/packaging and local evaluation helpers, not to use the skill. CI runs package checks and helper unit tests on Linux, macOS, and Windows; it does not run models. The [behavioral evaluation cases](evals/cases.json) remain a protocol with partial execution: one [local receipt/control and copy trial](evals/results/2026-09-21-local/report.md) is recorded with artifacts, including an evaluator defect and its fix. Both receipt conditions passed; no quality advantage or speedup is established. See [validation status](docs/COMPATIBILITY.md) before making compatibility or performance claims.

A [pilot golden set and blind-review gate](evals/results/2026-09-23-bar-gate/report.md) now compares two bar-boundary tasks. The model-only pilot review tied both variants; the release gate remained closed pending human blinded review. The gate is a local evaluation command, not a model check in CI or evidence that the candidate skill improved quality.

We especially want small counterexamples: unnecessary questions, missed decisions, context waste, invalid completion claims, or a project convention the skill accidentally overrides. Use [Issues](https://github.com/super1888/engineering-loop/issues) or [Discussions](https://github.com/super1888/engineering-loop/discussions); remove private code and data first.

The unreleased revisions clarify affected return-path outcomes, rendered evidence for visual defects, and the limits of known-fix replays ([three scenarios](evals/README.md#unreleased-flow-visual-and-learning-revision)). They also cover reference-project inheritance, effective conventions, gate evidence, task usefulness and corrections surviving a new session ([seven scenarios](evals/README.md#unreleased-reference-inheritance-and-effective-guidance-revision)). All ten scenarios remain unrun; historical product checks do not establish a benefit from the revised guidance. The existing stage routes remain in place; no fixed project architecture is imposed.

The optional [collaboration guide](skills/engineering-loop/references/collaboration.md) adds scoped ownership, specification-dispute resolution, accepted-change propagation and independent verification without requiring a fixed agent team. Its [four additional scenarios](evals/README.md#unreleased-collaboration-revision) also remain unrun; additional agents are not evidence of improved accuracy.

The [2026-09-22 UI A/B pilot](evals/results/2026-09-22-local-ui/report.md) compared current guidance with two experimental instructions on list-state repair and a copy-only control. Paired source artifacts were identical and all independent browser checks passed; no incremental correctness benefit was observed. Neither condition delegated, so that pilot did not test live coordination.

The subsequent [asynchronous-import A/B trial](evals/results/2026-09-22-async-import/report.md) used actual backend/frontend contributors, conflicting specifications and a scheduled owner contract change. Both conditions passed eight independent service scenarios and seven browser-flow milestones. An evaluator false positive was corrected with positive and negative controls. No incremental correctness benefit or reduction in work was established; the two candidate instructions remain experimental.

Two [scenarios](evals/README.md#specialist-routing-and-project-convention-trial) probe specialist-skill routing from short requests and preservation of project comments and constants under broad simplification advice. In the [synthetic convention A/B trial](evals/results/2026-09-23-convention/report.md), both variants passed without an incremental quality advantage, so the unproven implementation paragraph was removed. In the [synthetic routing A/B/C trial](evals/results/2026-09-23-routing/report.md), a short project routing rule selected the matching skills, and a focused regression instruction in specialist skills restored persistent tests in the tested tasks. Actual subagent delegation and HR-project outcomes remain untested.

If the workflow helps you, a star helps others discover it. Reproducible feedback helps us improve it.

## Credits and license

Inspired by published work on skill composition, specification-driven development, test-first feedback, and recoverable agent workflows. See [acknowledgments](ACKNOWLEDGMENTS.md). This initial implementation is independently written; it does not bundle those projects.

[MIT](LICENSE). Maintained by [super1888](https://github.com/super1888).
