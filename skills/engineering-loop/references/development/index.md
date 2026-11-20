# Route development by facts and changed boundaries

Use within [stage 03](../stages/03-development.md), after its MCP gate. This is a guidance index, not an executable classifier. A design-only request belongs to stage 02 and independent testing or review to stage 04. Use [stage 05](../stages/05-release.md) for release and cutover work and [stage 06](../stages/06-operations.md) for independent runtime incidents and maintenance. Updating build or configuration code can remain stage 03 without authorizing its application to production.

## Locate the slice

Establish the requested deliverable and authority, affected modules/paths, actual callers and relevant task facts. Detect each module's stack from maintained configuration, dependencies and representative code; a monorepo need not use one framework. Keywords find candidates, not the final route: an "admin/backend page" can be frontend work, and a visible save defect may involve a server contract.

Investigate available facts before asking. Ask only a remaining outcome, business or authority choice that changes the next action; do not ask the user to select skill names. Preserve every applicable project instruction, required full read and delivery stop point before filtering optional details.

## Select guidance

1. Read the [shared core](core.md) for a complete development slice. Do not restart project discovery or an already-settled interview.
2. Select the affected areas and scenario IDs below. Follow each selected scenario's **Read** link and read that execution body before implementation, even for a settled copy-only task. The catalog's summaries/checks are discovery metadata, not a substitute for the body. Reuse valid prior body reads; do not preload unrelated areas or bodies. Multiple areas are valid only when their changed behavior or contracts need them.
3. Match the actual module's stack and project rules. Read [stack bindings](stacks.md) only when locating or filling a specialist convention; a framework name alone does not supply a standard.
4. Check the short [risk index](risks.md) against the actual changes and downstream effects. Read every triggered rule, including a relevant rule outside the apparent frontend/backend label. Scenario suggestions are not an exhaustive risk checklist.
5. For component/style reuse, consult [template matching](templates.md) only when relevant. Read selected bodies and necessary related checks, then apply the stage's common challenge before execution. New boundaries need affected questions, not another full interview.

| Area | Catalog | Enter for | Do not infer from |
|---|---|---|---|
| Frontend | [F1–F8](scenarios/frontend.md) | Browser components, user interaction, page state or frontend build changes | A design-only request or every use of the word "page" |
| Backend | [B1–B8](scenarios/backend.md) | Service/API behavior, persistence, server-side access or jobs | An "admin/backend page" label alone |
| Integration | [I1–I8](scenarios/integration.md) | A changed/shared contract or an actual cross-module/system chain | Merely editing two files or using a mocked API |
| Engineering/shared capabilities | [E1–E4](scenarios/engineering.md) | Library/SDK, CLI/script, build/dependencies or generation tools | A requirement to deploy or install a new package |

For example, an approved button-label edit matches [F1](scenarios/frontend.md#f1-components-and-styles): follow its Read target to [component execution](frontend/components.md), whose copy-only path permits scoped consistency checks. Reading that body does not require a redesign, browser session, framework guide or component-template catalog.

## Missing or conflicting details

`available` identifies usable linked guidance within its stated scope; it does not certify execution. `partial` means existing baseline guidance is available but named team detail is pending. `pending` means no supplied standard/catalog is available. `retired` entries are not selected; retain their replacement pointer when one exists. These labels describe content, not task status or permission.

A pending optional convention is not an automatic blocker: reuse effective project instructions, accepted components and representative implementations. If a necessary contract, permission, acceptance rule or expressly required template cannot be established, report that exact gap and pause only dependent work. Do not fabricate a framework rule, template, package requirement or successful skill invocation. A conflicting explicit choice needs reconciliation before substitution.

Stage 03 inherits [PMS task policy](../pms.md), [verification](../verification.md) and conditional support from its stage. Route labels do not create cards, require one task per professional role, change an assignee or grant deployment authority. Finish at the accepted slice's evidence boundary.

For a tracked deliverable or a requested execution/acceptance document, use the [delivery record](delivery.md) with the selected body's concrete artifact and check requirements. A local edit can keep this evidence in its existing task or response; the record is not another mandatory file.

## Maintain an index entry

Use the following fields when adding a scenario, rule or binding; the catalogs use concise prose equivalents. Keep the normative body at one maintained location, and distinguish its authority/version from a candidate suggestion.

| Field | Required meaning |
|---|---|
| `id`, `status` | Stable identifier; available/partial/pending/retired |
| `scope` | Stage, area, concrete subscenario and any necessary stack/version conditions |
| `match` / `exclude` | Observable trigger and a legitimate nearby counterexample |
| `read` | Existing body/section and its maintained source; no dangling future links |
| `also_when` | Condition for a necessary related rule, not unconditional fan-out |
| `verify` | Evidence needed for the protected behavior, preserving valid alternatives |
| `pending` | Missing team-specific detail and where to fill it; not an invented requirement |

New content must earn its activation condition. Split a section into a file when it has useful independent content; do not create a language-by-scenario copy of the whole catalog. Read this maintenance section when extending the index, not as another execution ceremony.
