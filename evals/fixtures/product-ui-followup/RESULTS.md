# New-task advice follow-up — 2026-11-02

## Actual conditions

Six fresh local `codex exec` invocations completed with exit 0 on macOS arm64, CLI 0.166.0-alpha.5.1. Requested model and recorded session model: `gpt-6.1-sol`; reasoning effort was not frozen or recorded. All conditions used the same isolated reduced provider configuration copied before execution, the same explicit English-only/no-tools/no-implementation instruction, and two concurrent CLI processes at most. No personal AGENTS or installed user skills were copied into the isolated CODEX_HOME. Authentication remained local and is not part of the report.

Baseline: `f12204d3549848a9d585ec0a150dd3d931150cee`, v0.1.12. Enhanced: `8db89e7`, v0.1.13. Both received their matching entrypoint, requirements and verification reference; enhanced additionally received its UI guide. These frozen commit inputs are unaffected by later working-tree edits. This is supplied-package advice comparison, not automatic routing or single-rule ablation.

The task author knew the first-round goals/results. These are newly executed examples, not an independent hidden test set. Product and copy-only control intentionally retain the same broad problem type. UI now explicitly states slow/failing service, keyboard and narrow-tablet use; it therefore cannot establish that an omission on the earlier implicit task has been fixed. Narrow-screen acceptance is justified by this explicit request; this run does not evaluate the later desktop-default policy.

## Criterion observations

Observed denotes coverage in advice only, not executed behavior. Scores were reviewed against final responses, with no automatic phrase-count grading. The scorer knew the variants; an independent agent reviewed the tasks and observations but was also not blind.

| Criterion | Baseline | Enhanced | Supporting observation |
|---|---|---|---|
| P1 underlying problem | Observed | Observed | Both reject AI enthusiasm as sufficient demand evidence. |
| P2 alternatives and concrete frequency/impact | Observed | Observed | Baseline asks about last week's missed updates and current tools; enhanced asks current tools, frequency and consequences. |
| P3 bounded experiment and success signal | Observed | Observed | Both propose a manual digest using existing channels/sources and observe catching/acting on important items. Baseline gives no fixed duration, but none was required. |
| P4 abandon/change feature | Observed | Observed | Baseline compares improving the tracker or notifications and conditions the digest on fit; enhanced explicitly says continue/revise/stop. |
| P5 <=3 questions, no implementation | Observed | Observed | Each gives exactly three questions and advice only. |
| U1 task and representative content | Observed | Observed | Both use item→borrower→confirmation→next, long titles and missing images. |
| U2 meaningful alternatives before replication | Absent | Observed | Baseline proposes one workspace adapted to viewports; enhanced compares one-page flow with sequential steps using the same records. Viewport adaptation alone is not an alternative interaction design. |
| U3 slow/loading | Observed | Observed | Both preserve selections, show pending progress and prevent repeated confirmation. |
| U4 failures/retry/input/duplicates | Observed | Observed | Both distinguish definite failure from unknown outcomes, retain context and require authoritative result checking before unsafe repetition. |
| U5 missing/long content | Observed | Observed | Both preserve usable identification without images and wrap long titles. |
| U6 keyboard/focus | Observed | Observed | Both address keyboard navigation, visible focus/order and status announcements. |
| U7 narrow layout | Observed | Observed | Both adapt the flow to the explicitly requested narrow tablet. |
| U8 interactive/rendered evidence boundary | Observed | Observed | Both propose prototype task sessions and separate real service integration; neither claims execution. |
| C1 accepted copy-only scope | Observed | Observed | Both retain the sentence-only replacement and prohibit layout/behavior/other-copy changes. |
| C2 no renewed discovery/prototype | Observed | Observed | Neither asks questions or adds design exploration. |
| C3 focused verification/no false execution | Observed | Observed | Both propose targeted checks and explicitly say implementation has not happened. |

## Conclusion and next evidence

The enhanced response made alternative UI approaches explicit; the baseline already covered the other requested UI concerns and all product/control criteria. This single sample per condition provides no reliable efficacy, speed, token-cost or real usability claim. No browser, implementation, user session or production integration was run. Different answer length and stochastic variation can explain differences. The follow-up narrows the earlier UI observation: explicit task constraints elicited loading/error/keyboard coverage in both packages, so the first omission is not evidence that adding more general guidance is the right correction.

Retain the existing UI guide pending evidence from runnable interface tasks; do not add rules solely to force this known answer. A future study should freeze effort/configuration, use independently authored tasks and blind comparison, and inspect actual browser behavior when claiming interface quality. Raw prompts, events, stderr, final outputs and configuration remain local under ignored `evals/results/product-ui-followup/`.

## Input identities

- `baseline-product`: SHA256 `52ca8bff8d161de0081bd3cfc72f164c8944566a55419d9911bf7a9a0bbdf58b`, exit 0.
- `enhanced-product`: SHA256 `2dbfa16290cc2eac915220b07e6910e2d1b70fc67d579e0c4e557438035a37df`, exit 0.
- `baseline-ui`: SHA256 `e1ff1480efcd98a2081441985cba76105d1d7314cfa4f63fb9649ecdb29752ee`, exit 0.
- `enhanced-ui`: SHA256 `128212e024bcc3d9a765da79380d72e034efcc96643116d7fc87ff2b15c6b706`, exit 0.
- `baseline-control`: SHA256 `1d13fa9bb541b903600fb73a9d7b638ad9c7b8a0cd1f85189f08dec20c8e1f83`, exit 0.
- `enhanced-control`: SHA256 `a82eece4d686c7ce94436dcf4ba3b5a61f9d7ce0e125eb6a2fd8f88ae126c293`, exit 0.
