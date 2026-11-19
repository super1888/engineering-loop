# Shared development core

**ID:** `dev.core` · **Status:** available existing guidance.

Use for the current development slice after the [entrypoint](../../SKILL.md) prerequisites. Retain the common challenge, effective project conventions and required full reads; this shared base does not select a new technology or authorize another phase. Inspect the [risk index](risks.md) and apply only its matching bodies.

**Challenge focus:** Which contracts, callers and state boundaries change, and what relevant failure or recovery example would contradict the proposed repair?

## Slice and scope

Inspect the incumbent behavior, related tests, callers, and boundaries. Select the smallest complete user behavior that can be verified. Reuse the repository's architecture and commands; do not introduce dependencies, abstractions, or a parallel framework without a current reason.

Distinguish accepted features, engineering work required for their correctness, and optional improvements. An unstated implementation detail is not automatically out of scope; necessary permissions, validation and recovery must not be dropped to keep a diff small. For a new dependency, service, general abstraction or parallel implementation, establish the current need, why existing mechanisms are insufficient and the maintenance cost. Local choices inside settled boundaries can proceed; consequential new scope or architecture choices need the developer's decision. Report material unrelated findings without automatically adding them to this task.

Bound unfinished work by what can be explained, reviewed and verified together, not by a fixed line count. Verify the first representative slice before multiplying similar implementations: trace actual calls, model conversions and ownership against the selected architecture, as well as checking behavior. Matching folders or class names is insufficient. Reuse approved local patterns; do not add empty layers to imitate a reference. If the next slice depends on an unresolved contract or a failing relevant check, resolve that dependency first; independent authorized work can continue. Use [project.md](../project.md) when inherited conventions, ownership or enforcement are missing.

## Diagnosis and correction

For a bug, reproduce the symptom and preserve a regression that distinguishes it. Form a falsifiable hypothesis, run the smallest useful experiment, then modify the relevant cause. Classify code, configuration, environment, dependency, test, and misunderstood-requirement failures before choosing a fix. A number of failed attempts is not proof of bad architecture.

For a user correction, infer its intended scope from the request and existing decisions; clarify only consequential ambiguity. Check relevant callers or analogous implementations for the same demonstrated cause, fix applicable occurrences within scope, and report material remaining ones. Do not turn a local preference into a global rule or expand this check into a repository audit. If the correction should govern future tasks, use [learning.md](../learning.md) to place it in a durable implementation, check or discoverable convention rather than relying on conversation memory.

## Checks and evidence

For testable behavior changes, use red → green → refactor where it provides useful feedback. Derive expected behavior from an accepted example, independent calculation, or contract. Avoid tests that simply repeat the implementation. A copy-only edit may need consistency checks rather than unit tests.

Explain justified redundancy by the failure it addresses and its maintenance cost. Preserve required recovery and authorization behavior when simplifying. Reconcile source inventories for broad replacements. Raise material contract or data-impact changes as concrete deltas; continue authorized work elsewhere.

Use [verification.md](../verification.md) for applicable evidence boundaries and checks; development self-checks need not wait for a project-wide testing phase.

## API contract inventory

When adding or changing a Controller route, locate the repository's API operation inventory and its contract check. If a checked-in OpenAPI operation manifest is part of that contract, update it with the route and run the owning contract test. Use the project's actual paths and commands; if the inventory is generated instead, follow its existing check rather than creating a new manifest.

## Accepted deferrals

For an accepted deferral with meaningful future cost, record its reason, affected behavior and a condition for revisiting it in the existing tracker. Do not label incomplete acceptance as harmless debt or create a debt entry for every minor imperfection.
