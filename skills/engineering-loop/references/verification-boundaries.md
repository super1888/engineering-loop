# Verify specialized boundaries when they apply

Use the applicable section selected by [verification.md](verification.md). These are scoped checks, not a checklist for every change; retain each section’s stated nearby exception.

## Split transactions

For a reservation committed separately from a work item, use the real database isolation level and independent connections to check commit-unknown exceptions, same-key contenders, and rollback/retry orderings. Inspect the resulting reservation, work item, and publication record together; mock-only tests cannot establish whether a release is safe or an orphan is eventually settled. A single atomic transaction with a confirmed rollback does not need this split-transaction gate.

## SDK transport after dependency changes

When excluding or replacing an SDK's transitive dependency, exercise the real SDK through the affected request path with the resulting classpath. Request serialization and mocked clients can pass while an interceptor fails before transport. A small loopback server can verify local transport without a paid provider call; keep the security constraint intact and distinguish this check from provider acceptance. An unaffected pure serialization change does not require a transport probe.

## Direct-upload storage quotas

When a delegated upload writes directly to object storage, verify quota against bytes the storage accepts, including unfinished objects. Declared size and a per-request proxy limit do not by themselves bound retained storage usage.

## Cross-user and role access

For a workflow shared by several users or roles, follow the actual actor through downstream services. A project-level membership check does not prove that an owned task or resource can be read by another authorized member; verify the cross-user path and an unauthorized control without relaxing the public ownership boundary.

## Rendered visual and responsive defects

For a visual or responsive defect, reproduce the reported viewport or aspect ratio and inspect the rendered result as well as relevant geometry. Use the project's existing browser/design checks; passing overlap or overflow assertions does not establish visual quality. Include a nearby unaffected layout when useful, without imposing a universal viewport matrix or treating a smaller viewport as actual browser zoom. Scope evidence to the rendered asset and animation state.

## Accessibility scans and status feedback

For accessibility scans, distinguish definite violations, incomplete checks, and manual findings. Inspect incomplete results at the affected element before claiming the scanned scope passed; uncertain contrast over an image does not by itself justify a color change. Check the rendered role and accessible name of labeled wrappers, including UI library components: an `aria-label` attribute on a generic container does not establish a named group. Where the name matters, assert the intended role and name rather than the attribute alone. For changing status messages, also inspect live-region text and `aria-busy` timing; a role/name assertion alone does not prove a screen reader announced the update.

## Image input with structured output

When a business invocation combines image input with strict JSON Schema output, provider/model capability flags and a successful text-only connection test do not prove that combination works. Before activating that usage, exercise the intended adapter's actual image-plus-schema request with representative samples; check provider acceptance, parsed structure and task-relevant semantics. A text-only usage needs verification of its own text contract, not a multimodal probe.

## Incomplete media evidence and abstention

Test abstention as well as defect detection when evidence has known gaps. A structurally valid, high-scoring model verdict cannot establish audio or temporal quality from static frames. Where unobserved dimensions block delivery, enforce that evidence limit in the existing server adjudication rather than relying only on prompt wording, and preserve explicit defect failures. Supply known duration bounds for time-based findings and verify outputs through the actual consumer contract; schema acceptance alone may allow an invalid interval. Keep workflows with complete evidence scoped to their own contract.

## Failed review after artifact creation

If review fails after an artifact has been produced, verify that the established failure policy still blocks approval while retaining permitted diagnostic output and a usable failure report. An exception that discards the artifact may defeat recovery without improving the gate; do not change a blocking policy into approval or human-review eligibility just to retain evidence. Keep intentionally disposable or unsafe output governed by its own retention contract.

## Generated media and document properties

For generated media or documents, a successful processor exit and a nonempty file do not establish the agreed output properties. Check relevant properties in the actual runtime, such as supported subtitle glyphs, duration or audio tracks, and inspect the rendered result where needed. A nearby metadata-only change does not require an unrelated rendering or language matrix.
