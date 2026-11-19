# B1 API and contract changes

**ID:** `dev.backend.api` · **Status:** available execution baseline; project naming, response format and packages remain bound to the actual contract.

## Scope and inputs

Use for a changed route, request/response model, validation or error meaning. Identify its callers, accepted examples, current API/schema inventory, permission boundary and owning contract command. A frontend label change does not enter this body.

## Execute

1. Trace the current request through transport validation, authorization, service effects and response mapping; locate the maintained owner rather than imposing new layers.
2. Derive runtime input checks from the accepted request shape. For an object contract, reject malformed JSON, null, arrays and scalar values before field access or protected writes. Preserve legitimate array/scalar endpoints and the project's unknown-field policy.
3. Preserve distinctions between missing, null, empty and zero when the contract gives them different meanings. Apply [R1](../rules/data-fidelity.md) if values cross a precision/serialization boundary and [R2](../rules/access.md) if access changes.
4. Change the authoritative contract and affected consumers together. For Controller operations, apply the [API inventory gate](../core.md#api-contract-inventory); follow its actual generation/update process instead of creating a parallel manifest.
5. Reuse established error/status semantics. Resolve a consequential behavior conflict before dependent implementation; do not invent a universal response envelope or convert a required rejection into success.

## Verify

- Exercise an accepted request and the relevant malformed/type/boundary rejection; check both the response and absence of unintended protected writes.
- Run the owning contract check and affected consumer example. A registered route or schema-valid payload alone does not prove the producer/consumer combination; use [I1](../scenarios/integration.md#i1-interface-alignment) only when that boundary is involved.
- Reuse unaffected evidence and distinguish mocked handler checks from actual service integration through [verification](../../verification.md).

## Deliver and bind

Record the changed operations, accepted/rejected examples, contract version, affected callers and actual check outcomes using [delivery evidence](../delivery.md). Bind endpoint naming, DTO/error conventions and API libraries to maintained project references; those team-specific choices remain pending here.
