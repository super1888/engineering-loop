---
name: engineering-loop
description: Team delivery entrypoint with a required PMS MCP connection. Identify the current task's project stage, load its guidance and relevant specialist details, then coordinate execution and acceptance. Use for team delivery, task management, uncertain project recovery, or explicit invocation. Standalone explanations outside this workflow stay lightweight.
license: MIT
metadata:
  version: "0.1.36"
---

# Engineering Loop

Match the user's language.

## Route

1. **Connect:** read [connection.md](references/connection.md). Every stage and specialist, including analysis-only work, requires successful MCP identity, intended-project and workflow reads. Configuration or tool registration is insufficient. Failed or unknown access blocks downstream work and code/PMS writes; permit only minimal target/connection discovery and diagnosis.
2. **Locate the stage** from the task's requested deliverable and project evidence, not keywords or overall project progress. Modules may be in different stages. Investigate first; ask only a decision that changes the next action, never which route to use. Combine stages when needed without replaying completed ones.
3. **Read the stage guide** and apply the common [grill.md](references/grill.md) with that stage's focus before execution.
4. **Descend only as needed** through the stage's links to scenarios, stack rules, [templates](templates/index.md) and [specialists](references/specialists.md).

| Current task's stage | Stage guide | Signals |
|---|---|---|
| 01 需求分析与确认 | [01-requirements.md](references/stages/01-requirements.md) | Investigate the problem, current behavior and boundaries |
| 02 方案设计与规划 | [02-design.md](references/stages/02-design.md) | Product/technical design, UI and delivery planning |
| 03 开发与联调 | [03-development.md](references/stages/03-development.md) | Implement, diagnose a code defect or integrate systems |
| 04 测试与验收 | [04-testing.md](references/stages/04-testing.md) | Test or assess a deliverable against accepted behavior |
| 05 发布与验证 | [05-release.md](references/stages/05-release.md) | Prepare, deploy or verify a release, including its recovery |
| 06 持续运维 | [06-operations.md](references/stages/06-operations.md) | Maintain a service, diagnose incidents or verify readiness |

Re-route on a stage transition, material scope or risk change, conflicting evidence or recovery, not on every message or edit.

## Support

| When | Read |
|---|---|
| A supplied task reference, task-management request or tracked work | [pms.md](references/pms.md). The connection gate does not authorize task mutations |
| Project conventions are missing or conflict | [project.md](references/project.md) |
| A concrete review | [review.md](references/review.md) |
| Several contributors or an ongoing goal | [collaboration.md](references/collaboration.md) |
| Leaving work for later, a handoff or uncertain recovery | [resume.md](references/resume.md) |
| A demonstrated lesson or requested retrospective | [learning.md](references/learning.md) |
| This skill's guidance failed or was corrected | [feedback.md](references/feedback.md) |

A support-only task need not replay the lifecycle.

## Always

- Preserve all applicable project instructions, required full-document reads and delivery stop points. Impose no stack, directory, agent-count or worktree policy.
- A stage classifies work; it does not create a task or authorize the next phase. Analysis does not authorize implementation, and implementation does not authorize publication or destructive data changes.
- Answer an intervening question, then resume unfinished authorized work. Honor stop, replacement and draft-only limits.
- Never lower a threshold, delete a failing assertion or change an expectation to make a check pass.
- Claim only what was checked on this version, and report passed, failed and unrun separately. A PMS status is not delivery proof.
