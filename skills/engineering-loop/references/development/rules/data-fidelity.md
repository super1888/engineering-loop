# R1 Data fidelity across representations

**ID:** `dev.risk.data-fidelity` · **Status:** available existing boundary guidance.

**Trigger:** A value crosses API, language, browser, widget, serialization or saved-example boundaries and its identity or precision may be lost. First establish the actual type/range and affected consumers. This rule does not invent a domain's amount, rounding or time policy.

When identifiers can exceed a consumer's exact numeric range, verify their round trip through APIs, browser state, widgets and saved examples. Keep the value exact with a string or explicit large-integer handling, and check that starter data names a usable resource rather than a placeholder ID.

**Nearby exception:** A label-only edit with unchanged value flow does not require a new numeric representation or a serialization matrix.

**Verification:** Use the relevant cross-boundary examples in [verification.md](../../verification.md), with an independently known expected value and actual affected consumers. Keep untested representations explicit. Project-specific amount, time and schema conventions remain with their maintained source.
