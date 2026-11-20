# 04 Testing and acceptance · 测试与验收

## Enter

Use after the entrypoint's MCP gate when the current deliverable is a test result, independent review, integration verification or business acceptance. A review-only request remains read-only unless edits are separately authorized.

## Inputs

Identify the accepted examples and scope, artifact/revision and configuration, relevant environment, changed boundaries and available prior evidence. Reuse unchanged valid checks; do not infer coverage from a successful command or task status alone.

## Execution and focused references

Read [verification.md](../verification.md) to match checks to claims and select only applicable sections of its boundary companion. For a concrete diff review, also read [review.md](../review.md); for visible or interactive behavior, read the relevant [ui.md](../ui.md) guidance. Use [collaboration.md](../collaboration.md) when independent contributors or integrated ownership need coordination.

Apply the [common challenge](../grill.md) to the claim, independent expected result and likely failure boundary. Investigate missing facts before asking; resolve a material acceptance dispute with its authorized owner rather than deriving expectations from the implementation.

## PMS

Follow [pms.md](../pms.md) when applicable. Link the actual version, covered scope, findings and acceptance record to the relevant deliverable. Check planned coverage and dependencies before advancing a tracked task; no cards or missing links do not prove no work remains. Keep testing as a work phase distinct from the actual board's review/completion transitions.

## Deliverables

Record passed, failed and unrun checks with commands or method, artifact/environment identity, covered scope, findings and unresolved limits. Use existing test and acceptance records; do not fabricate human acceptance or require a new report for every small check.

Keep the pre-release defect tracking and test acceptance record in stage 04. Link the tested build, relevant case and retest evidence, open findings and actual acceptance decision so release and operations can reference that record. When a new structured record is needed and the project has no applicable format, adapt the [test and acceptance template](../../templates/acceptance-record.md).

## Exit and return

Required evidence and authorized acceptance must support the claimed result. Classify failures before returning to [development](03-development.md), a bounded [requirement decision](01-requirements.md), or the affected environment/check. Preserve intended assertions. Preparation or [release](05-release.md) proceeds only within existing authority and project stop points; testing alone does not authorize publication.
