# Exploratory matched advice trial — 2026-11-02

## Conditions

Six fresh `codex exec` invocations on macOS arm64, CLI 0.166.0-alpha.5.1. Recorded session model: `gpt-6.1-sol`; reasoning effort not recorded. Baseline source: `f12204d3549848a9d585ec0a150dd3d931150cee` (v0.1.12). Enhanced inputs: working v0.1.13 entrypoint and references, frozen in local prompts; hashes below identify the actual inputs rather than a later commit. No production data or browser execution. Model was instructed not to call tools; observed output contained advice only.

Personal AGENTS and skills were absent from the isolated CODEX_HOME. Authentication and provider configuration were reused locally. Baseline product/control initially used the original configured ancillary MCP services, which emitted transport warnings; before enhanced conditions these were removed from the isolated config, preserving the same model provider. UI conditions both used the reduced config. This startup difference confounds timing comparisons; no speed claim is made. Product/control compare the entrypoint + requirements package; UI compares the matching entrypoint + requirements + verification package, with the new UI reference additionally supplied to enhanced. This is not a single-sentence ablation or automatic-routing test.

## Observed results

`Observed` means present in advice, not executed or proven useful. `Absent` means the response omitted the criterion. No criterion was scored from phrase matching alone.

| Prespecified criterion | Baseline | Enhanced | Supporting observation |
|---|---|---|---|
| Product: challenge ticket-count assumption | Observed | Observed | Baseline: “Ticket counts may reward small tasks”; enhanced questions whether counts reflect valuable productivity. |
| Product: affected people/current alternatives or measurable loss | Observed | Observed | Both propose employee/manager discovery; enhanced explicitly asks frequency, cost and current handling. |
| Product: bounded hypothesis test, success signal, option to abandon | Uncertain | Observed | Baseline proposes small discovery and asks what improvement justifies a pilot, but does not define a bounded outcome test; enhanced proposes shorter delivery without more rework and explicitly allows stopping. |
| Product: at most three questions, no implementation | Observed | Observed | Both give three questions and advice only. |
| Control: proceed without reopening discovery | Observed | Observed | Both preserve behavior/layout and propose focused diff/check verification; enhanced additionally mentions committing, an unsolicited detail in this no-implementation task. |
| UI: task-derived layout and representative content | Observed | Observed | Both use list/detail review with long reasons, multiple attachments and missing evidence. |
| UI: meaningful alternatives before expansion | Observed | Observed | Both compare list/detail against expandable cards; enhanced prototypes only the selected direction after sketch comparison. |
| UI: missing/loading/error states and mobile/keyboard concerns | Absent | Absent | Both address missing evidence and mobile layout, but omit loading/error and keyboard concerns. Partial coverage does not satisfy the combined criterion. |
| UI: propose interactive/rendered validation without claiming execution | Observed | Observed | Both propose supervisor prototype sessions with observable errors and navigation checks; neither claims actual testing. |

## Interpretation and limits

All six CLI invocations exited zero and produced final responses. The baseline already exhibited most intended behavior. Enhanced product advice was more explicit about measured loss, current alternatives and stopping; this single task cannot establish a reliable benefit. UI showed no clear observed advantage on the prespecified coverage and missed the same state/keyboard criterion in both conditions. No usability, actual visual quality, complete development workflow or reduction in real rework was evaluated. The enhanced UI response was Chinese despite the English task, a language difference that also limits direct comparison.

One sample per condition, one model, no blind scoring and no human user sessions: these are exploratory observations, not an efficacy claim. The evaluator knew the change goals; expected criteria were recorded before execution. Raw prompts, transcripts, hashes and timing remain local in ignored `evals/results/product-ui-first-round/`. Repeat with held-out tasks and blind judgment before claiming transfer; investigate UI omissions with a fresh task rather than adding rules solely to fit this known answer.

## Prompt identities

- `baseline-control`: SHA256 `3e60b7b199407a9019ddd2184b4e5a71b91df67674ad7488a63112ba7bf6b180`, exit 0.
- `baseline-product`: SHA256 `f773ab7b90954a64cf3eace75c3f270c39e220ce7ed9f4df534efaedf805be85`, exit 0.
- `baseline-ui`: SHA256 `7d1692382722c1f7b5974469a8f1a637b9e9fc482c8cf4b1ba3c194b23bbefa9`, exit 0.
- `enhanced-control`: SHA256 `d641ef1067954fc1e49b6ea8fb5224f4e12cbb31c74b4981ba53d73076eb7d30`, exit 0.
- `enhanced-product`: SHA256 `459d8de96e32edc49e445461489826affca6514246d07c64f01b6edd8f67d13a`, exit 0.
- `enhanced-ui`: SHA256 `a96a3ac75868fa8171f204183506356a6af23ebb90d002098252c1efc73439d6`, exit 0.
