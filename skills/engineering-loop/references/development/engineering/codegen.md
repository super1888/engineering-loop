# E4 Tooling and generated code

**ID:** `dev.engineering.codegen` · Execution baseline available; project generation policy remains bound locally.

## Scope and inputs

Use for an accepted generator, generated-contract or generated-source change. Identify the maintained input/schema, generator/version/configuration, owned output inventory, legitimate manual exceptions and affected consumers. A file that merely resembles generated code is not enough to decide its authority.

## Execute

1. Locate the real generation command and source of truth before editing output. Fix the authoritative input or generator when it owns the behavior; preserve explicitly maintained manual exceptions.
2. Reproduce generation in the intended directory/runtime. Check required command results and confirm that the new output actually exists before dependent verification.
3. Reconcile the expected output set with created, changed, removed and excluded files. Preserve unrelated user work; do not remove files solely because the generator did not list them without checking ownership.
4. Check relevant types, serialization and public contracts through actual consumers; use [data fidelity](../rules/data-fidelity.md) where generated conversions can lose meaning.
5. Demonstrate reproducibility when it is part of the generator contract, accounting for declared timestamps/environmental inputs. Do not impose byte identity on outputs whose accepted format allows variation.

## Verify and deliver

Run the owning generation/contract checks and a representative affected consumer. Compare the correct source/output version; passing tests against unapplied or stale generated files do not verify this change. Do not add a parallel operation inventory when the project already generates one.

Record source, generator identity, affected output set, consumer evidence and unrun limits through the [delivery record](../delivery.md).

## Project bindings

Bind generator versions, regeneration commands, source/output ownership, deterministic properties and checked-in artifact policy. No scaffold, language or additional generation framework is required by this baseline.
