# Turn intent into a bounded behavior contract

Investigate facts available in the project before asking the user. Separate current behavior, desired behavior, assumptions, and unknowns. Agree the current slice, not every hypothetical future feature.

Use concrete normal, rejected, and uncertain-result examples. For stateful behavior, consider only relevant cases such as duplicate submission, missing data, partial failure, permissions, and refresh recovery. Do not turn a coverage checklist into mandatory new product features.

Translate domain-expert explanations into only the terms, invariants, state transitions and permissions needed for this slice. Have consequential rules grounded in accepted examples with inputs, actions and observable outcomes; distinguish an expert's confirmed rule from an agent's proposal. Use boundary examples to expose ambiguity (for example, ordered 100, received 60, next receipt 50). Do not silently choose a business policy or treat an unanswered question as acceptance. Technical implementation choices need not be sent back to the expert.

Ask a round of independent decisions whose prerequisites are already settled. Each has options, a recommendation tied to the user's goal, cost, and reversibility. Dependent questions belong after their prerequisite. Respect a preference for one question at a time. Keep optional future decisions out of this slice.

Record the accepted outcome, non-goals, meaningful constraints, examples, affected boundaries, and verification approach in the existing source of truth. A short conversation can suffice for a small change. Where a requirement spans independently verifiable capabilities, propose a small capability/dependency map before planning implementation.

Keep a lightweight connection from each consequential rule to its implementation boundary and acceptance check; existing test names, issue links or contract identifiers can suffice. When a rule changes, update the affected examples and checks explicitly. Do not create a separate traceability database for a small feature.

Stop clarifying when no unresolved material decision changes this slice's acceptance. Low-impact reversible implementation details can proceed under existing authorization. If the user asks for design only, end with the design; do not begin implementation.
