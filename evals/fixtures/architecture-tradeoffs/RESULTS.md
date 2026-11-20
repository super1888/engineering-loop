# Conditional architecture challenge smoke — v0.1.28

On 2026-11-20, three fresh Codex CLI 0.169.1 contexts on macOS arm64 used the same frozen skill and read-only synthetic PMS. Each received its own request and maintained `PROJECT.md` from the frozen acceptance. The prompts omitted expected routes and guide names. The default model was used, with serving model/build identity unknown. [Acceptance specification](TASK.md)

A private adapter reused the native copy-edit mock, preflight and event capture, and froze the supplemental acceptance separately from the historical acceptance. It denied access to the evaluator area, other cases and earlier evidence. All preflights passed workspace/root reads, 18 protected-read denials, three outside-write denials and tool-network denial with `HOME` unchanged. Raw artifacts, the wrapper and auth references remain private. [Historical helper protocol](../core-route/TASK.md)

## Observed routes and outcomes

All three cases returned the full frozen connection guide at event 5, then completed the three synthetic MCP reads at events 9–11. No explicit `SKILL.md` read appeared in the captured tool output, and host-provided entrypoint provenance is unknown. The table describes completed content reads and the observed decision behavior.

| Case | Reads after the gate | Outcome against frozen criteria |
|---|---|---|
| A, sufficient evidence | Event 13 returned full `02-design.md` and `grill.md`. Event 15 returned the maintained note. Event 17 returned full `architecture.md`. | Recommended the existing application, relational store and worker. Used the known roles, customer and user counts, ordinary and peak loads, separate 150 ms and 34 s rehearsal results, and matched first-year estimates of USD 8,200 versus USD 22,840. Challenged the simpler design with possible queue/database contention and interrupted-work retry behavior, proposed acceptance checks and set measurable conditions to reopen the decision. Closed the recommendation without a repeated interview. |
| B, material uncertainty | Event 13 returned the note, full `02-design.md` and `grill.md`. Event 15 returned full `architecture.md`. | Used a hypothetical concurrency cap to challenge extrapolation from warm single-job times. Retained the observed 165 ms acknowledgement, compared USD 7,800 versus USD 11,800 at the same horizon and proposed a separately authorized 10-minute, 24-job/minute burst validation with both latency limits and decision rules. It kept the tier commitment open pending test results. |
| C, settled desktop design | Event 13 returned the note, full `02-design.md` and `grill.md`. Event 15 returned full `ui.md`. No architecture guide read appeared. | Delivered the existing loading, empty and error states, keyboard retry behavior, and a proposed focus transition after a successful retry. No generic capacity/cost checklist or extra design interview appeared. It left rendered acceptance for a future authorized preview. |

Manual inspection confirmed C's full stage and challenge outputs despite the command's brace-expanded paths. All three CLIs exited zero with a completed output. Each mock log contains exactly the three required accepted reads, and all 77 files per workspace matched their frozen before hashes. No attempted mutation or opposite route was observed. Each case met its route, observed decision and scope criteria. The rehearsals and prices in these cases were synthetic maintained inputs. There was no real service/performance test, cost measurement, procurement, implementation or deployment. The helper's unused missing-MCP conditions and B's future validation and subsequent answer or commitment remain untested. The observations establish those case outcomes, with general efficacy and cross-host behavior unverified.

## Frozen input identities

The complete current package matched the shared 74-file skill inventory. The inventory digest uses a compact, key-sorted UTF-8 JSON mapping of relative paths to per-file SHA-256 values.

| Input | SHA-256 |
|---|---|
| Shared skill inventory | `b6f68737f050e2e32f47108c717c2e33264b38502bc16c9b8c4e8f727465a4a4` |
| `SKILL.md` | `23f3bad8359512c181c1a2a9dd24f16813422a1cd4b67a06b0a9c85ca60f39ce` |
| `architecture.md` | `96f36aa83f3e29cb7bd9dc538bde63973a61f3c79b81ae217984cad580d04019` |
| Supplemental acceptance | `23bcb0112d23333f21b8a53f24c656aec3575877543980858437a9b96aa4a99a` |
| Historical helper acceptance | `00de29d396d223f9e0e5604524550ebfcb84495c1f5813123ffce1c58f6ebbd9` |
| Unchanged helper | `52e8bd38805141d8ecbcc950b88c400f9df412d0ee9b996d25590b292b83d4a5` |
| A prompt | `ff6c1107ba6ca7fb67d67a4e242068005ae931c045756f5e893bd49be79be8d6` |
| A note | `edd6ba04bf8618df023e938313929e61ddbff14081837ed972bac58642cb121d` |
| B prompt | `52f8f2899483a729d3e70651e2bdaefb7ea6bd475fcc5386b93e53b9a5bb0e89` |
| B note | `13dfafdd26bdaf60f97a539ee13f20d6e74f0d025271d5c5f9a0b4e1b386d8f4` |
| C prompt | `7c4d2793dcf203f55f01d3be536f74c64136755e3e5f5ee7107edc830550ed2e` |
| C note | `25f77c63b1b47cbe43a373e6c7dab9b6d88b641dfd1a770c184e0ab9ee2899ad` |
