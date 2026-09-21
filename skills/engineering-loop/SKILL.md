---
name: engineering-loop
description: Coordinate a bounded engineering change across requirements, implementation, review, verification, and delivery. Use when explicitly requested, when resuming work with uncertain state, or when a cross-boundary change needs unresolved decisions coordinated. Do not activate for explanations, routine local edits, or an already-scoped stage handled by project guidance.
license: MIT
metadata:
  version: "0.1.0"
---

# Engineering Loop

Keep human decisions, implementation, and evidence aligned through one bounded change. Match the user's language. This skill guides decisions; tool permissions and executable checks enforce boundaries.

## Enter once; route only when needed

Identify the requested outcome and current stage. Reuse established decisions and the project's workflow. A named stage request enters that stage directly; do not restart discovery. A routine edit with sufficient context proceeds through the existing local workflow without extra ceremony.

For uncertain resumed work, read [resume.md](references/resume.md). For new or materially changed work, make a brief start card using available facts: **outcome/non-goals; relevant state; settled decisions; unresolved blockers; next slice and evidence**. Keep it in conversation unless durable recovery is needed. Missing facts trigger investigation; material choices trigger questions. Do not ask the user to choose internal skill routes.

Read only the reference for the current unresolved need:

| Need | Reference | Exit evidence |
|---|---|---|
| Connect a new project or missing cross-boundary rules | [project.md](references/project.md) | Relevant sources, owners, active checks and gaps |
| Clarify behavior and tradeoffs | [requirements.md](references/requirements.md) | Accepted examples, boundaries, unresolved items |
| Implement a slice or diagnose a bug | [implementation.md](references/implementation.md) | Scoped changes and relevant checks |
| Review a concrete diff | [review.md](references/review.md) | Evidence-linked findings and dispositions |
| Verify behavior or integration | [verification.md](references/verification.md) | Passed, failed, unrun, with version/scope |
| Prepare or execute a release | [release.md](references/release.md) | Identified artifact, migration/recovery, smoke evidence |
| Diagnose a running service | [operations.md](references/operations.md) | Impact, tested hypothesis, recovery evidence |
| Preserve a demonstrated lesson | [learning.md](references/learning.md) | Scoped correction and a counterexample |

## Keep authority and scope explicit

- Follow the user's intent and existing authorization. Analysis does not authorize implementation; implementation does not silently authorize publication or destructive data changes. Do not ask again for an action already authorized within unchanged scope.
- Inherit repository rules for branches, commits, documentation, tests, configuration, and deployment. Do not impose a directory, stack, multi-agent setup, worktree, or parallel build policy.
- Separate observed facts, approved target behavior, proposals, and unknowns. When they conflict, investigate; do not pick a convenient source and rewrite the others to agree.
- Ask only decisions that change business behavior, acceptance, permissions, or costly rework. Batch independent decisions whose prerequisites are settled. Show alternatives, recommendation, cost, and reversibility. Silence is not acceptance of a required choice.
- Continue authorized, bounded, reversible work with adequate evidence. If new scope or a material decision appears, present the concrete difference; continue independent work that does not depend on it.

## Scale effort and retain evidence

Use a light path for clear local changes, a standard path for a complete feature slice, and a deeper path for uncertain or high-impact boundaries. These are effort choices, not mandatory approval stages. A small data migration can need deeper verification than a large text change.

Keep acceptance independent of the implementation. Do not lower a threshold, erase a failing assertion, or rewrite an expectation merely to obtain green checks. Legitimate requirement or test corrections need their reason and preserved intent recorded.

For enumerable work, reconcile the source inventory with implemented, explicitly excluded, and remaining items. A tidy task list is not evidence that all required items were listed. For non-enumerable claims, state the coverage limit.

Evidence belongs to the relevant code, configuration, data, and environment state. Reuse inspectable evidence when those remain unchanged; rerun affected checks when they change. Completion language must distinguish static checks, runtime checks, and user acceptance.

## Bound context and loops

Do not preload the lifecycle references or the whole repository. Read an index, then relevant sections. Reuse unchanged material. Keep one effective task state in the project's existing location: scope, decisions, blockers, evidence pointers, next action. Keep verbose logs and historical alternatives outside the active summary.

Re-enter routing only for a stage transition, material scope/risk change, conflicting evidence, or state recovery. Do not repeat routing on each message, file edit, or tool call. On repeated failure without new evidence, stop that attempt and change hypothesis or report a concrete blocker; do not accumulate speculative patches.

At a useful handoff, record the effective state and referenced versions. Progressive disclosure reduces unnecessary reads; it does not erase already-loaded conversation content or guarantee a fixed token cost.

Finish with the outcome, its evidence, unresolved limitations, and any required decision. Invoke learning only for a demonstrated lesson, not to add a rule after every edit.
