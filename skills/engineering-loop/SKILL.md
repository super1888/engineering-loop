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

For uncertain resumed work, read [resume.md](references/resume.md). When coordination or ambiguity warrants it, briefly establish **outcome/non-goals; relevant state; settled decisions; unresolved blockers; next slice and evidence**. Reuse an existing plan instead of restating it; keep this in conversation unless durable recovery is needed. Missing facts trigger investigation; material choices trigger questions. Do not ask the user to choose internal skill routes.

Read only the reference for the current unresolved need:

| Need | Reference | Exit evidence |
|---|---|---|
| Connect project rules, reference projects or contributors | [project.md](references/project.md) | Effective conventions, owners, active checks and gaps |
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
- With sufficient evidence, make authorized local, reversible implementation choices autonomously. Necessary engineering work must trace to accepted behavior or project constraints. Present new business behavior or consequential scope/architecture changes with their impact and recommendation; continue independent work that does not depend on the decision.

## Scale effort and retain evidence

Use a light path for clear local changes, a standard path for a complete feature slice, and a deeper path for uncertain or high-impact boundaries. These are effort choices, not mandatory approval stages. A small data migration can need deeper verification than a large text change.

Keep acceptance independent of the implementation. Do not lower a threshold, erase a failing assertion, or rewrite an expectation merely to obtain green checks. Legitimate requirement or test corrections need their reason and preserved intent recorded.

Separate conformance from usefulness. When observed use challenges an accepted design, identify the failed assumption and validate a bounded alternative before changing the effective agreement; do not silently redefine success.

For enumerable work, reconcile the source inventory with implemented, explicitly excluded, and remaining items. A tidy task list is not evidence that all required items were listed. For non-enumerable claims, state the coverage limit.

Evidence belongs to the relevant code, configuration, data, and environment state. Reuse inspectable evidence when those remain unchanged; rerun affected checks when they change. Completion language must distinguish static checks, runtime checks, and user acceptance.

## Bound the agent's own work

Do not preload the lifecycle references or the whole repository. Read an index, then relevant sections. Once information is sufficient for the next authorized action, act; do not search for hypothetical blockers. Reuse settled decisions unless new facts or changed conditions invalidate them.

Re-enter routing only for a stage transition, material scope/risk change, conflicting evidence, or state recovery, not every message or tool call. Do not repeat effective checks without a relevant change, failure, unresolved concern or project-required rerun. Extra planning, reviewers and tooling need a current reason; a small task needs no full plan or retrospective.

If an attempt fails without yielding new evidence, change the hypothesis or investigation, or report the concrete blocker; do not repeat speculative patches. Continue other authorized work when possible. Saving effort never justifies skipping required verification or necessary behavior.

When recovery is needed, keep one effective task state in the project's existing location: scope, decisions, blockers, evidence pointers and next action. Keep verbose history separate. Record relevant versions at handoff. Progressive disclosure does not erase loaded context or guarantee a fixed token cost.

Once the requested outcome and required checks are complete, report the result, evidence, material limits and any required decision, then stop. Do not open an unsolicited optimization cycle. Keep communication proportional; do not narrate every internal checklist or repeat agreed principles. Invoke learning only for a demonstrated lesson or requested retrospective.
