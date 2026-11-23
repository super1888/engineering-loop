# Architecture selection and trade-offs

Use from [stage 02](stages/02-design.md) for a consequential architecture or technology choice. Select this guide when system boundaries, real workload, user-visible waits, delivery or ownership cost could change the decision. Apply the [common challenge](grill.md) throughout the choice, starting with existing facts and decisions.

## Anchor the design in the current workload

- Start with confirmed scope, actual users and critical workflows. Translate relevant customer and active-user counts, operation frequency, data sizes and burst patterns into typical and peak load. Use measurements when available and attribute estimated ranges.
- Write the targets for the affected user journey at that load. For background work, distinguish the time until the user sees feedback from the time until the result is usable. When delay drives the decision, distinguish queueing, processing and downstream wait. Label confirmed requirements, observed performance, estimates and unknowns.
- State each quality that drives the choice as a scenario, not an adjective: the trigger, the part of the system affected, the measurable response and the conditions. Mark each driver observed, reported by a named source, inferred or unknown; a reported figure is not a measurement.
- Apply hard requirements and valid project constraints before comparing preferences. Include the roles, data guarantees, failure cases and operating boundaries that actually affect acceptance or the choice.

## Compare the smallest complete design

Start with the simplest candidate that can deliver the confirmed scope and be operated by the team. Use the evidence to select languages, deployment shape, data stores and middleware. Count reuse, skills, dependencies, deployment and migration effort as real costs.

Compare only credible alternatives with a consequential difference. Use the same load and time horizon for delivery effort, infrastructure and licensing, ongoing maintenance and relevant migration cost. Prefer the candidate that serves the accepted priorities with the least delivery and operating burden. Before adding a component, identify the specific requirement the current candidate misses or the supported bottleneck, and explain how to verify that the addition helps. Surface conflicting requirements if no candidate meets them.

A candidate that breaks a hard constraint is rejected, not scored lower; it returns only if the constraint's owner changes the constraint. Do not use numeric weights the evidence cannot support. For each trade-off, name the side given up and the scenario that pays for it. Before adding a module, layer or abstraction, apply the deletion test: if removing it makes its complexity disappear rather than reappear in its callers, it is a pass-through and stays out, unless a project or team stack rule requires that layer. Add an interchangeable interface only when two real implementations exist in this scope; one implementation and a hypothetical second is not a reason.

## Challenge and close the decision

- Try to falsify the recommendation with a relevant counterexample or failure case. Trace each confirmed in-scope requirement and applicable hard constraint to a design choice and its evidence or acceptance check. Retain agreed behavior when comparing simpler options.
- Investigate the assumptions most likely to change the result. If facts leave a consequential user decision open, ask a focused question with your recommendation, alternatives and implications. If the unknown is empirical, use available evidence or propose a bounded check that can distinguish the choices. Reassess the affected choice when its answer changes.
- Keep a recommendation conditional while a material uncertainty can change the choice. Identify the missing fact or decision and which work depends on it. Once evidence supports the smallest feasible design against the confirmed goals and the remaining unknowns would leave the choice intact, finish this design slice. Reuse settled answers and keep additional analysis proportional to the decision.

Use the existing design record for one recommendation, the key trade-offs and assumptions, the evidence or checks that support it, and any genuinely pending decision. When future scale could change the choice, record an observable trigger for reassessment. Also record the evidence that would reverse the choice. Write a separate decision record, in the project's existing format, only when all three hold: the choice is costly to reverse, a later reader would be surprised without the reason, and a credible alternative was rejected. Otherwise a line in the design record is enough. State the limits of estimates and bounded tests. Design agreement and validation evidence support their respective claims, and later implementation and deployment follow the project's existing authority and acceptance rules.
