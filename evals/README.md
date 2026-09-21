# Behavioral evaluation protocol

`cases.json` is a set of **unexecuted scenario specifications**, not a model runner or a pass-rate claim. A fixture description tells a tester what raw project facts to provide; it is not an executable repository fixture yet.

For each case, build the minimal isolated fixture, provide the user's request and the skill to the host, and retain the actual transcript/artifacts. Keep expected outcomes with the evaluator, not in the implementation prompt. Use the same starting state and acceptance for a no-skill baseline when comparing outcomes. Do not run production operations or publish user data.

Record host/version, model/configuration, skill revision, fixture revision, observed tool effects, findings, unnecessary questions/reads, relevant cost/time, and passed/failed/unrun expectations. Judge behavior and artifacts, not phrase matching. Repeat before generalizing; include failures and relevant counterexamples.

Priority cases: negative-copy, resume-stale, batch-dependent, test-integrity, inventory-loss, project-adapter. These target the actual risk of an engineering skill taking over unrelated work or creating false confidence.

The repository's Python checks validate distribution only. Cross-platform CI does not execute these behavioral scenarios. A future runner should make the distinction explicit.
