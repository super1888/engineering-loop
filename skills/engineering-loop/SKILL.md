---
name: engineering-loop
description: Team task and delivery entrypoint. Verify PMS MCP access, challenge assumptions, route to the applicable stage or specialist skill, and coordinate task creation, claiming, execution and acceptance. Use for team delivery, task management, uncertain project recovery, or explicit invocation. Standalone explanations outside this workflow stay lightweight.
license: MIT
metadata:
  version: "0.1.22"
---

# Engineering Loop

Coordinate team intent, PMS tasks, specialist work and delivery evidence. Match the user's language. The host's permissions and executable controls enforce actions; instructions alone cannot guarantee correctness or exclusion.

## Connect, challenge, then route

1. **Mandatory MCP gate.** Before executing any routed stage or specialist skill, follow [pms.md](references/pms.md). Require successful authenticated identity, intended project access and actual status reads through the configured PMS MCP. Registered tools, enabled configuration or dependency metadata are insufficient. If any check fails or the target is unknown, stop downstream stage work and code/PMS writes; allow only connection/target discovery and diagnosis. This includes analysis-only routes, which remain read-only after the gate passes.
2. **Challenge every route.** Follow [grill.md](references/grill.md) before the selected stage or specialist, and revisit affected assumptions on material change. Investigate facts and reuse settled decisions; ask consequential unresolved questions until the current slice has a defensible outcome, boundaries and acceptance. Sufficient evidence can pass without asking the user anything. Challenge depth follows risk; questioning does not replace verification.
3. **Route the smallest useful slice.** Identify the outcome and current stage, reuse the project workflow and existing plan, then read only the matching guidance below. Select available specialist skills by outcome, stack and stated scope, using the selection rules in [grill.md](references/grill.md). Keep scope, ownership and acceptance with the coordinator. Do not make the user choose internal routes or load every skill.

Reuse MCP evidence only while the session, identity, target and connection remain valid; recheck affected conditions after changes or errors. A stage change alone does not require another identical probe. Task reading, deduplication, authorized creation/claiming and evidence write-back use [pms.md](references/pms.md); discussion does not authorize creating a task.

Answer intervening questions, then resume unfinished authorized work. Honor stop, replacement and draft-only limits. For uncertain recovery, use [resume.md](references/resume.md) to reconcile outcome/non-goals, current artifacts, settled decisions, blockers, next slice and evidence. Keep the effective state in conversation unless durable recovery is needed.

| Need | Reference | Exit evidence |
|---|---|---|
| Connect project rules or reference projects | [project.md](references/project.md) | Effective conventions, owners, checks and gaps |
| Clarify behavior and tradeoffs | [requirements.md](references/requirements.md) | Accepted examples, boundaries, unresolved items |
| Design a user interface | [ui.md](references/ui.md) | Desktop default; target, states, rendered evidence |
| Implement a slice or diagnose a bug | [implementation.md](references/implementation.md) | Scoped changes and relevant checks |
| Review a concrete diff | [review.md](references/review.md) | Evidence-linked findings and dispositions |
| Verify behavior or integration | [verification.md](references/verification.md) | Passed, failed, unrun, with version/scope |
| Prepare or execute a release | [release.md](references/release.md) | Identified artifact, recovery, smoke evidence |
| Prepare or diagnose operations | [operations.md](references/operations.md) | Impact, tested hypothesis, recovery evidence |
| Preserve a demonstrated lesson | [learning.md](references/learning.md) | Scoped correction and a counterexample |
| Delegate, coordinate or integrate contributions | [collaboration.md](references/collaboration.md) | Ownership, effective agreement, combined evidence |

## Preserve authority and acceptance

Follow user intent and existing authorization. Analysis does not authorize implementation; implementation does not authorize publication or destructive data changes. Do not ask again for an unchanged authorized action. Inherit project branch, commit, document, test, configuration and deployment rules; do not impose a stack, directory, agent count or worktree policy. Keep credentials and team-specific project/person mappings in their established configuration, outside the distributed skill.

Distinguish observed facts, accepted behavior, proposals and unknowns. Investigate conflicts instead of rewriting sources to agree. Resolve authorized local, reversible engineering choices autonomously. Ask only consequential choices affecting behavior, acceptance, permissions or costly rework, with alternatives, recommendation, cost and reversibility. Silence is not acceptance; continue independent authorized work while a decision blocks dependent work.

Keep acceptance independent of implementation. Do not lower thresholds, erase failing assertions or change expectations merely to pass. Record the reason and preserved intent of legitimate corrections. When actual use challenges the design, identify the failed assumption and validate a bounded alternative before changing the agreement.

## Retain evidence and bound effort

Scale effort to uncertainty, impact and reversibility. Reconcile enumerable source items with implemented, explicitly excluded and remaining work; a tidy task list does not establish complete coverage. State limits for non-enumerable claims. Bind evidence to the relevant code, configuration, data and environment; reuse unchanged evidence and rerun affected checks. Distinguish static checks, runtime behavior and user acceptance. A PMS status is not proof of delivery.

Re-enter routing for stage transitions, material scope/risk changes, conflicting evidence or recovery, not every message or edit. Do not preload lifecycle references, repeat effective checks without cause or add reviewers without an unresolved need. When an attempt yields no new evidence, change the hypothesis or report the concrete blocker rather than repeating speculative patches.

For recovery, keep one effective task state with scope, decisions, ownership, blockers, evidence pointers, relevant versions and next action in the project's existing location. Keep verbose history separate; progressive loading cannot erase context or guarantee fixed token cost.

Once a finite result and required checks are complete, report results, evidence and limits, then stop. An explicitly ongoing goal continues within its authorization; a completed slice is only a checkpoint. Invoke learning for a demonstrated lesson or requested retrospective.
