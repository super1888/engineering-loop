# Coordinate implementation, specification and verification

Use when authorized delegated tasks need coordination, concurrent contributors need ownership or contract-change reconciliation, or temporary branches/worktrees need integration and cleanup. Delegate only when available, authorized and useful. Roles are responsibilities, not a required agent count: a coordinator, implementer and verifier may suffice; separate specification and test work only when their scope justifies it. A small local task needs no agent team or coordination service.

## Assign bounded ownership

| Responsibility | Owns | Authority boundary |
|---|---|---|
| Coordinator | Effective agreement, task boundaries, dispute routing and integrated acceptance | Resolves engineering choices within existing authority; routes consequential business or scope decisions to the authorized owner |
| Implementer | Scoped code, self-checks and evidence of specification problems | Does not silently change accepted behavior or weaken acceptance |
| Specification reviewer (SDD) | Alignment with effective requirements and architecture; maintenance of accepted specification changes | Can challenge both code and specification, but cannot invent business policy |
| Test verifier (TDD where useful) | Expected outcomes from accepted examples, boundary tests and integrated behavior | Does not derive correctness solely from the implementation or rewrite expectations merely to pass |

Give each contributor only the relevant agreement/version, paths and contracts owned, prerequisites, expected result and checks. Agree who owns shared files and integration before overlapping work. Serialize conflicting writes, including specification/test files and shared build or Git state, according to project policy. In a shared checkout, check the staged paths immediately before committing; a path-limited `git add` does not isolate a later commit if another contributor stages files meanwhile. Coordinate the index or use an isolated index when that race is real. Do not assign two agents the same repair without a concrete reason.

For a specialist assignment, name the affected stack and applicable project skill or maintained reference when available. A role label alone does not supply project expertise. Let a contributor identify a narrower relevant skill when the environment exposes one, but keep the effective agreement, file ownership and acceptance with the coordinator. Do not load every available skill or add contributors merely to give each skill an owner.

## Carry an ongoing goal across bounded slices

Distinguish a finite assignment from an explicitly ongoing goal. Give the contributor the relevant outcome, exclusions, authority, project/skill paths, owned slice, checks and continuation condition. Creating a task proves dispatch, not implementation or verification. Keep its returned identity and reconcile the resulting artifacts at each meaningful checkpoint.

For an ongoing goal, preserve the full outcome while finishing verifiable slices. A verified slice or commit is a checkpoint, not goal completion. After checking its evidence, proceed to the next supported slice within the existing scope. If the contributor is terminal and work remains, continue through an authorized follow-up or perform the next slice; if a specific handle remains live, follow the monitoring guidance below. An ongoing goal alone does not authorize new tools, schedulers, external messages, publication or unrelated cleanup.

A continuation or scope correction supersedes a conflicting first-round stopping instruction. Send affected contributors the relevant delta when authorized and check their next artifacts against it; they may retain already-loaded guidance. On an explicit pause, stop dispatching new slices and relay the pause to authorized active contributors, preserving unfinished work and evidence. Do not turn a finite completed request into an ongoing loop or mark an unfinished paused goal complete.

## Resolve disagreements with evidence

An implementer or reviewer challenging a specification provides the effective rule, a concrete conflicting fact or usage scenario, consequence, proposed correction and affected work. The coordinator distinguishes:

- Stale text or a check defect with an established authoritative answer: correct within scope and retain the basis; do not re-ask a settled decision.
- A different implementation preserving accepted behavior: decide within existing engineering authority.
- An unresolved contradiction or consequential change to business behavior, acceptance or architecture: use [requirements.md](requirements.md) to investigate and obtain the appropriate decision, with alternatives and impact.

Documentation is not immune to correction, and implementation convenience is not evidence that it is wrong. Agent agreement or majority vote does not settle a disputed requirement. Pause only work dependent on the unresolved decision; continue independent authorized work. If investigation adds no evidence, report the concrete decision/blocker rather than cycling between speculative implementation and review.

## Keep active work on the effective agreement

Reuse the project's tracker or task state for the effective agreement/version, ownership, unresolved decisions and evidence pointers. An accepted change records what it supersedes and sends the relevant delta to affected contributors. Identify impacted code, tests and prior evidence; revise or stop obsolete dependent assignments before their results are integrated. Reading a message is not proof of adaptation: check that returned artifacts use the effective agreement. Do not broadcast whole histories or make every agent reload all references.

An existing file or message can be sufficient. Propose a shared coordination service only for demonstrated needs, with appropriate authorization; it is not a prerequisite. If used, distinguish advisory ownership from enforced writes and handle stale reservations. Notifications do not replace reconciliation.

When monitoring a contributor, an active conversation label or quiet timeout is not proof that a command is still running or has stopped. Inspect its specific job or session handle and relevant artifacts; wait on a confirmed live handle, otherwise state uncertainty only when actionable and defer to the next meaningful checkpoint instead of polling or nudging repeatedly. Do not restart solely because observation expired.

## Replace a conversation without duplicating its work

When the user authorizes context handoff, reconcile the current repository and latest terminal report before relying on an older ownership record. A completed contributor may have committed or frozen work after that record was written. Preserve its unique artifacts and evidence; do not replay the old assignment merely because the record still says active. Treat expired resource deadlines as historical until current handles or resource observations establish their state.

Carry a short effective handoff into a fresh conversation: outcome, authority, source revision, owned changes, evidence, unresolved work and any live handles. Confirm the predecessor has stopped conflicting writes and the successor has checked the handoff before transferring ownership and continuing. A live command can survive the conversation: retain its handle and custodian rather than killing or restarting it for context cleanup. Retire the old conversation only within the user's authorization and at a safe boundary. Finite completed tasks need no replacement.

Prefer compact status and terminal summaries when reading contributor history. A small turn count may still return an entire long tool transcript; select the needed fields before displaying it and fetch raw evidence only for an unresolved acceptance item. Conversation replacement preserves the goal, not every historical message.

## Review meaningful boundaries

Review the first representative slice before replication, a material shared-contract change, an explicit specification conflict, or the integrated result. Select checkpoints by current risk rather than reviewing every edit or continuously polling unfinished code. Findings name the relevant agreement and identifiable code state, trigger, consequence and evidence. Code changes invalidate only affected findings and checks; reuse still-valid results.

For critical behavior, establish test expectations from accepted scenarios before or alongside implementation where useful. A verifier may inspect code for risks, but expected results need an independent basis. Preserve legitimate alternative implementations and exceptions. Source conformance, observable behavior and task usefulness require different evidence; use [verification.md](verification.md).

The coordinator reconciles findings, accepted specification changes and affected contributor results, then verifies combined behavior at an identifiable integrated state. Separate green checks or a clean merge are insufficient. Report passed, failed and unrun evidence and any remaining decision. Stop when a finite requested result and required checks are complete; ongoing goals follow the continuation condition above. Extra reviewers need a current unresolved reason.

## Retire temporary branches after integration

When temporary branches or worktrees feed one delivery, identify the target and account for each contribution before calling the result complete. Show that its required work is present by ancestry, an equivalent patch, or evidence that a later change supersedes it; integrate unique required work and verify the resulting target state. Retain any branch with unique unintegrated work.

After integrated verification, remove only safe, agent-created temporary worktrees and local refs, plus remote refs when authorized. Preserve uncommitted or untracked work and checkouts still in use. Integration and cleanup do not authorize a push or deployment.
