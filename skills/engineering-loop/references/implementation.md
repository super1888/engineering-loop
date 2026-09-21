# Implement and diagnose in slices

Inspect the incumbent behavior, related tests, callers, and boundaries. Select the smallest complete user behavior that can be verified. Reuse the repository's architecture and commands; do not introduce dependencies, abstractions, or a parallel framework without a current reason.

Bound unfinished work by what can be explained, reviewed and verified together, not by a fixed line count. Verify the first representative slice before multiplying similar implementations. If the next slice depends on an unresolved contract or a failing relevant check, resolve that dependency first; independent authorized work can continue. Use [project.md](project.md) when ownership or enforcement is missing.

For a bug, reproduce the symptom and preserve a regression that distinguishes it. Form a falsifiable hypothesis, run the smallest useful experiment, then modify the relevant cause. Classify code, configuration, environment, dependency, test, and misunderstood-requirement failures before choosing a fix. A number of failed attempts is not proof of bad architecture.

For testable behavior changes, use red → green → refactor where it provides useful feedback. Derive expected behavior from an accepted example, independent calculation, or contract. Avoid tests that simply repeat the implementation. A copy-only edit may need consistency checks rather than unit tests.

For stateful or asynchronous changes, identify operation ownership, transitions, idempotency, result-unknown behavior, and recovery. Consider real boundary behavior when transactions, caches, queues, authentication, or external services interact. Verify actual scheduling rather than equating configured threads with throughput.

Explain justified redundancy by the failure it addresses and its maintenance cost. Preserve required recovery and authorization behavior when simplifying. Reconcile source inventories for broad replacements. Raise material contract or data-impact changes as concrete deltas; continue authorized work elsewhere.
