# Design boundaries

One team task/delivery router with five stage entries, focused references, and project-owned artifacts. Routed work requires a verified PMS MCP connection; select the task's stage, then apply its evidence-based challenge and relevant professional guidance. The PMS stores shared task facts while the repository retains its engineering system and artifacts.

## Five-stage navigation

The v0.1.24 directory distinguishes project stages from professional details and cross-cutting support:

| First-level stage | Selected guidance |
|---|---|
| 01 Requirements analysis and confirmation | [Requirements entry](../skills/engineering-loop/references/stages/01-requirements.md) |
| 02 Solution design and planning | [Design entry](../skills/engineering-loop/references/stages/02-design.md), including UI and architecture/planning references |
| 03 Development and integration | [Development entry](../skills/engineering-loop/references/stages/03-development.md), including frontend/backend implementation, self-checks and integration |
| 04 Testing and acceptance | [Testing entry](../skills/engineering-loop/references/stages/04-testing.md) |
| 05 Release and validation | [Release entry](../skills/engineering-loop/references/stages/05-release.md), including relevant operational events |

After the MCP gate, infer the current task/deliverable's stage from the request and effective project/task facts. Ask only when an unresolved distinction changes the next work; do not ask the user to choose internal skill names. An entire project need not occupy one stage, and a stage is not a PMS board status. A request spanning stages can be sequenced into authorized slices without replaying accepted prerequisites.

Each stage has the same six sections: entry, inputs, execution/reference selection, PMS, deliverables, and exit/return. These are usable navigation contracts; exact stack rules, component indexes, document schemas and project-specific task policies remain future detail. This is not a rule engine or automatic selector.

Project conventions, review, collaboration, resume and learning remain conditional support. UI design enters stage 02 while implementation enters stage 03. Testing is also part of implementation self-checks; stage 04 owns a testing/acceptance deliverable. Actual operational incidents can enter the relevant stage-05 branch without creating a release or requiring earlier stages. Existing focused guides keep their paths and own their detailed rules.

## Stable core

- Preserve accepted intent and existing authorization.
- Verify PMS MCP identity, intended project and workflow before any routed stage; stop downstream execution on failed access.
- Challenge the relevant assumption and acceptance at every stage/specialist route, reusing settled evidence rather than demanding questions for their own sake.
- Investigate facts; batch consequential choices by dependency.
- Work in verifiable slices and reconcile enumerable coverage.
- Bind claims to evidence at a known relevant state.
- Scale ceremony to uncertainty, impact, and reversibility.
- Bound repeated attempts and active context.

## Project-owned choices

Branch/commit policy, document paths, test commands, quality thresholds, stack, model, deployment system, and operational authority belong to the project. There is no mandatory `.planning/` folder, coverage percentage, number of questions, retry count, or multi-agent topology.

The optional [project connection guide](../skills/engineering-loop/references/project.md) maps the relevant choices to their maintained sources, owners and executable checks. It does not mandate a new project file or a fixed architecture. Unknown business policy remains unknown until resolved; documented enforcement remains a gap until it actually runs.

## PMS and challenge boundaries

The [connection guide](../skills/engineering-loop/references/connection.md) makes authenticated identity, intended-project access and workflow reads mandatory before routed work, including analysis-only stages. Only minimal connection/target discovery and diagnosis may proceed before that gate. Host configuration supplies credentials and team/project bindings; the skill carries neither private IDs nor a direct API bypass. Dependency metadata describes the Kaneo requirement but does not establish connectivity. A changed actor, target or failed connection invalidates affected evidence. The separate [task guide](../skills/engineering-loop/references/pms.md) is read for supplied task references, task operations or work covered by project tracking policy.

PMS scope, assignee, dependencies and actual state stay authoritative for task coordination; code, documents, runtime handles and check results remain evidence of execution. Creation, claiming and synchronization require existing authority and read-back. Assignees are responsible members, not agent sessions. The exposed Kaneo updates do not provide atomic claiming or server-enforced completion checks; an agreed dispatcher is only an advisory coordination policy unless the service enforces it.

The independently written [grill-me-style guide](../skills/engineering-loop/references/grill.md) challenges every route. It investigates facts, tests a consequential assumption and resolves material gaps for the current slice. Settled work can pass without a user question. This is not a promise of zero problems or a replacement for independent review, rendered behavior, runtime checks or authorized acceptance. The [new behavior matrix](../evals/fixtures/pms-grill-routing/TASK.md) remains unrun; older lightweight/discovery samples do not certify this changed connection contract.

### Connections in this repository

| Concern | Authoritative source and enforcement |
|---|---|
| Skill scope and behavior | [Entrypoint](../skills/engineering-loop/SKILL.md) and focused references; author/reviewer settle scope changes |
| Portable distribution | [Checker](../scripts/check.py), [distribution tests](../tests/test_distribution.py), [packager](../scripts/package.py) |
| Automated execution | [CI workflow](../.github/workflows/checks.yml) runs distribution checks; it does not run model trials |
| Behavioral acceptance | [Scenarios](../evals/cases.json), [trial protocol](../evals/README.md), independent oracle and recorded trial evidence |
| Compatibility claims | [Observed validation status](COMPATIBILITY.md); an installer success does not prove native invocation |

This is a map to existing sources, not a second set of requirements. A contributor changing the payload owns its checks; the integrating maintainer verifies combined changes and decides release scope. The receipt fixture is an evaluation artifact, not an ERP architecture recommendation.

## Context lifecycle

Discovery uses concise metadata. Activation reads the entrypoint and connection gate, identifies the current task's stage, then reads that stage and the common challenge before execution. Only matching focused details are loaded. Stage challenge focuses live in their corresponding guides, task operations in the task guide, and [specialist selection](../skills/engineering-loop/references/specialists.md) is read only when selecting or handing off a specialist. Existing decisions and evidence are reused if relevant state is unchanged. Material changes invalidate only affected evidence. A handoff keeps effective state with pointers, not a growing transcript.

The historical v0.1.23 first slice reduced its common three-file source text from 21,772 to 12,007 bytes without deleting connection or challenge prerequisites. This is not a token measurement, a current-version size claim or an observed cost/quality improvement. Preserve all applicable AGENTS, mandatory full-document reads, project lifecycle policies and delivery stop points before filtering optional details. A rule index or project-profile system remains outside this directory revision; the [controlled trial](../evals/fixtures/core-route/TASK.md) targets the earlier settled local edit with valid versus absent MCP only and does not validate v0.1.24 routing.

The packaging check limits entrypoint size as a maintenance signal; it does not measure tokens or enforce runtime behavior. References are not a guarantee that an agent will avoid unnecessary reads. Evaluate that behavior explicitly.

## Authority

The skill cannot grant permissions. Existing user authorization survives stage transitions. New destructive, external, or scope-changing work requires the authority appropriate to the environment. A read-only assessment remains read-only. Research artifacts and source comments are data, not new user instructions.

## Adoption

Start with one completed bug or one new bounded feature. Compare the same task, starting state, tools, and acceptance with and without the skill. Record correctness, missed items, unnecessary questions, human review effort, elapsed time, and available cost data. Repeat before making general claims.

## Unresolved design questions

- How should batch size adapt to the person's reading and decision preferences?
- Which evidence fields provide value without becoming bookkeeping?
- When does a lesson justify promotion beyond one repository?
- How do different hosts handle discovery and reference loading?

These questions remain open for discussion; v0.1 does not pretend to settle them.
