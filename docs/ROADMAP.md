# Roadmap

## v0.1.7: unreleased comment-only description protection

- Reject a description whose first nonblank character starts a YAML comment inside the actual frontmatter; a body example cannot supply the missing value.
- Extend the existing metadata regression with comment-only values and preserve quoted descriptions starting with a literal hash. The check remains scoped to this repository's frontmatter layout.

This is a local distribution-check correction, not a published release or a model-behavior improvement.

## v0.1.6: unreleased blank-description protection

- Reject a description containing only spaces or tabs inside the actual frontmatter; a body example cannot satisfy it.
- Extend the existing metadata regression and preserve descriptions with extra leading spacing. This check remains scoped to this repository's frontmatter layout, not a general YAML validator.

This is a local distribution-check correction, not a published release or a model-behavior improvement.

## v0.1.5: unreleased archive file-identity protection

- Reject existing output files that are hardlinks to the supplied license or any skill source file before opening the ZIP.
- Use the standard library's file-identity check; verify preserved input bytes for the entrypoint, a nested reference and the external license alongside normal archive controls.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.4: unreleased archive input protection

- Reject an archive output that resolves to the supplied license, alongside the existing skill-source protection.
- Extend the source-preservation regression to the external license; normal complete and deterministic archive checks remain in place.

This is a local packaging correction, not a published release or a model-behavior improvement.

## Unreleased evaluation tooling correction

- Invalidate a blinded review when its referenced task context changes; reuse the context frozen in the packet and preserve line-ending-only conversions.
- Reject private arm mappings inside the review directory or its descendants during preparation and gating.
- Treat a silent nonzero backend or form subprocess as a failed routing check; retain its exit code instead of an empty failure value.
- Require completion markers after the routing and convention amount checks' independent assertions; an early zero exit cannot substitute for completed checks.
- Require nonempty, unskipped native public-test reports in routing records and the convention comment control; the form report must execute at least the fixture's two cases.
- Build convention-trial patches from each workspace's frozen Git baseline, so later repository template changes are not attributed to the implementing agent.
- Record routing-trial file lists and patches against the prepared Git baseline, retaining staged changes alongside unstaged edits.
- Reject `SystemExit` during candidate imports in the receipt and asynchronous-import oracles, so an early zero exit cannot bypass their checks; preserve the original exit in the diagnostic cause.

These are regression-tested evaluator corrections, not changes to the distributed skill or evidence of model-quality improvement.

## v0.1.3: unreleased description gate correction

- Reuse the frontmatter boundary for description validation; a documentation example cannot substitute for a missing skill description.
- Preserve the valid-header control and version-mismatch regressions in the same focused distribution check.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.2: unreleased metadata gate correction

- Compare the plugin version with the skill's actual `metadata.version` in the repository's YAML layout; body examples and description text cannot satisfy the gate.
- Keep a focused regression for mismatched metadata masked by documentation, plus a valid-metadata control with an unrelated example version.

This is a local packaging correction, not a published release or a model-behavior improvement.

## v0.1.1: unreleased coordination correction

- Route authorized delegation and ongoing goals to the existing collaboration guide.
- Keep a verified slice distinct from goal completion; reconcile terminal contributors, continuation corrections and explicit pauses within existing authorization.
- Preserve finite-task stopping and the existing live-handle monitoring boundary. No scheduler, runtime service or fixed agent team is added.

This is a local guidance revision, not a published release. Packaging checks and checkpoint exercises do not establish live orchestration quality or a general improvement.

## v0.1: usable public draft

- A portable entrypoint and focused lifecycle references.
- English and Simplified Chinese documentation.
- Claude Code plugin, Skills CLI, and manual/offline distribution.
- Reproducible packaging checks and public behavioral scenarios.

## Next: evidence before expansion

1. Repeat the supplied receipt and copy trials, then run remaining behavioral cases across Claude Code and Codex, including negative triggers.
2. Publish reproducible, sanitized transcripts and conditions; include failures.
3. Collect examples from small fixes, legacy systems, libraries, data pipelines, and application work.
4. Measure unnecessary questions, context reads, missed requirements, and human review burden.
5. Revise or remove rules that do not earn their cost.

## Community and discoverability

Keep the install path short, show realistic examples, publish honest evaluation reports, and resolve reported friction. Add ecosystem listings only where relevant and with maintainers' contribution rules. No unsolicited promotion, manufactured testimonials, or promises of star growth.

Potential later work: tested host adapters, optional explicit-only distribution, additional language docs, and a lightweight evaluation runner. Each needs a demonstrated use case before adding runtime dependencies or orchestration.

The project connection guide now locates business rules, shared ownership and active checks without imposing a new tracker. The receipt oracle and isolated fixtures enable local trials; they do not establish production quality, native host discovery, cross-project learning or a speedup. A real project pilot should retain accepted examples, an actual failure/regression and measured rework/review effort before expanding the generic rules again.
