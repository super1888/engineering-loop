# Compatibility and validation

Last updated: 2026-09-21. Intended targets: local Claude Code and Codex with Agent Skills support. Other compatible hosts may read the same instructions, but are not certified here.

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

Later local trial on Windows (2026-09-21): [receipt/control and copy evidence](../evals/results/2026-09-21-local/report.md). Explicitly supplied skill files were used by isolated Codex desktop subagents; this does not test native discovery or install invocation. Both receipt candidates passed seven independent evaluator checks, and the copy candidate changed only the label. An evaluator resource defect was reproduced, fixed and regression-tested. The full scenario catalog, Claude Code behavior, production work and cross-project transfer remain unverified. No overall behavioral pass rate, quality advantage or development speedup is claimed.

CI checks links, package structure, metadata consistency, archive contents, archive path safety and the evaluator's connection-release regression. It does not run models or prove automatic trigger accuracy or instruction compliance. This turn ran local checks; a new remote CI result is not claimed.

Local personal-folder installation does not imply availability in cloud products or scheduled remote sessions. Follow each host's documentation for those environments. No automatic install, setting mutation, or API call occurs merely from reading this skill.
