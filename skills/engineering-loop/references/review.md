# Review the change against intent and engineering evidence

Fix the review target: relevant revision/diff, effective requirement, known pre-existing changes, and available verification. A review request alone does not authorize edits or release.

Review two axes: (1) matches the accepted behavior and scope, including missing work; (2) preserves relevant engineering invariants such as authorization, data integrity, state transitions, compatibility, and recoverability. Assess unnecessary complexity against current requirements rather than file count alone.

If evidence challenges the specification itself, distinguish that dispute from implementation nonconformance. Report the rule, conflicting scenario and impact; do not force a known-bad behavior merely to match text or silently rewrite the rule. For concurrent work, use the decision and propagation path in [collaboration.md](collaboration.md); review an identifiable slice rather than repeatedly interrupting unfinished edits.

For structural changes, inspect the cost of the next plausible change: duplicated business rules, edits spread across unrelated modules, unused extension points, and competing old/new paths. Identify the authoritative implementation and relevant checks. Remove superseded paths when in scope and safe; if compatibility requires both, record the owner and retirement condition. Do not turn a local review into an unsolicited repository-wide refactor.

Inspect test changes alongside implementation changes. A changed expectation needs an accepted behavior change or a demonstrated correction to the test. Timing fixes should wait for observable state; increased timeouts need an environment or workload reason and must not hide a product latency regression.

Report actionable findings with location, triggering condition, consequence, and evidence. Distinguish a demonstrated defect from a hypothesis or preference. Reconcile findings after fixes instead of generating endless fresh opinions. An independent reviewer is useful when available and authorized; neither multiple agents nor agreement is proof of correctness.

Conclude with findings/dispositions and the evidence boundary. No findings in a diff is not a claim that the entire product is defect-free.
