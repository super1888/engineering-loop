# Design and verify a usable interface slice

**Challenge focus:** Which user task and existing design system govern the choice, and what rendered or interactive evidence could expose a failed assumption?

Use when a new or materially changed interface needs interaction or visual decisions. Reuse the project's design system, accepted screens and available design/browser tools. A settled copy or spacing correction needs only its affected checks, not a redesign workshop or a new design tool.

## Frontend design gate: desktop by default

Before planning or accepting frontend work, establish the requested target. Without an explicit user requirement for mobile, design and verify desktop only: do not add mobile mockups, phone breakpoints, touch-specific navigation or mobile acceptance tasks. Desktop window resizing, long content and browser zoom remain relevant desktop checks; a narrow window alone does not authorize a mobile scope.

When the user explicitly requests mobile support, include the specified devices, interactions and viewports in design and acceptance. An explicit tablet or phone request applies to that target, not every mobile device. Reuse an already-confirmed user requirement rather than asking again. If existing project requirements or a supplied reference conflict with the desktop default, identify the conflict and resolve its intended scope before dependent changes; do not silently remove existing mobile behavior.

At acceptance, state the target and inspect the corresponding rendered evidence. Unrequested mobile work is a scope failure to reconcile before acceptance; missing explicitly requested mobile evidence remains unverified. When rendering is unavailable, report the limitation rather than treating this gate as passed. The gate applies to design and implementation decisions, not a demand for a browser session during a design-only advice task.

## Start with a task and representative content

Name the actor, entry point, information needed, main action, success signal and supported exit/return path. Establish what the interface must help the person decide or complete before choosing controls. Resolve business-policy uncertainty through [requirements.md](requirements.md); layout choices must not silently introduce permissions, cancellation or recovery policies.

Before choosing the layout of a new screen or a consequential layout change, establish the minimum, typical and maximum of each variable piece of content (length, count, size), from real data where the project has it, and the states that matter for this task. Look these up before asking. Ask the owner what must stay untouched and what would make the result feel wrong even if it were polished; record the answers as anti-goals beside the scope.

Arrange information by the task's priority and frequency. Use representative titles, quantities, images and long or missing values to test density and hierarchy; placeholder cards alone cannot establish a usable layout. Reuse effective tokens, components and interaction conventions before introducing a parallel visual system. A supplied reference establishes only the properties the user intends to inherit, not every hidden behavior.

## Test the uncertain decision before replication

When direction remains consequentially uncertain, compare a small number of materially different approaches against the same user task and content. Explain the tradeoff and recommend one; cosmetic variants that cannot change the decision add little evidence. Variants differ in structure: layout, information hierarchy or primary action, not color or copy. Three is the default and five the ceiling; redo one that came out close to another. Within a prototype requested or authorized for the decision, mount them where the result will live, on the real route or inside its host page with representative or permitted data and surrounding navigation, because every variant looks acceptable on an empty page. Stub mutations, mark the code as throwaway and switch variants without adding a dependency. When one wins, record the question, the verdict and the reason in the design record, rebuild the winner to production standard rather than promoting prototype code, and remove the losers and the switcher from the delivered branch. If an accepted direction already exists, proceed within it without asking the user to choose again.

Build one representative page or interactive slice before multiplying similar screens. Include the main path and relevant loading, empty, error, disabled or permission states; distinguish a missing result from an unavailable action. For asynchronous work, make the accepted completion signal and return behavior observable. These are checks on the requested flow, not automatic authorization to add new states or capabilities.

A static rendering can answer visual hierarchy questions. Navigation, editing, validation, focus or recovery questions need an interactive slice. Use the least costly artifact that can resolve the uncertainty; a prototype does not prove backend integration or production readiness. Preserve existing authorization when moving from design into implementation.

## Accept the rendered behavior

Run the slice in the project's actual browser or preview path. Follow the representative task using realistic content, inspect the result, and capture evidence of the relevant state. Where applicable, check:

- Navigation and supported return paths retain the expected context and show the changed result.
- Loading, validation and failures give actionable feedback without duplicate submission or lost input.
- Relevant desktop window sizes (and explicitly requested mobile viewports) remain readable; long labels, dense data and missing media do not obscure the main action or create unintended overflow.
- Keyboard order, visible focus, control names, contrast and status feedback support the affected interaction. Automated accessibility results still require interpretation.

Choose viewports and states from the actual use or reported defect rather than imposing an exhaustive matrix. Compare a nearby unaffected layout when a responsive repair could regress it. Geometry checks and screenshots serve different purposes: neither alone establishes interaction quality. See [verification.md](verification.md) for visual, accessibility and integration evidence boundaries.

Record the tested route, viewport, content/state, artifact or revision, observed result and evidence location in the project's existing acceptance record. Distinguish rendered inspection, interaction checks, real service integration and user acceptance. If browser access or a required state is unavailable, state that boundary instead of declaring the interface complete from source inspection. When observed use exposes a failed design assumption, return to a bounded requirements decision rather than adding unrelated polish.
