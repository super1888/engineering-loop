# I3 Preserve data across representations

**ID:** `dev.integration.data-representation` · **Status:** available execution baseline; domain value policies remain pending.

Use for identifiers, amounts, time values, enums or serialization crossing actual consumers. An unchanged local value does not require a new representation. Apply [R1 data fidelity](../rules/data-fidelity.md) to the affected round trip.

## Inputs

Identify the originating value and independently expected meaning, schema/type/range, actual serializers and consumers, saved examples, and relevant artifact/configuration versions. Reuse accepted currency/rounding, timezone and missing-value decisions; a language type alone cannot settle them.

## Execute

1. Map the value from producer through transport, client/widget state, persistence and any later consumer involved in this change. Find conversions and defaults that may lose identity or meaning.
2. Establish accepted examples for relevant large/range-boundary values and absent/null/zero distinctions. Investigate missing facts before asking a consequential domain-policy question.
3. Preserve exact identifiers through every affected representation using the established compatible contract. Do not silently coerce a large ID to an inexact number or turn unknown data into zero.
4. For amounts or time, apply the project's confirmed scale/rounding and timezone semantics at the correct boundary. Do not infer currency, units, locale or date meaning from formatting alone.
5. Update affected schema/types/examples and their real consumers together; starter examples must identify usable resources when the flow requires them.

## Verify

- Round-trip independently known values through the actual changed request/state/storage or consumer path and compare exact identity or accepted semantic equivalence.
- Check only relevant null/zero, precision, range or time-boundary examples. Do not impose an unrelated language/timezone matrix on a local edit.
- Separate simulated serialization checks from real consumer/persistence integration. Retain untested representations and unknown domain decisions explicitly.

## Deliver

Record the accepted value policy, affected representations, artifact identity, expected/observed examples and limitations through the existing [delivery record](../delivery.md). Keep authoritative schema and business decisions in their maintained locations.

## Team bindings — pending

Bind currency/rounding, units, timezone, enum evolution and serialization conventions. No default business policy or universal number-to-string conversion is introduced.
