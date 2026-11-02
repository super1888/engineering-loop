# Native Codex discovery observations — 2026-11-02

Three fresh macOS arm64 Codex CLI invocations used `codex-cli 0.166.0-alpha.5.1`, requested model `gpt-6.1-sol`, and the complete unreleased Engineering Loop v0.1.18 package installed at each external disposable workspace's `.agents/skills/engineering-loop`. No skill body was injected by the evaluator into the prompt or system instructions. The explicit condition named `$engineering-loop`; the other two did not. The [acceptance](TASK.md) was frozen before dispatch. This is a non-blind sample of three different tasks, not a matched efficacy comparison.

## Actual outcomes

| Condition | Observed evidence | Frozen outcome |
|---|---|---|
| Implicit uncertain resume | Announced Engineering Loop; tool-read the installed project `SKILL.md` and `references/resume.md`; inspected checkpoint and implementation; `python3 -B check.py` passed; reported stale checkpoint, limited check coverage and a bounded next step. Task files remained unchanged. | Passed the stated routing and read-only criteria. |
| Explicit `$engineering-loop` | Announced Engineering Loop and tool-read project `references/resume.md`; inspected implementation and checkpoint; ran the passing check and reported the same scoped recovery conclusion. Task files remained unchanged. No separate `SKILL.md` tool-read event appeared. | Strict frozen requirement for a visible SKILL.md tool read was not met. Announced skill use and scoped resume behavior were observed; direct entrypoint-read provenance is unproven by this transcript. |
| Copy-only control | Replaced only `>Export</button>` with `>Download</button>`, preserving the onclick handler and other bytes; no resume reference, implementation plan or skill announcement. | Passed the local-edit/lightweight criteria. Catalog discovery itself was allowed. |

All three CLI processes exited 0. The explicit result is retained as incomplete against the literal predeclared evidence requirement; a host may supply explicitly selected skill content without a separate tool read, but this run did not capture initial developer metadata to establish that mechanism. The criterion was not weakened after observing it.

## Isolation and identities

HOME was unchanged. Each child used its own initially empty CODEX_HOME with only copied authentication and minimal provider settings; no personal skill, AGENTS instruction, plugin configuration or body injection was copied. The workspaces and their ancestors had no AGENTS.md at preflight. `evals/read_guard.py` protected the actual repository and personal `.agents` root, with successful absolute/relative/symlink read-denial probes and writable workspace controls before each dispatch. Receipts recorded completion and exit 0. The personal same-name skill resolves into the denied repository; the observed implicit read explicitly names the project copy. This protects specified roots only, not the whole filesystem, network or credentials.

The native host still attempted remote plugin synchronization and MCP initialization; stderr included retry/network warnings, but the model turns completed. Thus independent CODEX_HOME did not mean a completely empty host catalog. Remote/system metadata and initial developer messages were not fully captured. Do not infer total source isolation or reliable implicit selection merely from these runs. No other host, repeated trial, baseline, quality advantage or cost improvement was tested.

The resolved CLI executable was `/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex`. The entrypoint SHA256 was `6897b21e93f4ffb1c7646901f5b657c00d1bd30cc54d648d4c02dff94197e767`; a local manifest retains the entire source package's per-file SHA256 and configuration digest. Prompt SHA256 values:

- Implicit: `4ed3ccaea0b9c2dc219c78a3c7f4648b8213aa9490c0445faa9ded31cb9362bd`.
- Explicit: `86d28ce54782f4fcb30be9d5fc1803b64a82ad0d5197a6e22e859a45a184fa6a`.
- Copy-only: `bcbe1eeee55ca595f15b9ba72240064bab2f436e3339b130b0c9a2bb6dab0d2f`.

Task-file preservation was checked against the setup script’s exact constants after completion; independent pre-dispatch task-file hashes were not retained. The acceptance file was written before execution, but its separate timestamped hash was not saved. These are audit limits, not evidence of a changed contract.

Raw prompts, manifests, JSONL events, guard receipts, stderr and final messages remain local outside the repository in `/private/tmp/engineering-native-zdlcn8gf/logs`; an ignored pointer is at `evals/results/native-discovery/artifact-location.txt`. Raw configuration/authentication and signed remote URLs are excluded from committed evidence. One initial wrapper preparation placed the receipt inside the denied repository and failed before any dispatch; the receipt/log location was corrected before the three model invocations, without changing tasks or acceptance.
