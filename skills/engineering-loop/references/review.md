# Review the change against intent and engineering evidence

**Challenge focus:** Which effective requirement and identifiable diff support the finding, and does the proposed correction preserve legitimate alternatives?

Fix the review target: relevant revision/diff, effective requirement, known pre-existing changes, and available verification. A review request alone does not authorize edits or release.

Review two axes: (1) matches the accepted behavior and scope, including missing work; (2) preserves relevant engineering invariants such as authorization, data integrity, state transitions, compatibility, and recoverability. Assess unnecessary complexity against current requirements rather than file count alone.

If evidence challenges the specification itself, distinguish that dispute from implementation nonconformance. Report the rule, conflicting scenario and impact; do not force a known-bad behavior merely to match text or silently rewrite the rule. For concurrent work, use the decision and propagation path in [collaboration.md](collaboration.md); review an identifiable slice rather than repeatedly interrupting unfinished edits.

For structural changes, inspect the cost of the next plausible change: duplicated business rules, edits spread across unrelated modules, unused extension points, and competing old/new paths. Identify the authoritative implementation and relevant checks. Remove superseded paths when in scope and safe; if compatibility requires both, record the owner and retirement condition. Do not turn a local review into an unsolicited repository-wide refactor.

Inspect test changes alongside implementation changes. A changed expectation needs an accepted behavior change or a demonstrated correction to the test. Timing fixes should wait for observable state; increased timeouts need an environment or workload reason and must not hide a product latency regression.

Report actionable findings with location, triggering condition, consequence, and evidence. Distinguish a demonstrated defect from a hypothesis or preference. Reconcile findings after fixes instead of generating endless fresh opinions. An independent reviewer is useful when available and authorized; neither multiple agents nor agreement is proof of correctness.

Conclude with findings/dispositions and the evidence boundary. No findings in a diff is not a claim that the entire product is defect-free.

## Procedure

Scale to risk, judged by what the change touches (authorization, stored data, external effects, removed checks), not its size. A small low-risk diff gets one careful pass through these steps and no added reviewer; independent review stays limited to the cases in [grill.md](grill.md) and [collaboration.md](collaboration.md).

1. **Pin the comparison.** Name the base and head revision or dirty-file snapshot, and confirm the diff is non-empty and the intended one before reading it.
2. **Gather the yardsticks:** the effective requirement, and the project instruction and standards files whose scope covers each changed file. If no requirement exists, say so and skip step 4 rather than inferring one from the code.
3. **Read as an outsider.** The author's summary, rationale and reported results are unverified claims: check them against the diff, and never lower a severity because a shortcut was explained. Where the host provides an independent reviewer and the checkpoint warrants one, give it only the brief, base and head, not the session history or the author's reasoning; it does not modify the checkout. Otherwise run the passes yourself in sequence and state that no independent check was made.
4. **Requirement pass.** Report requirements that are missing or partial, behavior nobody requested, and requirements implemented wrongly, each citing the requirement. Where the requirement is silent, what a reasonable user would expect counts; silence is not permission.
5. **Rules and defects pass.** A rule violation cites the exact rule and its file, and the rule must be in scope for the changed file. A defect names the input or state that triggers it.
6. **Validate each candidate separately** before reporting: re-read the cited code with its callers and guards, and confirm the trigger is reachable and the consequence real. Drop what is refuted and give the count. Keep an unsettled candidate only if its consequence would be serious, labeled as a hypothesis with the check that would settle it.
7. **Do not report** issues that predate the diff (note a serious one separately as pre-existing), what the project's linter, formatter or type checker already enforces, preferences no documented rule backs, speculation about an input or state you cannot show to occur, or a rule the code suppresses with a stated reason the project accepts.
8. **Report the two passes side by side**, not merged into one ranking, so a clean result on one does not mask the other. List what you declined to judge and why: behavior outside the requirement, requirements not verifiable from this diff, evidence you could not read. State an empty list as empty. Missing or unreadable evidence is a reported gap, neither a pass nor a refutation.

When the change touches authentication, authorization, secrets, input parsing, query or command construction, deserialization or a trust boundary, add [security-review.md](security-review.md).
