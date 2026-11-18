# Design boundaries

One team task/delivery router, focused references, and project-owned artifacts. Routed stages require a verified PMS MCP connection and an evidence-based challenge; specialist skills supply execution guidance. The PMS stores shared task facts while the repository retains its engineering system and artifacts.

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

The [PMS guide](../skills/engineering-loop/references/pms.md) makes authenticated identity, intended-project access and workflow reads mandatory before routed work, including analysis-only stages. Only minimal connection/target discovery and diagnosis may proceed before that gate. Host configuration supplies credentials and team/project bindings; the skill carries neither private IDs nor a direct API bypass. Dependency metadata describes the Kaneo requirement but does not establish connectivity. A changed actor, target or failed connection invalidates affected evidence.

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

Discovery uses concise metadata. Activation reads the entrypoint. A current need reads its reference. Existing decisions and evidence are reused if relevant state is unchanged. Material changes invalidate only affected evidence. A handoff keeps effective state with pointers, not a growing transcript.

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
