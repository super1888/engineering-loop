# E1 Public libraries and SDKs

**ID:** `dev.engineering.libraries` · Execution baseline available; project package policy remains bound locally.

## Scope and inputs

Use for an accepted public API, shared package or SDK change. Identify the maintained public exports, affected consumer/version promises, package format/runtime and actual build/test commands. A helper internal to one module does not automatically need a public library or release process.

## Execute

1. Trace a representative real caller and the documented import/initialization path. Separate public contract changes from private implementation details.
2. Implement the requested slice using the existing exported types, error/cancellation semantics and ownership rules. Preserve compatibility that the project actually promises; surface a consequential breaking change before dependent work.
3. Update affected examples, generated types and documentation at their authoritative sources. Do not add duplicate adapters or expose internals merely to make a sample compile.
4. When package output changes, build/pack locally using the repository's mechanism and exercise the affected entry from that output. Source-tree imports alone cannot establish what the consumer receives.
5. Apply [data fidelity](../rules/data-fidelity.md), [access](../rules/access.md) or [SDK transport](../rules/sdk-transport.md) only when the changed boundary triggers it. A local pack is not publication authority.

## Verify and deliver

Check accepted and rejected inputs through a representative consumer; include an existing-version consumer only where compatibility is promised. Identify package bytes/version and supported runtime for a package-level claim. For an internal-only change, use its relevant caller/check rather than requiring unrelated packaging.

Record the changed public surface, actual consumer result, compatibility limits and artifact through the [delivery record](../delivery.md). Keep unrun platform/provider behavior separate.

## Project bindings

Bind the package manager/format, export conventions, version policy, supported runtimes, example location and owning checks. No package namespace, repository layout or publication registry is prescribed here.
