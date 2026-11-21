# Roadmap

## v0.1.33 · unreleased routing-only entrypoint

- Reduce the [entrypoint](../skills/engineering-loop/SKILL.md) from 6,921 to under 4,000 bytes and lower its maintenance budget from 7 KB to 4 KB. It keeps the connection gate, stage location, the six-stage table, a support table and five always-on rules: project instructions are preserved, a stage is not authority, interrupted work resumes, checks are not weakened to pass, and only checked results are claimed.
- Remove general conduct that the [common challenge](../skills/engineering-loop/references/grill.md), [verification](../skills/engineering-loop/references/verification.md), [connection](../skills/engineering-loop/references/connection.md) and [collaboration](../skills/engineering-loop/references/collaboration.md) guides already state. Move the sentences that existed only in the entrypoint: changing the hypothesis when an attempt yields no new evidence goes to the [development core](../skills/engineering-loop/references/development/core.md) and verification; keeping acceptance independent goes to the development core; binding evidence to its version and stopping at a finished result go to verification; keeping one recoverable state goes to [resume](../skills/engineering-loop/references/resume.md).
- Bytes are not measured tokens or quality. A rule outside the entrypoint applies only when its guide is read; an earlier same-chat continuation sample already failed with the rule in the entrypoint. The effect of this move is unmeasured.
- Stage templates are unchanged. The new cases are unrun. [Entrypoint scenarios](../evals/fixtures/slim-entry/TASK.md) · [Evidence index](../evals/STATUS.md)

## v0.1.32 · unreleased challenge depth and extracted team stack rules

- Give the common challenge two depths. Stage 01 and 02 deliverables use Full depth: separate the problem from the proposed solution, ask open questions before offering options, disagree with evidence, produce assumptions, an alternative, a disconfirming case, coverage and open decisions, pass a fresh-context check where available, and wait for the owner's confirmation before dependent work. Settled local edits stay Light. [Common challenge](../skills/engineering-loop/references/grill.md)
- Add team rule files extracted from the team's existing services and products for [Java / Spring](../skills/engineering-loop/references/development/stacks/java-spring.md), [Python / FastAPI](../skills/engineering-loop/references/development/stacks/python-fastapi.md) and [React frontends](../skills/engineering-loop/references/development/stacks/frontend-team.md). They are partial: confirmation as the shared standard is pending and each lists choices the team has not settled. The development router reads the matching file before implementation; project instructions win where they differ.
- Stage templates are unchanged. The shared component and style catalog remains unavailable.
- The new cases are unrun. [Challenge and stack-rule scenarios](../evals/fixtures/challenge-depth-and-stack-rules/TASK.md) · [Evidence index](../evals/STATUS.md)

## v0.1.31 · unreleased acceptance and production-defect handoff

- Keep the original pre-release defect and test acceptance record in stage 04. Track production defects in stage 06 and reference that record and the affected version. Reuse the project's existing formats and locations. [Acceptance template](../skills/engineering-loop/templates/acceptance-record.md) · [Operations template](../skills/engineering-loop/templates/operations-record.md) · [Unrun template routing cases](../evals/fixtures/stage-templates/TASK.md)

## v0.1.30 · unreleased six-stage document templates

- Add starter templates for each stage's applicable deliverable while preserving existing project formats. The requirements template covers new products and additions to existing systems. Development, independent acceptance, release verification and operations link their own evidence. [Six-stage templates](../skills/engineering-loop/templates/index.md)
- Leave team-specific fields and decisions open until needed. Ask about gaps that can change delivery or acceptance and keep the evidence of settled decisions in the existing record.

## v0.1.29 · unreleased kickoff and PMS planning

- Add a reusable stage 02 kickoff plan for product design, technical design with shared contracts, development tasks and schedule, and module ownership and readiness. Carry the existing project format through drafting, kickoff decisions and authorized synchronization. [Delivery planning](../skills/engineering-loop/references/delivery-planning.md) · [Kickoff template](../skills/engineering-loop/templates/kickoff-plan.md)
- Estimate human effort and elapsed time independently. Record stage 03 implementation and self-test evidence, track review according to project ownership and handoff, and link actual stage 04 acceptance where applicable.
- Verify the intended PMS target, authenticated operator and responsible assignee before approved task writes. Check each participant's connector when the project requires individual access. [Planning scenarios](../evals/fixtures/kickoff-planning/TASK.md) · [Evidence index](../evals/STATUS.md)

## v0.1.28 · unreleased architecture selection and tradeoffs

- Add focused architecture guidance to stage 02 and pair it with the common challenge. Resolve consequential gaps with evidence, a bounded check or an authorized decision.
- Compare feasible options using measurable workloads, both waits where applicable and the same cost horizon. Record the recommended minimum design, verification and triggers to reconsider. [Architecture guide](../skills/engineering-loop/references/architecture.md)
- Track checks for the new route by version. [Architecture scenarios](../evals/fixtures/architecture-tradeoffs/TASK.md) · [Evidence index](../evals/STATUS.md)

## v0.1.27 · unreleased six-stage routing

- Add 06 Continuous operations to the skill entrypoint and the current execution directory.
- Route release preparation, deployment and verification of an identifiable release to 05. Route ongoing operations, actual incidents and independent recovery or readiness work directly to 06.
- Use the existing operations reference, PMS gate and authorization boundaries. Track the proposed requirements, design and PMS task refinements in the [six-stage discussion draft](ROUTING.zh-CN.md#六阶段设计草案).
- Use version-specific checks for the new entries and the release/operations boundary. [Six-stage scenarios](../evals/fixtures/six-stage-routing/TASK.md) · [Evidence index](../evals/STATUS.md)

## v0.1.26: unreleased scenario execution details

- Give all 28 development scenarios individual execution bodies, leaving catalogs focused on matching and links.
- Specify inputs, concrete actions, relevant positive/negative checks, actual delivery evidence and remaining project bindings; preserve copy-only, read-only and design-only limits.
- Retain the user's confirmed existing project conventions. Add version-aware React/Vue behavior checks from official sources without selecting libraries, upgrades or a common architecture.
- Reuse one optional delivery record for tracked artifacts and existing PMS policy; do not create a document/card per component or professional role.
- Keep actual template contents pending after the intended source returned empty. Record current validation under the [detail specification](../evals/fixtures/development-details/TASK.md), separately from prior routing samples.

## v0.1.25: unreleased development subroutes

- Keep the five-stage top level and route stage-03 work through 28 frontend, backend, integration and engineering/shared scenario entries, using task facts, paths, module configuration and changed boundaries.
- Extract existing implementation content into the common core and nine shared risk entries; retain the old implementation path as a compatibility route and keep focused verification/UI sources authoritative.
- Apply stack filters and conditional risk rules without copying every scenario per language/framework or loading every branch. Preserve project instructions, required full reads, MCP, challenge, authority and acceptance.
- Reserve explicit pending slots for team stack standards and component/style entries. The template contract is available; an actual Frontend-Design-Common catalog and shared button templates remain unconnected.
- Reuse project conventions for missing optional detail, and stop dependent work for missing necessary prerequisites. Subroute selection does not create tasks or grant additional execution authority.
- Record actual checks in the [development-routing validation](../evals/fixtures/development-routing/RESULTS.md); detailed indexes alone do not establish routing accuracy, reduced context or model-quality gains.

## v0.1.24: unreleased five-stage directory

- Make requirements analysis/confirmation, solution design/planning, development/integration, testing/acceptance and release/validation the five first-level entries.
- Keep the MCP gate mandatory; identify the current task's stage from available evidence, asking only about consequential ambiguity, then apply that stage's challenge and relevant focused guidance.
- Give each stage the same six-part contract: entry, inputs, execution/reference selection, PMS use, deliverables, and exit/return. Preserve current specialist/support guides and their boundaries; detailed stack, component, document and task templates remain follow-up work.
- Treat project rules, review, collaboration, resume and learning as conditional support. Distinguish task stage from project-wide progress and board status; operational events need not create release work.
- Keep historical trials tied to their actual versions. Current checks and any scenario exercises are recorded in the [evidence index](../evals/STATUS.md); the directory change alone does not establish automatic selection, context savings or delivery quality.

## v0.1.23: unreleased common-core routing split

- Separate the mandatory connection gate from task operations, keeping identity, target, workflow, fail-closed behavior and evidence validity required on every activated route.
- Keep the shared grill method small; move stage focuses to their owning guides and read specialist coordination only when selecting or handing off a specialist.
- Preserve applicable project instructions, full-document requirements, authorization and delivery stop points. Do not introduce a rule engine or cross-project profile changes in this first slice.
- Freeze the [local-copy trial](../evals/fixtures/core-route/TASK.md) with valid versus absent MCP conditions and inspect actual model/tool/file events separately from adapter mechanism controls. Record actual outcomes and limits before making any behavioral claim.

## v0.1.22: unreleased team entrypoint, PMS gate and route challenge

- Reposition the entrypoint around team task creation, claiming, execution and acceptance, with focused lifecycle and specialist routing.
- Require actual authenticated PMS MCP identity, intended-project access and workflow reads before every activated route, including analysis-only work. Block downstream execution on failed access; dependency metadata and configuration alone cannot pass.
- Add a Kaneo task-operation guide for scoped lookup, authorized creation, ownership, uncertain write outcomes, read-back and evidence-based state updates. Keep team bindings and credentials outside the distributed skill; ordinary assignment is not atomic claiming.
- Apply an independently written grill-me-style challenge to each stage/specialist, investigating facts and resolving consequential assumptions while allowing zero-question settled work and preserving existing authorization.
- Keep the [new behavior matrix](../evals/fixtures/pms-grill-routing/TASK.md) unrun. Local structural, distribution and read-only connection checks do not establish model reliability, write access or server-enforced gates; see [current compatibility evidence](COMPATIBILITY.md#unreleased-v0122-connection-contract).

## v0.1.21: unreleased inline-link validation

Check angle-bracket Markdown destinations with spaces and optional inline link titles. Retain valid local destinations, external links and fragment-only links; this remains a focused inline-link check, not full Markdown parsing.

## v0.1.20: unreleased packaged-input validation

Validate Markdown links and JSON inside the complete skill payload, including directories whose names normally identify local output. Preserve repository-local output exclusions. This fixes distribution validation coverage, not model behavior.

## Unreleased local native discovery observations

- Observe a complete project-local installation in fresh CLI contexts without evaluator-supplied skill body.
- Keep implicit project-entry evidence, explicit entry-read uncertainty and a lightweight control separate; do not turn one local build into cross-host certification.
- Preserve original strict criteria and catalog/input-freezing audit limits in `evals/STATUS.md` and the linked report.

## Unreleased existing-client release evidence

- Make the retained-assets branch of `release-existing-clients` runnable with two desktop versions and a delayed module fetch after cutover.
- Separate fresh-page health from open-page continuity and keep evaluator-supplied rollback configuration distinct from the model artifact.
- Preserve local-only, cache/retention-duration and production limitations; current execution status belongs in `evals/STATUS.md`, not historical snapshot wording.

## v0.1.19: unreleased same-chat continuation clarification

Preserve unfinished work through intervening questions, with explicit stop, replacement and draft-only controls. A [local two-turn trial](../evals/fixtures/same-chat-continuation/RESULTS.md) failed the continuation condition and respected explicit stopping. Investigate conditional-blocker recovery before claiming prevention; replacement, draft-only and new-chat controls remain unrun.

## v0.1.18: unreleased evaluation and packaging corrections

- Reject existing receipt leaves (including dangling links) and prepare receipt output before guarded dispatch; retain explicit failed/unstarted status on failed probes.
- Check all original inventory after a failed refresh, including records hidden by the current filter, without prescribing numeric display formatting.
- Ignore only the root-local `.venv` during document/JSON validation; preserve checks on project and nested fixture/payload files.
- Preserve unrelated longer path prefixes in trial summaries. These controls repair tools, not model-quality evidence.

## v0.1.17: unreleased verification reference routing

- Keep common verification decisions in the main guide and route conditional technical boundaries to a focused reference.
- Preserve original acceptance paragraphs and exceptions without strengthening unrelated checks or weakening relevant gates.
- Check structural preservation and actual fresh-context reference selection separately from general quality or context-cost claims.

## Unreleased handoff consumption and probe-runtime correction

- Exercise a prepared runtime handoff and an explicit lightweight read-only condition in fresh contexts, without claiming end-to-end multi-agent or causal benefits.
- Resolve the read-guard helper’s own probe interpreter when a virtualenv alias is hidden by the policy; retain target argv and denied roots unchanged, with a reproduced red/green regression.
- Keep the post-run helper correction distinct from the preceding model receipts. See `evals/README.md` for actual observations.

## v0.1.16: unreleased delegated environment handoff

- Distinguish coordinator-host availability from a contributor’s effective runtime, working directory and permission boundary.
- Carry relevant non-sensitive invocation and dependency resolution details; preserve guards and reuse unchanged capability evidence.
- Mechanism controls reproduce protected-path and missing module-resolution failures separately from code defects; model-transfer and time-saving effects remain unproven.

## Unreleased independent-destination recovery validation

- Exercise SQLite backup restoration separately from restarting intact original storage, with an explicit before/after snapshot boundary.
- Preserve backup/source identity and distinguish restored historical data, new writes and restart persistence from off-host disaster recovery or production recovery objectives. See `evals/README.md` for actual results and limits.

## v0.1.15: unreleased operational readiness

- Connect service expectations to observable business outcomes, response ownership and bounded runbooks without mandatory monitoring infrastructure.
- Exercise a local configuration fault where HTTP remains healthy but queued work does not progress, preserving deliberately manual test modes.
- Keep restart durability, actual backup restoration and production acceptance as separate evidence claims. Actual rehearsal conditions and results belong in `evals/README.md`.

## Current validation priorities

- Independent review: distinguish a reproduced contract failure from passing author checks, and retain a legitimate no-finding control. See `evals/README.md` for actual observations rather than inferring benefit from agent count.
- Operational readiness now has local worker-configuration recovery and independent-destination backup restoration evidence, including an explicit snapshot cutoff. Production signals/response ownership, off-host recovery and production recovery objectives remain unvalidated; preserve deliberate manual-worker testing and do not require a monitoring service for ordinary local work.
- Performance, capacity and cost remain conditional future work. They need representative workload and accepted budgets before new gates; no measurements or general improvement are claimed here.

## Unreleased specified-directory read protection

- Add a macOS evaluation command wrapper with per-root canary probes, legitimate workspace operations and failure-closed dispatch.
- Evaluate a real implementation under the boundary and independently inspect resulting desktop behavior; retain actual loaded-version limitations and distinguish directory protection from complete isolation.

## Unreleased desktop runtime evaluation

- Exercise the desktop target gate in a disposable inventory implementation, using evaluator-owned browser interactions and positive/negative oracle controls.
- Preserve the initial empty-state assertion ambiguity and distinguish a clarified known-issue follow-up from independent discovery. See `evals/README.md` for actual outcomes and limitations; no general skill advantage or real-service acceptance is claimed.

## v0.1.14: unreleased frontend target gate

- Default frontend design and acceptance to desktop; add specific mobile targets only on explicit user request.
- Preserve established mobile behavior and resolve conflicting requirements before dependent changes.
- Verify target scope separately from rendered acceptance; advice-only trials cannot prove browser behavior.
- Split follow-up advice criteria and correct first-round applicability limits without rewriting historical scores.
- Normalize known lexical/resolved trial paths in a shared recorder helper, with symlink and sibling-path controls; remove the macOS temporary-directory workaround.

## v0.1.13: unreleased product and UI revision

- Challenge unresolved product assumptions with user/context, alternatives, impact, success signals and a bounded experiment; retain direct execution for settled local changes.
- Add an on-demand UI workflow from user tasks and representative content to states, prototypes and rendered acceptance.
- Run a first-round comparison and retain actual conditions, limitations and outcomes in `evals/README.md`. No release or general quality advantage is implied.

## v0.1.12: unreleased saved-receipt revision

- Read back identity and state before a saved receipt triggers ownership transfer or continuation; a successful writer exit and JSON syntax do not establish that contract.
- Repair only the invalid receipt within existing authority, retaining verified work and live handles. Keep ordinary text handoffs in their established format without a required schema or approval.
- Add [receipt checkpoint controls](../evals/fixtures/handoff-receipt/TASK.md) for null/stale artifacts, a repaired receipt and a valid text handoff. These remain unrun; packaging checks do not establish a model-behavior benefit.

This is a local guidance revision, not a published release.

## v0.1.11: unreleased conversation-handoff revision

- Reconcile terminal reports and current artifacts with stale ownership records before replacing an authorized conversation.
- Transfer confirmed ownership and live handles at a safe boundary; retain resource-state uncertainty and avoid replaying completed work.
- Keep contributor-history reads compact before displaying long tool transcripts.
- Extend the [coordinator checkpoint fixture](../evals/fixtures/delegated-continuation/TASK.md) with stale-record recovery and a live-build control. Both new checkpoints remain unrun; packaging checks do not establish improved coordination.

This is a local guidance revision, not a published release.

## v0.1.9: unreleased directory-junction protection

- Reject Windows directory junctions as well as symlinks in the skill payload, using the standard library's native reparse tag on supported Python versions.
- Check entries before descending into linked directories or replacing an existing ZIP; keep normal deterministic archives, file hardlinks and their input-preservation controls.
- Add one native Windows junction regression that checks both distribution rejection and preserved archive/source bytes. Other platforms skip that Windows-specific case.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.8: unreleased empty-scalar description protection

- Reject empty or blank quoted descriptions and unquoted YAML null values, including an inline comment after a null value.
- Reuse the existing metadata regression; preserve quoted null words, literal hashes and comments after a nonempty value. The check still targets this repository's single-line frontmatter layout, not general YAML validation.

This is a local distribution-check correction, not a published release or a model-behavior improvement.

## v0.1.7: unreleased comment-only description protection

- Reject a description whose first nonblank character starts a YAML comment inside the actual frontmatter; a body example cannot supply the missing value.
- Extend the existing metadata regression with comment-only values and preserve quoted descriptions starting with a literal hash. The check remains scoped to this repository's frontmatter layout.

This is a local distribution-check correction, not a published release or a model-behavior improvement.

## v0.1.6: unreleased blank-description protection

- Reject a description containing only spaces or tabs inside the actual frontmatter; a body example cannot satisfy it.
- Extend the existing metadata regression and preserve descriptions with extra leading spacing. This check remains scoped to this repository's frontmatter layout, not a general YAML validator.

This is a local distribution-check correction, not a published release or a model-behavior improvement.

## v0.1.5: unreleased archive file-identity protection

- Reject existing output files that are hardlinks to the supplied license or any skill source file before opening the ZIP.
- Use the standard library's file-identity check; verify preserved input bytes for the entrypoint, a nested reference and the external license alongside normal archive controls.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.4: unreleased archive input protection

- Reject an archive output that resolves to the supplied license, alongside the existing skill-source protection.
- Extend the source-preservation regression to the external license; normal complete and deterministic archive checks remain in place.

This is a local packaging correction, not a published release or a model-behavior improvement.

## Unreleased evaluation tooling correction

- Execute candidate Python sources and public tests with an isolated bytecode path and writes disabled; timestamp/size collisions cannot reuse an earlier candidate's cache. Preserve workspace source/cache bytes, including native receipt/import oracles and the browser evaluator's server launch.
- Verify the unchanged 10,000-cent order and export boundary in a fresh process for the comment-only control; stale declaration text cannot mask a changed value or inlined limit, and equivalent annotated declarations remain valid.
- Resolve relative trial directories in routing and convention recorders; preserve prompt mismatch rejection, remove local directory prefixes, and retain ordinary final-message words and punctuation.
- Accept annotated constant assignments in the convention amount check; reject a wrong value or a declaration without a value assignment.
- Verify the order and export limits against the module constant in a fresh process; unused references cannot hide an inlined limit in either behavior.
- Copy convention-trial skill revisions from native NUL-delimited Git paths, preserving Chinese names, spaces and committed file bytes independently of working-tree edits.
- Accept standard constant and module imports, including aliases, in the convention amount check; keep unused-import and inlined-limit counterexamples failing.
- Reject a blind-gate decision output that aliases any review input, artifact or fixture context; preserve input bytes while allowing a separate decision file to be refreshed.
- Invalidate a blinded review when its referenced task context changes; reuse the context frozen in the packet and preserve line-ending-only conversions.
- Reject private arm mappings inside the review directory or its descendants during preparation and gating.
- Treat a silent nonzero backend or form subprocess as a failed routing check; retain its exit code instead of an empty failure value.
- Require completion markers after the routing and convention amount checks' independent assertions; an early zero exit cannot substitute for completed checks.
- Require nonempty, unskipped native public-test reports in routing records and the convention comment control; the form report must execute at least the fixture's two cases.
- Build convention-trial patches from each workspace's frozen Git baseline, so later repository template changes are not attributed to the implementing agent.
- Record routing-trial file lists and patches against the prepared Git baseline, retaining staged changes alongside unstaged edits.
- Reject `SystemExit` during candidate imports in the receipt and asynchronous-import oracles, so an early zero exit cannot bypass their checks; preserve the original exit in the diagnostic cause.

These are regression-tested evaluator corrections, not changes to the distributed skill or evidence of model-quality improvement.

## v0.1.3: unreleased description gate correction

- Reuse the frontmatter boundary for description validation; a documentation example cannot substitute for a missing skill description.
- Preserve the valid-header control and version-mismatch regressions in the same focused distribution check.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.2: unreleased metadata gate correction

- Compare the plugin version with the skill's actual `metadata.version` in the repository's YAML layout; body examples and description text cannot satisfy the gate.
- Keep a focused regression for mismatched metadata masked by documentation, plus a valid-metadata control with an unrelated example version.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.1: unreleased coordination correction

- Route authorized delegation and ongoing goals to the existing collaboration guide.
- Keep a verified slice distinct from goal completion; reconcile terminal contributors, continuation corrections and explicit pauses within existing authorization.
- Preserve finite-task stopping and the existing live-handle monitoring boundary. No scheduler, runtime service or fixed agent team is added.

This is a local guidance revision, not a published release. Packaging checks and checkpoint exercises do not establish live orchestration quality or a general improvement.

## v0.1: usable public draft

- A portable entrypoint and focused lifecycle references.
- English and Simplified Chinese documentation.
- Claude Code plugin, Skills CLI, and manual/offline distribution.
- Reproducible packaging checks and public behavioral scenarios.

## Next: evidence before expansion

1. Repeat the supplied receipt and copy trials, then run remaining behavioral cases across Claude Code and Codex, including negative triggers.
2. Publish reproducible, sanitized transcripts and conditions; include failures.
3. Collect examples from small fixes, legacy systems, libraries, data pipelines, and application work.
4. Measure unnecessary questions, context reads, missed requirements, and human review burden.
5. Revise or remove rules that do not earn their cost.

## Community and discoverability

Keep the install path short, show realistic examples, publish honest evaluation reports, and resolve reported friction. Add ecosystem listings only where relevant and with maintainers' contribution rules. No unsolicited promotion, manufactured testimonials, or promises of star growth.

Potential later work: tested host adapters, optional explicit-only distribution, additional language docs, and a lightweight evaluation runner. Each needs a demonstrated use case before adding runtime dependencies or orchestration.

The project connection guide now locates business rules, shared ownership and active checks without imposing a new tracker. The receipt oracle and isolated fixtures enable local trials; they do not establish production quality, native host discovery, cross-project learning or a speedup. A real project pilot should retain accepted examples, an actual failure/regression and measured rework/review effort before expanding the generic rules again.
