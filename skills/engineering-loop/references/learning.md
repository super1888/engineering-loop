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

For a material lesson, keep a short record in the existing project knowledge source: observed trigger and evidence; root cause; why the current checks missed it; correction and safeguard; applicability and owner; reproduction/check and its result. A useful safeguard rejects the original failure and permits a valid nearby case. If that has not been demonstrated, label the lesson a candidate rather than a proven prevention.

Transfer the smallest useful artifact: a regression for a business bug, a check or template for a recurring stack-specific defect, or skill guidance plus a behavioral case for a repeated workflow failure. Keep confidential project facts local. A new project selects relevant lessons through [project.md](project.md), verifies their assumptions and runs their safeguards; copying prose alone is not evidence of adoption. Existing authorization may cover this work, but does not authorize publishing private experience or installing global rules.

Evaluate whether the change prevents the original failure without disrupting a simple or unrelated task. Remove or narrow ineffective instructions. Preserve privacy when sharing examples. Do not autonomously broaden permissions, publish project experience, or promote a local policy to global scope.

Assess an iteration with observable outcomes: missed acceptance items, escaped defects/rework, unnecessary questions, human review effort and elapsed delivery time when actually measured. Record task size and environment so unlike tasks are not treated as a speed comparison. Missing measurements stay unknown; more rules, tests or generated code are not evidence of improvement.
