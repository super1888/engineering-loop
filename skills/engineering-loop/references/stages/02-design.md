# 02 Solution design and planning · 方案设计与规划

## Enter

Use after the entrypoint's MCP gate when the current deliverable is a product specification, architecture decision, UI/interaction design or delivery plan. A known implementation detail does not automatically require a design workshop.

## Inputs

Reuse the relevant accepted behavior, boundaries, current architecture and design system, maintained project conventions and known delivery constraints. Check only prerequisites of this design slice; do not demand every upstream document when the necessary agreement already exists.

## Execution and focused references

- For behavior specifications or consequential scope changes, read [requirements.md](../requirements.md).
- For a consequential choice of system shape, technology, capacity, user wait or ownership cost, read [architecture.md](../architecture.md). Use its challenge and evidence checks when comparing options and before concluding the design.
- For an interface another module, client or external system consumes, including retry and idempotency behavior, read [api-design.md](../api-design.md).
- For architecture responsibilities, reference-project inheritance or enforcement gaps, read [project.md](../project.md) and the applicable maintained project architecture.
- For interface decisions, read [ui.md](../ui.md), including its target-device gate.
- For an applicable shared component/style catalog, use [template matching](../development/templates.md); it also serves design work without moving the request into implementation.
- For kickoff materials, module assignments, delivery estimates or turning kickoff decisions into PMS tasks, read [delivery-planning.md](../delivery-planning.md).
- For delegated ownership, dependencies or integrated planning, read [collaboration.md](../collaboration.md) when those boundaries apply.

Apply the [common challenge](../grill.md) at **Full depth** to a design, architecture or delivery-plan deliverable: challenge whether the proposed solution and task split meet the confirmed need with the least that works, and produce the written outputs, independent check and confirmation gate before dependent development or task creation. A known implementation detail stays Light. On the architecture route, actively test the recommendation against a material counterexample or failure case even when project evidence already answers the relevant questions. Use facts, representative content or a bounded experiment. Ask only for decisions that remain open and matter to this slice.

## PMS

Follow [pms.md](../pms.md) for task references, operations and tracking policy. Bind specifications, design or plans to their actual deliverables; do not create one card per section or screen by default. Reuse existing authorization, distinguish ownership from blocking dependencies and keep phase labels separate from board states.

## Deliverables

Maintain the requested specification, design, architecture decision or delivery plan in its existing project location, with version, affected scope, decisions and linked prerequisites. Use the project's actual templates; new technical-stack and component-template indexes are not supplied by this stage.

## Exit and return

The requested design must support its accepted examples and make unresolved decisions explicit. UI conclusions need the applicable rendered or interactive evidence; a proposal is not implementation proof. Return to [requirements](01-requirements.md) for a consequential behavior dispute. Move to [development](03-development.md) only when authorized; design-only work stops with its design.
