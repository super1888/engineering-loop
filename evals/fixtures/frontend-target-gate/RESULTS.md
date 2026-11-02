# Frontend target gate smoke observations — 2026-11-02

## Conditions

Three fresh CLI invocations on macOS arm64, Codex CLI 0.166.0-alpha.5.1, same reduced isolated provider configuration as the product/UI follow-up. Requested and recorded session model: `gpt-6.1-sol`; effort was not explicitly fixed or recorded. Each received the working v0.1.14 entrypoint plus UI reference, with English-only, no-tools, advice-only instructions. No personal AGENTS or user skills were copied. The files were held unchanged while input prompts were prepared. Prompt hashes below identify actual supplied inputs; input file hashes are included separately.

These are a single-variant smoke check against three prespecified tasks, not an old/new comparison, automatic skill discovery or rendered behavior test. Task authors and scorers knew the intended gate. No implementation, browser session or actual usability validation occurred.

## Observations

| Condition | Criterion | Result | Evidence from final advice |
|---|---|---|---|
| Default desktop | No unrequested phone/tablet scope or acceptance gate | Observed | Names a desktop-only slice, explicitly excludes unrequested mobile, checks desktop windows, zoom, keyboard and relevant states. |
| Explicit phone | Retain requested desktop+phone implementation/acceptance | Observed | Names both targets, proposes phone rows and touch/filter/on-screen-keyboard checks; says required desktop and phone checks must pass. |
| Preserve existing mobile | Desktop-only change preserves existing phone behavior | Observed | Limits implementation to desktop spacing and existing breakpoint boundaries; proposes a before/after phone regression without new mobile designs or breakpoint changes. That regression is legitimate preservation, not newly imposed phone adaptation. |
| All three | No false implementation/testing claim | Observed | Each explicitly states that the plan has not been implemented or validated. |

All three invocations exited zero. This shows that supplied guidance was followed in these three advice samples. It does not establish reliable future compliance, visual quality, implementation correctness or net workflow benefit. Actual implementation tasks with independent browser checks remain future evidence. No guidance was tuned in response to these particular answers.

## Input identities

- `skills/engineering-loop/SKILL.md`: SHA256 `5da09e31c65000b0ebb18b486b7119360fb92c799facd588b5292d567b8b427e`.
- `skills/engineering-loop/references/ui.md`: SHA256 `c55d19644d388f98ddcc799377cc230e298b34f4a0c0400378248fc2134ca2c4`.
- `current-desktop` prompt: SHA256 `13dbb2e4104f69abb71f5eb817c7190996a1fdf2f295e3d6f098917241ef01b1`, exit 0.
- `current-phone` prompt: SHA256 `0e6d007f28ea79a3ad20e0b80735d5047fb049b831f8cb7436d63f5d4a317325`, exit 0.
- `current-preserve` prompt: SHA256 `e887069a1ed5d0d6d6eeb59e9d5f3a12f9092876d986f4444d194a02146ad582`, exit 0.

Raw prompts, transcripts, stderr, outputs and isolated configuration remain local under ignored `evals/results/frontend-target-gate/`.
