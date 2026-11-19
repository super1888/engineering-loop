# I1 Align an actual producer/consumer contract

**ID:** `dev.integration.contracts` · **Status:** available execution baseline; team protocol bindings remain pending.

Use when an accepted change crosses an actual API boundary. Two independent edits with unchanged contracts need no integration campaign. This baseline does not authorize changing a business rule to make producer and consumer agree.

## Inputs

Identify the producer and affected consumers, their artifact/revision and configuration, the maintained schema/API inventory, and accepted request/result examples. Establish which side owns validation and error meanings. Read [project guidance](../../project.md) only for missing or conflicting ownership/conventions.

## Execute

1. Trace the actual request construction, transport, decoding and consumer use. Compare field names, types, optional/absent/null values, enums, pagination and errors only where this change affects them.
2. Reconcile a discrepancy against the effective contract and independent accepted examples. A current implementation or generated type alone cannot decide a disputed requirement.
3. Update the owning contract and affected producer/consumer together. Preserve the existing API inventory/generation/check mechanism described in [core](../core.md#api-contract-inventory); do not add a parallel manifest.
4. Exercise the actual consuming path in the intended test environment. A schema check and a direct request can support narrower claims but do not prove the browser/service combination.
5. Apply [R1](../rules/data-fidelity.md) for representation loss and [R2](../rules/access.md) for actor-dependent behavior only when those boundaries are involved.

## Verify

- Use a normal accepted example and a relevant rejected or missing-value example from the maintained agreement; compare the producer result with what the real consumer observes.
- For rejection, verify the expected error meaning and any required absence of business effects. Do not rewrite assertions to match an incorrect response.
- Distinguish generated/schema validity, adapter tests, actual integration and user acceptance. Record an unavailable consumer/environment as unrun.

## Deliver

Record the reconciled contract/version, affected producer/consumers, checks and remaining compatibility gaps through the existing [delivery record](../delivery.md). Link authoritative documents rather than copying them into every task.

## Team bindings — pending

Bind actual API examples, schema/client-generation policy, compatibility policy, owners and contract-test commands here or through maintained project references. No universal response envelope or generation tool is supplied.
