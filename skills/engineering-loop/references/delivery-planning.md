# Kickoff and delivery planning

Use from [stage 02](stages/02-design.md) when planning work for a team kickoff or converting its decisions into PMS tasks. Keep one effective plan from draft through kickoff and synchronization. Adapt the [kickoff template](../templates/kickoff-plan.md) to the project's existing documents, headings and tables. Link their effective versions and leave unsettled business details, formats and field conventions pending.

## Before kickoff

Use the [common challenge](grill.md) with the project manager or relevant decision owner. Test whether a representative user flow can be delivered and accepted with the proposed API, data model and ownership. Surface conflicts in requirements, contract boundaries or workload assumptions that change the plan. Reuse settled decisions and leave the dependent plan rows pending when an answer is still needed. Use [architecture.md](architecture.md) for consequential trade-offs and add design detail in proportion to the scope.

Prepare the draft outputs needed for the meeting. **产品设计方案** captures the agreed scope, user flow and acceptance examples. **技术设计方案** captures the architecture decision, module boundaries, API contracts and consumers, data models and read/write ownership. **开发任务与排期表** maps design scope to deliverable slices, dependencies, milestones and acceptance checks. **模块分工与开工检查** puts shared contracts, owners, sequencing and unresolved decisions on the agenda. Reuse existing documents where they cover these needs. Account for each in-scope deliverable in the task plan or as an explicit deferral.

## Divide work by deliverable and handoff

- Give each module or independently verifiable slice one accountable owner. A slice can cover both frontend and backend. Split when ownership changes, work can be scheduled independently, or a distinct handoff needs its own evidence. Group small related interfaces when they have the same owner and acceptance boundary.
- In [03 开发与联调](stages/03-development.md), track implementation and self-test as separately checkable items, including the expected self-test evidence. They can share one task for the same owner and handoff. Give code review its own task when a separate reviewer or scheduled handoff needs tracking. Link independent version or business testing to [04 测试与验收](stages/04-testing.md), with its own scope, expectations and evidence. Create a separate integration task only for a distinct cross-module or external verification chain with its own outcome.
- For shared APIs, schemas, files or environments, name a contract owner, consumers, the version or handoff condition and the work that depends on it. Use [collaboration.md](collaboration.md) to resolve overlapping writes and reconcile contract changes. Record the decision and affected consumers and checks before dependent work proceeds.

Estimate **human effort** and **elapsed time to acceptance** as separate ranges. Include AI setup, human review and likely rework in the effort of the people who do them. Include dependencies, review queues and external waits in elapsed time where they affect delivery. Prefer comparable AI-assisted work with evidence. When samples are missing, state what the estimate assumes and calibrate using the first accepted slice. Count effort at the working-task level once and derive milestones from dependencies and available owners.

## After kickoff

Reconcile the minutes into the same plan. Record accepted changes, their source and decision owner, the effective version and impacted tasks or contracts. Keep disputed or missing scope, assignee, dependency and acceptance decisions visible with their impact. Reuse the recorded authorization for the confirmed batch of creations, assignments and links. If creation is confirmed and the project permits an unassigned card, leave assignment pending.

For authorized PMS writes, use [connection.md](connection.md) and [pms.md](pms.md). Check the actual project, stage parents where used, available statuses and intended workspace members. Map approved development and independent acceptance work to their respective stages. Match existing cards by project, stable plan row and scope before creating. Use an existing card field or description to carry the plan row and source version so a card can be found before its ID is known. Use parent-child links for ownership and blocking relations for real prerequisites.

Record each confirmed card ID against its plan row. Read back affected fields, including parent, assignee, state or dependency links when applicable. After a partial or unknown result, reconcile the affected cards and relationships first, then finish confirmed missing writes within current authority. Record any pending assignments or links. A synchronized plan can be used by the corresponding stage once that work is authorized.
