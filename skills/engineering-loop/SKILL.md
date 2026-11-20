---
name: engineering-loop
description: Team delivery entrypoint with a required PMS MCP connection. Identify the current task's project stage, load its guidance and relevant specialist details, then coordinate execution and acceptance. Use for team delivery, task management, uncertain project recovery, or explicit invocation. Standalone explanations outside this workflow stay lightweight.
license: MIT
metadata:
  version: "0.1.28"
---

# Engineering Loop

Coordinate team intent, tasks, specialist work and delivery evidence. Match the user's language. Host permissions and executable controls enforce actions; instructions cannot guarantee correctness or exclusion.

## Connect, locate the stage, then execute

1. **Connect first:** read [connection.md](references/connection.md). Every activated stage and specialist, including analysis-only work, requires successful MCP identity, intended-project and workflow reads. Configuration or tool registration is insufficient. Failed or unknown access blocks downstream work and code/PMS writes; permit only minimal target/connection discovery and diagnosis.
2. **Locate this task's stage:** use its requested deliverable, task and project evidence, not keywords or overall project progress. Modules may be in different stages. Investigate first; ask only a missing outcome/scope decision that changes the next action, not which internal route to use. Combine stages when needed without replaying completed ones.
3. **Read the selected stage:** use the six-stage table below. Apply the common [grill.md](references/grill.md) with that stage's focus before execution: reuse settled decisions and resolve material assumptions and acceptance gaps. Sufficient evidence permits zero user questions; questioning never replaces verification.
4. **Descend only as needed:** follow the stage's links to professional guidance, applicable stack conventions or [specialists.md](references/specialists.md) when selecting a specialist. Preserve all applicable project instructions, required full-document reads and delivery stop points. Read only matching details, not every stage or technology.

Read [pms.md](references/pms.md) for a supplied task reference, task-management request, or work subject to the project's tracking policy. It governs lookup, deduplication, authorized creation/claiming and evidence write-back; the connection gate does not authorize task mutations. Keep credentials and project/member bindings in established configuration.

Reuse connection/challenge evidence only while its session, identity, target and relevant conditions remain valid. Recheck affected facts after errors or material change; a stage change alone does not require identical probes or another interview.

Answer intervening questions, then resume unfinished authorized work. Honor stop, replacement and draft-only limits. Reuse the existing plan and workflow.

| Current task's stage | Stage guide | Main routing signals |
|---|---|---|
| 01 需求分析与确认 | [01-requirements.md](references/stages/01-requirements.md) | Investigate the problem, current behavior and boundaries |
| 02 方案设计与规划 | [02-design.md](references/stages/02-design.md) | Product/technical design, UI and delivery planning |
| 03 开发与联调 | [03-development.md](references/stages/03-development.md) | Implement, diagnose a code defect or integrate systems |
| 04 测试与验收 | [04-testing.md](references/stages/04-testing.md) | Test or assess a deliverable against accepted behavior |
| 05 发布与验证 | [05-release.md](references/stages/05-release.md) | Prepare, deploy or verify a release, including its recovery |
| 06 持续运维 | [06-operations.md](references/stages/06-operations.md) | Maintain a service, diagnose incidents or verify readiness |

Stages classify work; PMS columns describe task state. Selecting a stage does not create a task or authorize the next phase. Each guide indexes entry, inputs, execution, PMS, deliverables and exit/return conditions; stack/template details remain conditional.

Conditional support: [project.md](references/project.md) for missing conventions, [review.md](references/review.md) for concrete review, [collaboration.md](references/collaboration.md) for coordination, [resume.md](references/resume.md) for uncertain recovery, [learning.md](references/learning.md) for a demonstrated lesson or requested retrospective. A support-only task need not launch development or replay the lifecycle.

## Preserve authority and acceptance

Follow intent and existing authorization. Analysis does not authorize implementation; implementation does not authorize publication or destructive data changes. Do not re-ask unchanged authorized actions. Inherit project branch, commit, document, test, configuration and deployment rules; impose no stack, directory, agent count or worktree policy.

Distinguish facts, accepted behavior, proposals and unknowns; investigate conflicts. Make authorized local, reversible engineering choices autonomously. Ask consequential choices affecting behavior, acceptance, permissions or costly rework with alternatives, recommendation, cost and reversibility. Silence is not acceptance. Continue independent authorized work while a decision blocks dependent work.

Keep acceptance independent of implementation. Do not lower thresholds, erase failing assertions or change expectations merely to pass. Record reasons and preserved intent for legitimate corrections. If actual use challenges the design, identify the failed assumption and validate a bounded alternative before changing the agreement.

## Retain evidence and bound effort

Scale effort to uncertainty, impact and reversibility. Reconcile enumerable source items with implemented, excluded and remaining work; a tidy task list does not prove coverage. State other coverage limits. Bind evidence to code, configuration, data and environment; reuse unchanged evidence and rerun affected checks. Distinguish static checks, runtime behavior and user acceptance. A PMS status is not delivery proof.

Re-route for stage transitions, material scope/risk changes, conflicting evidence or recovery, not every message/edit. Do not preload references, repeat effective checks without cause or add reviewers without need. If an attempt yields no new evidence, change the hypothesis or report the blocker instead of repeating speculative patches.

For durable recovery, keep one effective state with scope, decisions, ownership, blockers, evidence/version pointers and next action in the project's existing location. Keep verbose history separate; splitting files cannot erase loaded context or guarantee token savings.

When a finite result and required checks are complete, report results, evidence and limits, then stop. An explicitly ongoing goal continues within its authorization; a completed slice is a checkpoint. Invoke learning for a demonstrated lesson or requested retrospective.
