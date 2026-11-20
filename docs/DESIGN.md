# Design boundaries

Engineering Loop has six stage entries, focused references, and project-owned artifacts. Verify the PMS MCP connection before selecting the task's stage, challenging its assumptions and applying the relevant guidance. The PMS stores shared task facts. The repository retains its engineering system and artifacts.

## Six-stage navigation

The first-level entries represent stages for the current task. Each entry points to the relevant professional and supporting guidance.

| First-level stage | Selected guidance |
|---|---|
| 01 Requirements analysis and confirmation | [Requirements entry](../skills/engineering-loop/references/stages/01-requirements.md) |
| 02 Solution design and planning | [Design entry](../skills/engineering-loop/references/stages/02-design.md) · [Architecture selection and tradeoffs](../skills/engineering-loop/references/architecture.md) |
| 03 Development and integration | [Development entry](../skills/engineering-loop/references/stages/03-development.md), including frontend/backend implementation, self-checks and integration |
| 04 Testing and acceptance | [Testing entry](../skills/engineering-loop/references/stages/04-testing.md) |
| 05 Release and validation | [Release entry](../skills/engineering-loop/references/stages/05-release.md), including release readiness, deployment and verification |
| 06 Continuous operations | [Operations entry](../skills/engineering-loop/references/stages/06-operations.md), including incident response, ongoing maintenance and operational readiness |

After the MCP gate, infer the current task/deliverable's stage from the request and effective project/task facts. Ask only when an unresolved distinction changes the next work; do not ask the user to choose internal skill names. An entire project need not occupy one stage, and a stage is not a PMS board status. A request spanning stages can be sequenced into authorized slices without replaying accepted prerequisites.

Each stage has the same six sections: entry, inputs, execution/reference selection, PMS, deliverables, and exit/return. These are usable navigation contracts. The development layer below indexes existing rules; exact team stack standards, actual component entries, document schemas and project-specific task policies remain future detail. This is not a rule engine or automatic selector.

Project conventions, review, collaboration, resume and learning are conditional support. UI design enters stage 02. UI implementation and its self-checks enter stage 03. Stage 04 covers a testing or acceptance deliverable. Deployment, post-cutover verification and rollback tied to an identifiable release enter stage 05. Incidents, live configuration repair, operational readiness and recovery independent of a release can enter stage 06 directly. Read focused release and operations guidance as required by the task and preserve the authority for each action.

Stage 02 pairs its architecture guide with the common challenge when the choice materially affects delivery, performance, cost or maintenance. Test the recommendation against a relevant counterexample and resolve decision-changing questions through evidence or an authorized decision. Compare feasible options under the same workload and cost horizon, distinguishing interaction response from background-result readiness when both matter. Record the simplest feasible recommendation, the verification method and what would trigger reconsideration. [Architecture guide](../skills/engineering-loop/references/architecture.md) · [Common challenge](../skills/engineering-loop/references/grill.md)

Proposed refinements to requirements intake, design planning and PMS task structure are tracked in the Chinese discussion draft. [Six-stage discussion draft](ROUTING.zh-CN.md#六阶段设计草案)

## Development selection and pending detail

The [development router](../skills/engineering-loop/references/development/index.md) adds scenario selection under stage 03. Its professional indexes cover [frontend F1–F8](../skills/engineering-loop/references/development/scenarios/frontend.md), [backend B1–B8](../skills/engineering-loop/references/development/scenarios/backend.md), [integration I1–I8](../skills/engineering-loop/references/development/scenarios/integration.md) and [engineering/shared E1–E4](../skills/engineering-loop/references/development/scenarios/engineering.md). Version 0.1.26 links all 28 entries to individual execution bodies: inputs, actions, discriminating checks, actual deliverables and project bindings. These are conditional baselines, not 28 mandatory reads or new cross-project stack policies. The user confirmed retaining existing project conventions.

Select from the accepted outcome, affected modules/paths, actual configuration, representative code and call boundaries. Keywords discover candidates; they do not settle the route. Select relevant scenario sections and compatible stack guidance, then independently attach triggered risk rules. Frontend work can expose an API/concurrency boundary; a backend keyword cannot by itself turn an administration-page label edit into service work. Cross-boundary work reads its applicable combination rather than all professional indexes.

The [common core](../skills/engineering-loop/references/development/core.md) retains shared implementation behavior. Nine [risk entries](../skills/engineering-loop/references/development/risks.md) own or link data fidelity, access, read-only effects, asynchronous/idempotent work, concurrent edits, split transactions, uploads, SDK transport and rendered evidence. Existing implementation constraints are migrated rather than dropped; [implementation.md](../skills/engineering-loop/references/implementation.md) keeps its old path as a compatibility entry. Shared bodies remain single-source, and existing verification/UI owners retain their authoritative detail.

[Stack bindings](../skills/engineering-loop/references/development/stacks.md) now link conditional React/Vue behavior checks to official sources and the actual installed version. Project library, architecture and style choices remain local; other specific bindings stay pending when unavailable. The [delivery record](../skills/engineering-loop/references/development/delivery.md) reuses existing task/document formats and actual evidence, not a new PMS schema. The [template contract](../skills/engineering-loop/references/development/templates.md) retains metadata/matching guidance, but the intended external repository returned empty on inspection. Explicit template identity still needs actual contents and compatibility; no template implementation is fabricated.

Effective project instructions, mandatory full-document reads, MCP, common challenge, acceptance and authorization cannot be filtered away. A triggered required rule remains required. Missing optional detail can fall back to maintained project conventions; an unresolved necessary prerequisite stops only dependent work. Each professional entry exposes pending details for later filling instead of inventing policies or blocking ordinary work because an optional team template is absent. PMS cards still follow actual delivery granularity and existing policy.

The historical [routing specification](../evals/fixtures/development-routing/TASK.md) retains its version. The current [execution-detail specification](../evals/fixtures/development-details/TASK.md) and [validation record](../evals/fixtures/development-details/RESULTS.md) separate source review from actual per-task reads and behavior. Rule coverage, unrelated reads, compatible template choice and appropriate clarification/fallback need observable task evidence before any routing-accuracy or context-benefit claim.

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

The historical v0.1.23 first slice reduced its common three-file source text from 21,772 to 12,007 bytes without deleting connection or challenge prerequisites. This is not a token measurement, a current-version size claim or an observed cost/quality improvement. Preserve all applicable AGENTS, mandatory full-document reads, project lifecycle policies and delivery stop points before filtering optional details. The development indexes are guidance, not an automatic rule engine or project-profile system. The [controlled trial](../evals/fixtures/core-route/TASK.md) targets the earlier settled local edit with valid versus absent MCP only and does not validate the v0.1.24 stage layer or v0.1.25 development routes.

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
