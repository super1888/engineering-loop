# Native Codex discovery — frozen task

Three fresh CLI invocations use a complete unmodified v0.1.18 skill copy at each external workspace's `.agents/skills/engineering-loop`. No skill body or AGENTS instruction is supplied. HOME remains unchanged; each independent CODEX_HOME contains no personal skill or AGENTS instruction. The real personal `.agents` root and repository are denied by `evals/read_guard.py`. Only minimal provider/auth configuration is reused. Raw local evidence is ignored.

## Inputs and acceptance (frozen before dispatch)

1. **Implicit uncertain resume:** “Resume this work. The previous session ended unexpectedly and I do not know whether its last update is complete. Inspect the workspace, reconcile the saved state against the current implementation and checks, then report what is established, what remains uncertain, and the next bounded step. Do not change files.” Workspace contains a stale checkpoint saying pending plus a current implementation and executable check. Pass requires tool evidence reading project SKILL.md and references/resume.md, checking actual state and preserving the read-only boundary; no user prompt names the skill.
2. **Explicit:** Same workspace/task, prefixed `$engineering-loop`. Pass requires tool evidence reading the project SKILL.md and resume reference and reconciling current state without changes.
3. **Light control:** “Change the button label from Export to Download in index.html. Keep behavior and other content unchanged.” Pass requires exactly that local edit, no resume reference or elaborate workflow. Native discovery/catalog exposure itself is allowed.

The fixture checkpoint says a label-format correction was pending; `label.py` already returns `item:<value>` and `check.py` asserts that contract. Resume acceptance permits reporting it complete with evidence or a justified remaining uncertainty; it does not require invented implementation work. Skill package and prompt hashes, actual model/configuration, CLI identity and guard receipts are frozen in the local manifest before dispatch. No runtime or efficacy claim across other hosts follows from these single samples. Scoring is non-blind.
