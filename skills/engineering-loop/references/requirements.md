# Turn intent into a bounded behavior contract

Investigate facts available in the project before asking the user. Separate current behavior, desired behavior, assumptions, and unknowns. Agree the current slice, not every hypothetical future feature.

Use concrete normal, rejected, and uncertain-result examples. For stateful behavior, consider only relevant cases such as duplicate submission, missing data, partial failure, permissions, and refresh recovery. Do not turn a coverage checklist into mandatory new product features.

Ask a round of independent decisions whose prerequisites are already settled. Each has options, a recommendation tied to the user's goal, cost, and reversibility. Dependent questions belong after their prerequisite. Respect a preference for one question at a time. Keep optional future decisions out of this slice.

Record the accepted outcome, non-goals, meaningful constraints, examples, affected boundaries, and verification approach in the existing source of truth. A short conversation can suffice for a small change. Where a requirement spans independently verifiable capabilities, propose a small capability/dependency map before planning implementation.

Stop clarifying when no unresolved material decision changes this slice's acceptance. Low-impact reversible implementation details can proceed under existing authorization. If the user asks for design only, end with the design; do not begin implementation.
