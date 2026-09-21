# Preserve evidence-based lessons, and retire bad rules

Use this after a demonstrated failure, repeated friction, or an explicit retrospective. A successful routine edit does not need a new policy.

Route the correction to its narrowest useful home:

| Observation | Preferred correction |
|---|---|
| Reproducible behavior bug | Regression test and relevant implementation |
| Mechanically detectable violation | Existing lint, configuration validation, or CI |
| Hard-to-find or stale facts | Navigation/effective-document correction |
| Business or architecture choice | Project decision with reason and scope |
| Repeated cross-project workflow failure | Skill candidate with an evaluation case |

Check whether a suitable safeguard already exists but is unwired or broken before adding another. A candidate records its trigger, applicability, expected benefit, cost, counterexample, and review/retirement condition. One incident can justify a local fix without justifying a universal prohibition.

Evaluate whether the change prevents the original failure without disrupting a simple or unrelated task. Remove or narrow ineffective instructions. Preserve privacy when sharing examples. Do not autonomously broaden permissions, publish project experience, or promote a local policy to global scope.
