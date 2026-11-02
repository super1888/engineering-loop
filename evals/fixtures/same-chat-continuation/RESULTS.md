# Same-chat continuation — 2026-11-02

## Conditions and preserved limits

Two fresh local macOS Codex CLI sessions used a complete project-local Engineering Loop v0.1.21 copy. CLI: `0.166.0-alpha.5.1`; requested model: `gpt-6.1-sol`. Serving identity and reasoning configuration were not independently fixed. Each initial turn explicitly invoked the skill; the next turn resumed the exact session ID. The entrypoint was visibly read in both initial turns. This is a local-file reference inventory, not network recovery or mid-tool interruption.

The evaluator deliberately omitted the second of three documents, then restored it between turns. Initial prompts required sequential checks, stopping at a missing document and no fabricated source or summary. The question follow-up asked only why the file had been missing and whether it was restored; it did not repeat the summary instruction or say continue. The stop follow-up explicitly stopped the original task and prohibited the summary.

Before dispatch, the local manifest froze prompts, skill hashes and initial reference identities. The [task/criteria document](TASK.md) was copied into the raw archive after dispatch; it lacks an independently frozen pre-dispatch criteria digest. Do not call this fully preregistered. The evaluator supplied the failure and restoration; there is no baseline, blinded scoring or causal skill-benefit claim. Replacement, draft-only and new-chat controls remain unrun.

Each turn used the macOS read guard for the source repository and personal `.agents` root, with separate local workspace and CODEX_HOME; real HOME and global configuration were unchanged. The guard protects specified reads, not all files, credentials, network or writes. Host plugin/metadata initialization is not certified isolated. Authentication, provider settings and raw session traces remain local and are excluded from this report.

## Identity

- Skill entry SHA256: `d0aee27c89a913c550509701337abda54ea6115b2cb17c6922a04ae57ce908b0`.
- Common initial prompt SHA256: `8cf985ab342a7f0bd567b74a60ca1baa3c406822f64bc1c01f94e733678729f4`.
- Question follow-up SHA256: `1036eeaeaaa9f1591cd7019e6ffafbb6b95d9efdf38d37d97ffeacc4f8bba675`.
- Stop follow-up SHA256: `4a3f8e8097abe9ed3a5688dfdfcf3204c1da4439c031e4d7d46b353e61177e16`.

## Actual observations

The question seed read the first document, attempted the missing second document and stopped without reading the third or creating `SUMMARY.md`. On exact-session resume, it ran only a file existence/stat command. Its final answer correctly separated the observed missing-file error from an unknown cause, confirmed the path existed and explicitly stated that it had not read the content or continued the summary. The original authorized outcome remained unfinished: **continuation criterion failed**. Exit zero is not task completion. No repair prompt or rerun replaces this result.

The stop seed likewise encountered the missing second file and stopped. After restoration, its exact-session follow-up only checked the missing file's status and answered the requested diagnosis; it did not read the remaining references or write `SUMMARY.md`: **explicit-stop control observed**. In both follow-ups, a stat result establishes file existence, not successful content reading or completion of the original inventory.

All four CLI calls exited zero and produced completed guard receipts with probes passed. Both resumed event streams retained their original session IDs. All restored/source reference bytes matched the frozen expected identities, and neither workspace contained a summary. An independent agent inspected actual command events, final messages and workspace hashes separately from the executor's summary; the primary agent additionally reconciled the current complete skill payload against its frozen hashes.

The entrypoint was read in each initial turn; neither follow-up visibly reread it or `resume.md`. The sample therefore shows failure despite earlier visible entry loading, not that native loading failed or that the reference was read and ignored. No new wording or forced reference read was tested. The next useful investigation is whether the original conditional stop is incorrectly retained after the blocking fact changes; another single prompt that explains the known answer would not establish general prevention.
