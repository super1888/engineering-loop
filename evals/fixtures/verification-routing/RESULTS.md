# Verification routing observations — 2026-11-02

## Conditions

Three fresh local Codex CLI invocations on macOS arm64 used requested model `gpt-6.1-sol`, English replies and the working v0.1.17 entrypoint/core verification package. Each external disposable workspace also contained verification-boundaries, collaboration and requirements references. The prompt asked for a verification plan only and permitted reading relevant sections; no task implementation, installation or service execution was authorized. The CLI process tree was guarded against reading the repository. This is specified-root protection, not complete filesystem/network/credential isolation; internal CLI bypass did not remove that outer rule.

A locally reused minimal CODEX_HOME supplied authentication/provider settings; secrets are excluded from this report. Serving identity and reasoning effort were not independently frozen. The task and evaluator criteria were written before dispatch, but task authors/scorers knew the intended routing outcomes. These are one sample for each of three different tasks, not an old/new comparison or native discovery test. Core was supplied directly, so this does not test whether a host initially chooses the skill.

## Actual outcomes and reads

All three invocations exited zero. Actual command events, not just the final route claim, were inspected:

| Condition | Actual reads | Observable plan and limit |
|---|---|---|
| Copy-only button label | No commands or additional reference reads | Focused diff, existing affected UI check and rendered label/layout inspection; no transaction, SDK or media gate. No implementation/testing was claimed. |
| Split reservation/work transactions | Listed references; read core; listed companion headings; read only lines 5–8, the split-transaction section | Required real database isolation and independent connections, commit-unknown/concurrent ordering, and joint reservation/work/publication inspection. No actual database or recovery execution occurred. |
| Pure SDK serialization | Read core and listed workspace files; did not read companion details | Planned actual serialized-payload and boundary-value checks without transport/live-service gate. Explicitly limited the evidence to serialization, not server acceptance. The task itself clearly excluded dependency/transport changes; this is not autonomous discovery of that boundary. |

The samples demonstrate that the supplied routing was usable for these clear cases and did not force a full companion read. They do not prove preserved behavior for every moved paragraph, reduced token/time cost, improved task quality, or general skill effectiveness. Structural paragraph preservation and repository checks are separate evidence. Raw prompts, events, final outputs, receipts and input manifests remain ignored/local under `evals/results/verification-routing/`.

## Input identities

- `copy`: CLI `codex-cli 0.166.0-alpha.5.1`, prompt SHA256 `3d7da6fbe74d4eeee9a2c497660d32470fb217a392f15ae9c83d36051a7e9992`, exit 0.
- `transaction`: CLI `codex-cli 0.166.0-alpha.5.1`, prompt SHA256 `81768af95a7a7dbdbaf3a5b9ab3c1d4ec211ecdbc8f677605c4fbc2ca2dfc6bb`, exit 0.
- `serialization`: CLI `codex-cli 0.166.0-alpha.5.1`, prompt SHA256 `de962121663980b115aeced01e1b1813449a361cafe4e2d495debf06954517a2`, exit 0.

Frozen reference-file hashes were identical across the three conditions:

- `collaboration.md`: SHA256 `2f1cfc834dc5f1796ddc03a5df0e6d074b576145a8cc1d01b2b261e8c88f7b25`.
- `verification-boundaries.md`: SHA256 `60bdafde408e1d748371a8705b8fd2f544443494e77b2f629e871497a66a24a2`.
- `requirements.md`: SHA256 `f475973f7c106ea746fe9c15047c10e034b3e85a314512555a8a3f586933fd94`.
- `verification.md`: SHA256 `d79b5fd19179978261777aab1eed876d6085d80eb497117db7d8eff0183b9b80`.
