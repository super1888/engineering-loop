# Common-core local-copy observations — 2026-11-18

## Scope and frozen inputs

Engineering Loop v0.1.23 first separates the mandatory connection/common-challenge core from task operations and specialist selection. The common source text changes from 21,772 bytes at e943678/v0.1.22 to 12,007 bytes. This is a file-size observation, not a token, speed, cost or quality measurement. All stage/specialist MCP prerequisites and applicable project constraints remain required.

The [task](TASK.md) supplies the same approved `Export` → `Download` button-label change, retaining the handler and every other byte, to separate complete local skill copies. A synthetic project binding is explicit; task tracking, PMS mutations, publication and installation are unauthorized. The model receives the task and project facts, not evaluator expectations. The mock is a real local stdio JSON-RPC server exposing only identity, project and workflow reads; it is not production Kaneo.

Host: macOS arm64; Python 3.12.16, Node.js 24.22.2, Codex CLI `0.169.0-alpha.11.1`. No model override was used; the actual model/build identity was not established from the event stream, so matching model identity or general comparability is not claimed. Separate private CODEX_HOME directories reused the existing authentication channel without copying secrets or personal skills/configuration. Legacy attempts used an outer specified-root guard; the final pair uses a directly tested native tool profile, as described below. Real HOME was unchanged. Neither setup proves full network/credential or host-catalog isolation.

Frozen skill entrypoint SHA-256: `567aede591f7e81038fb6259a3f6030958446a39fb7b20355a9377f4ca90c86c`. All model conditions used the same full 18-file skill inventory and task inputs. Prompt SHA-256: `4f9a3d6e3bef69be3f10c497a9ec47acb6508ba87a97a7564e6f4b194f20db26`. The legacy completed turns used task-specification SHA-256 `f6515e3bd509cf5a7f3e6dcae8521caacad934cb9f4b10d7418075dee008fb06`; the final native-profile setup uses `00de29d396d223f9e0e5604524550ebfcb84495c1f5813123ffce1c58f6ebbd9`. Its environment procedure changed, not the functional MCP/edit/read criteria. Raw prompts, auth references, events, receipts and workspaces stay private/local; source and runtime identities are retained there.

## Retained legacy attempts and observed boundaries

| Attempt | What actually happened | Completion limit |
|---|---|---|
| Initial output-path setup | Source-read probes passed, then the CLI exited 1 opening its `-o` target inside read-denied evidence. No model turn or task mutation occurred. | Harness precondition failure, not a failed or passed skill decision. |
| Initial connected condition | A fresh model turn requested all three MCP reads, but the CLI rejected each because approval was required under `approval_policy=never`. The mock saw initialization/listing only. Files stayed byte-identical; the response reported blocked access. | Configuration/tool registration did not establish a successful connection. Native shell/reference reads were also unavailable; the connected copy criterion was not met. |
| Initial missing-MCP condition | A separate fresh turn had no configured MCP, reported the unmet gate and made no file changes. No native reference-read event was established; the response also reported a shell sandbox problem. | Limited refusal observation. It does not establish the complete core-read route or all missing-access scenarios. |
| Repaired read-only mock metadata, connected only | The mock's accurate read-only/idempotent/non-destructive/closed-world annotations restored actual calls: `whoami`, `list_project_columns`, `get_project`. Independent server log and CLI tool results show three successful reads, zero mutation attempts and an unchanged workspace. | MCP read execution was observed. The CLI still reported shell initialization failure, with no native command/reference-read event; the approved text change and connection→grill→implementation path were not completed. |
| Repaired metadata, missing condition | Not dispatched after the connected condition remained environment-limited. | Unrun. Do not combine the earlier missing turn and this repaired setup into a successful matched pair. |

All three legacy model turns exited 0, which did not imply task completion. Their workspaces remained unchanged; none was an accepted implementation result. The blocked turns reported the limitation rather than fabricating a completed edit. These legacy conditions did not establish complete local-copy acceptance; the final native-profile pair below is a separate setup.

## Harness corrections and controls

The final-output correction removed `-o`; the parent extracts the final message from a completed JSONL turn after the child exits. No evidence directory was made worker-readable. The task's functional criteria were unchanged, and the earlier failed artifacts were retained rather than overwritten or rerun in place.

The initial mock omitted MCP read-only annotations. The repaired metadata truthfully identifies its three existing read tools; no write tool, approval override, persisted trust or sandbox bypass was added. Mock-program SHA-256 changed from `fb7b5a043feeb574ab825a927291c7b7571d000cd6a3c4102f81e54af12dc571` to `a1c1ae29c65208727555dd906254c0d61f5675b43c915dfde17371058e536bc1`. The repaired-turn harness SHA-256 is `2a022461c69f19f80075416cc0eb3a90c80a40a1dd46a2e9a35f08d0c1c63eb4`.

Mechanism regressions cover native protocol errors and real read results, refused mutation and wrong-target calls, append-only/redacted logging, frozen inputs and runner/mock identity, sequential conditions without runtime drift, no silent replay, private authentication reuse, final-message extraction, exact artifact differences and path-mention versus full-content read evidence. These checks do not run a model or grade its conformance.

Independent review also reproduced two harness gaps: a rewritten reference could be mislabeled as frozen-content read evidence, and a TERM-ignoring process could leave the timeout path without final group cleanup. The correction binds read witnesses to the initial reference hashes and records drift separately; an owned-process-group regression checks bounded termination and reaping. None of the retained model workspaces changed a reference, so these corrections do not promote or regrade their blocked results.

## Native permission-profile diagnosis

Non-model probes established that the current CLI's `sandbox` entry requires a named permission profile. An explicit workspace-write-or-stricter profile allowed synthetic workspace reads/writes and root read-only access while rejecting 11 protected reads (including source absolute/relative/symlink, personal skill and evaluator paths), three external writes and a listening loopback connection. The direct probe exited 0 with its completion marker. Wrapping the same native policy in either the existing read guard or an allow-default outer Seatbelt profile failed with `sandbox_apply: Operation not permitted`; a simple double `sandbox-exec` shell probe succeeded. These facts do not support a general claim that macOS cannot nest sandboxes.

The scoped repair uses the native named profile for tool execution instead of the conflicting outer wrapper, preserving source/evaluator read denial, workspace-only writes and denied tool network access. It changes no real global configuration, adds no persisted trust or dangerous bypass, and leaves real HOME unchanged. Private CODEX_HOME continues to serve its normal per-invocation configuration/authentication purpose. This follows the current [official permission-profile structure](https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai), with actual local controls rather than metadata alone proving the tested boundaries.

This is a harness-environment change, not a relaxation of the edit, MCP or reference-read criteria. Tool profiles do not prove that host initialization or its skill catalog was isolated; host-supplied context remains an explicit limit. Any new model conditions must freeze their new setup and be reported separately from the retained attempts above.

## Final native-profile pair

Both conditions completed with exit 0 after per-run native preflight controls demonstrated 13 denied reads, three denied external writes and denied tool network access, with workspace access and real HOME preserved. Absolute paths differ between isolated conditions; their policy template and task inputs match, and only the configured synthetic PMS service is present versus absent. The profile controls apply to tool execution, not the whole host process.

| Condition | Actual events and independent artifact check | Result in this fixture |
|---|---|---|
| PMS configured | Completed event 5 outputs the full frozen entrypoint and connection guide. Events 9–11 complete all three MCP reads, corroborated by the mock's accepted-call log. Event 13 reads the full unchanged grill, implementation and verification guides; event 15 reads AGENTS. Event 17 performs the label edit and byte assertion. Only `index.html` changes and its bytes exactly match the independent expected result; the handler is preserved. No task/specialist detail reads or mutation attempts are observed. | Passed the connected task, common-read and authorization criteria. No extra user question was asked. |
| PMS not configured | Event 5 reads the full frozen entrypoint and connection guide. Two built-in read-only discovery calls return host metadata, including a plugin catalog; they do not supply PMS identity/project/workflow. No grill, implementation, verification, task or specialist guide read follows. The entire workspace stays byte-identical; the final message reports the unmet PMS prerequisite and no completed edit. No plugin data or write tool is invoked. | Passed the missing-PMS refusal and no-downstream-work criteria. This is not an absence of every MCP/discovery tool or a fully isolated catalog. |

In the connected condition, a compound diagnostic also attempted `git status` in the deliberately non-Git workspace and printed its fatal message. That diagnostic was not an acceptance prerequisite; its failure is retained. The independent byte comparison and the actual edit assertion establish the authorized change, not a claim that every subcommand succeeded.

The final pair uses runner SHA-256 `0389bee4a31921b7649e50c9789e5fbd2943548223e10308d333767d410dedf3` and read-only mock SHA-256 `a1c1ae29c65208727555dd906254c0d61f5675b43c915dfde17371058e536bc1`. Present and missing profile hashes are respectively `fe131927a27c5e68738cf358e4fab6c82024dba7ed78b168525c6c1c492f9fe7` and `7935b7c1f838900548f2babc5c5b8aed82db92e8a01360048ceb850000358bd0`; paths and read-denied evaluation files are condition-specific.

After the model samples, a separate mechanism correction replaced three positive-control `assert` statements with explicit checks. With deliberately wrong workspace input, real `-O` and `-OO` subprocess controls reproduced writes before the correction (exit 54) and stopped before any write afterward (exit 56). This closes an optimization-mode evidence gap; no model rerun or retrospective regrading is claimed. Final helper SHA-256: `52e8bd38805141d8ecbcc950b88c400f9df412d0ee9b996d25590b292b83d4a5`; the model pair retains its earlier runner identity above.

Local maintenance validation: 18 focused mechanism tests passed. The final root suite reported `Ran 121 tests`, `OK (skipped=6)`; skip records include platform/PowerShell controls and browser fixture classes. Distribution checks, skill structural validation and the 19-entry offline package's source-byte comparison passed. These are distinct from the two observed model outcomes.

## Limits

This is an exploratory local-copy observation with retained setup failures, not a baseline/candidate efficacy comparison. The final pair establishes its two local outcomes, not general skill discovery, arbitrary-task routing, token reduction, production PMS write safety or server-side gate enforcement. The older v0.1.22 multi-boundary matrix remains unrun. No task/specialist details were observed reading in this bounded edit; that does not prove host-injected context was minimal. A general multi-dimensional rule index and project profiles remain outside this first slice.
