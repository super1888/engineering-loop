---
name: engineering-loop
description: Team task and delivery entrypoint. Verify PMS MCP access, challenge assumptions, route to the applicable stage or specialist skill, and coordinate task creation, claiming, execution and acceptance. Use for team delivery, task management, uncertain project recovery, or explicit invocation. Standalone explanations outside this workflow stay lightweight.
license: MIT
metadata:
  version: "0.1.23"
---

# Engineering Loop

Coordinate team intent, tasks, specialist work and delivery evidence. Match the user's language. Host permissions and executable controls enforce actions; instructions cannot guarantee correctness or exclusion.

## Connect, challenge, then route

1. **Connect first:** read [connection.md](references/connection.md). Every activated stage and specialist, including analysis-only work, requires successful MCP identity, intended-project and workflow reads. Configuration or tool registration is insufficient. Failed or unknown access blocks downstream work and code/PMS writes; permit only minimal target/connection discovery and diagnosis.
2. **Challenge the slice:** read the common [grill.md](references/grill.md). Investigate facts, reuse settled decisions and resolve material assumptions and acceptance gaps. Sufficient evidence permits zero user questions; questioning never replaces verification.
3. **Read matching guidance:** identify the outcome, stage, affected paths and boundaries. Preserve all applicable project instructions, including required full-document reads and delivery stop points; filtering details cannot waive them. Use the stage table below, or [specialists.md](references/specialists.md) when selecting/delegating an available specialist. Read only matching details, not the entire lifecycle.

Read [pms.md](references/pms.md) for a supplied task reference, task-management request, or work subject to the project's tracking policy. It governs lookup, deduplication, authorized creation/claiming and evidence write-back; the connection gate does not authorize task mutations. Keep credentials and project/member bindings in established configuration.

Reuse connection/challenge evidence only while its session, identity, target and relevant conditions remain valid. Recheck affected facts after errors or material change; a stage change alone does not require identical probes or another interview. Do not ask the user to choose internal routes.

Answer intervening questions, then resume unfinished authorized work. Honor stop, replacement and draft-only limits. For uncertain recovery, use [resume.md](references/resume.md) to reconcile outcome/non-goals, artifacts, settled decisions, blockers, next slice and evidence. Reuse the existing plan and workflow.

| Need | Reference | Exit evidence |
|---|---|---|
| Connect project rules or references | [project.md](references/project.md) | Effective conventions, owners, checks and gaps |
| Clarify behavior and tradeoffs | [requirements.md](references/requirements.md) | Accepted examples, boundaries, unresolved items |
| Design a user interface | [ui.md](references/ui.md) | Desktop default; target, states, rendered evidence |
| Implement a slice or diagnose a bug | [implementation.md](references/implementation.md) | Scoped changes and relevant checks |
| Review a concrete diff | [review.md](references/review.md) | Evidence-linked findings and dispositions |
| Verify behavior or integration | [verification.md](references/verification.md) | Passed, failed, unrun, with version/scope |
| Prepare or execute a release | [release.md](references/release.md) | Identified artifact, recovery, smoke evidence |
| Prepare or diagnose operations | [operations.md](references/operations.md) | Impact, tested hypothesis, recovery evidence |
| Preserve a demonstrated lesson | [learning.md](references/learning.md) | Scoped correction and a counterexample |
| Coordinate or integrate contributions | [collaboration.md](references/collaboration.md) | Ownership, agreement, combined evidence |

## Preserve authority and acceptance

Follow intent and existing authorization. Analysis does not authorize implementation; implementation does not authorize publication or destructive data changes. Do not re-ask unchanged authorized actions. Inherit project branch, commit, document, test, configuration and deployment rules; impose no stack, directory, agent count or worktree policy.

Distinguish facts, accepted behavior, proposals and unknowns; investigate conflicts. Make authorized local, reversible engineering choices autonomously. Ask consequential choices affecting behavior, acceptance, permissions or costly rework with alternatives, recommendation, cost and reversibility. Silence is not acceptance. Continue independent authorized work while a decision blocks dependent work.

Keep acceptance independent of implementation. Do not lower thresholds, erase failing assertions or change expectations merely to pass. Record reasons and preserved intent for legitimate corrections. If actual use challenges the design, identify the failed assumption and validate a bounded alternative before changing the agreement.

## Retain evidence and bound effort

Scale effort to uncertainty, impact and reversibility. Reconcile enumerable source items with implemented, excluded and remaining work; a tidy task list does not prove coverage. State other coverage limits. Bind evidence to code, configuration, data and environment; reuse unchanged evidence and rerun affected checks. Distinguish static checks, runtime behavior and user acceptance. A PMS status is not delivery proof.

Re-route for stage transitions, material scope/risk changes, conflicting evidence or recovery, not every message/edit. Do not preload references, repeat effective checks without cause or add reviewers without need. If an attempt yields no new evidence, change the hypothesis or report the blocker instead of repeating speculative patches.

For durable recovery, keep one effective state with scope, decisions, ownership, blockers, evidence/version pointers and next action in the project's existing location. Keep verbose history separate; splitting files cannot erase loaded context or guarantee token savings.

When a finite result and required checks are complete, report results, evidence and limits, then stop. An explicitly ongoing goal continues within its authorization; a completed slice is a checkpoint. Invoke learning for a demonstrated lesson or requested retrospective.
