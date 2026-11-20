# Six-stage routing smoke results — v0.1.27

On 2026-11-20, each frozen revision was assessed in two fresh local Codex CLI 0.169.1 contexts on macOS arm64 using the same synthetic service observations. O1 requested read-only incident triage after the cutover closed. O2 requested a continue/hold decision for the pending cutover. The prompts omitted expected stage and guide names. Both used the default model configuration, with serving model/build identity unknown. [Acceptance specification](TASK.md)

The initial revision exceeded the distribution entrypoint budget at 7,017 bytes. Shortening the 05 and 06 signal text brought it to 6,954 bytes and passed distribution validation. The final package differs from the initial one only in `SKILL.md`. The final pair reused the original prompts, snapshot, mock and supplemental acceptance to check the final candidate, while retaining the initial pair's results.

Both revisions reused the existing native copy-edit helper's read-only Kaneo mock, permission preflight and evidence capture. A private adapter provided the request and project instructions, froze the supplemental acceptance alongside the historical acceptance, and added read-denial rules for the other case, unused branch, manifests and wrapper. The final adapter also isolated the initial evidence directory. Actual preflights passed workspace/root reads, 15 protected-read denials per initial case and 16 per final case, three outside-write denials and tool-network denial with `HOME` unchanged. The adapter, raw events, manifests and auth references remain private. [Historical helper protocol](../core-route/TASK.md)

| Revision and case | Ordered evidence | Task result |
|---|---|---|
| Initial O1 | Event 5 returned the full entrypoint and connection guide. After the three successful synthetic MCP reads at 9–11, event 13 returned `06-operations.md` and `grill.md`, then event 15 returned `operations.md` and `verification.md`. | Read-only triage identified the growing backlog and proposed discriminating checks. |
| Initial O2 | Event 5 returned the connection guide. After MCP events 9–11, event 13 returned `05-release.md` and `grill.md`, then event 15 returned `release.md` and `verification.md`. | The observed build was `demo.41`. The queue criterion failed and the response recommended holding. |
| Final O1 | Event 5 returned the connection guide. After MCP events 9–11, events 13, 15, 17 and 19 returned full frozen `grill.md`, `06-operations.md`, `operations.md` and `verification.md`, respectively. | Reported queue growth and aging despite HTTP 200, kept the cause open, and proposed read-only checks for arrivals, completion rates and worker/job history. |
| Final O2 | Event 5 returned the connection guide. After MCP events 9–11, event 13 returned full frozen `05-release.md` and `grill.md`, then event 15 returned full `release.md` and `verification.md`. | Confirmed `demo.41` and recommended holding because six-minute oldest job age failed the two-minute criterion despite HTTP 200. The cause remained open. |

All four cases met the task-specific gate, selected-reference, outcome and read-only authority criteria. Each mock log contains only the three required accepted reads. Each CLI exited zero with a completed turn, and all 75 files per workspace matched their frozen before hashes. Completed tool events showed no out-of-scope actions or opposite stage guide reads. Manual inspection of completed outputs confirmed the frozen full texts when shell brace expansion escaped the helper's literal-path index. An explicit entrypoint read was observed only in initial O1. Entrypoint-load provenance for the other three contexts remains unknown. O3–O5 and the helper's unused missing-MCP branches remain unrun. Production access, actual deployment, recovery, PMS writes and general selection reliability remain unverified.

## Frozen input identities

| Input | SHA-256 |
|---|---|
| Initial 73-file skill inventory | `93e10914901ae9c0079d4bfb033680263eded5f6fc40c99ad973fda2835ee275` |
| Final 73-file skill inventory | `c3ed2f46ef5e216be606b23a4d20fd883d7e66e2e3eeaef8e594c7e665d86212` |
| Initial `SKILL.md` | `96688dab8de2b551344ea86fb5e79a974c485d8dea313ee2b689406b0de50423` |
| Final `SKILL.md` | `e683941e87d8e54d8817272a9de2f8faae1e2d54c0d22959236d94e1a07c8798` |
| `05-release.md` | `23a077573c86653844bad73c5ae3468b344bf0a26ab906c91ba7627c6a1e8eda` |
| `06-operations.md` | `70471ca5bca28e372be3b8abaeb05a9aed8e174e4b789a3c39c5e9adc41368c8` |
| Shared project instructions and snapshot | `b91796c5b40bc0a0b1f59b036bc1a88e4f293c1f075179875e7f96eeba24e4c4` |
| O1 prompt | `5103a63801de70f9bc4bc9828e6340b0e5b27693d22a80f0168d3f614f682e9b` |
| O2 prompt | `e2d7e30301f2f220419893f62a1671449bc7202f76d879955eadc335bb6e5782` |
| Supplemental acceptance | `e4c1376dfe3efed69dfdce791e2ca285db57fbf6d814dc9aa5f6597a858a2e5a` |
| Historical helper acceptance | `00de29d396d223f9e0e5604524550ebfcb84495c1f5813123ffce1c58f6ebbd9` |
| Unchanged helper | `52e8bd38805141d8ecbcc950b88c400f9df412d0ee9b996d25590b292b83d4a5` |

The inventory digest hashes a compact, key-sorted UTF-8 JSON mapping from relative paths to per-file SHA-256 values. Host initialization and catalog provenance remain outside the native tool preflight's coverage.
