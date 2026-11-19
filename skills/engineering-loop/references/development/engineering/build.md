# E3 Build and dependency changes

**ID:** `dev.engineering.build` · Execution baseline available; project build/dependency policy remains bound locally.

## Scope and inputs

Use for a changed build graph, dependency/lockfile, resource packaging or artifact behavior. Identify the affected module, actual manager/tool versions, owning manifest/lockfile, runtime entrypoint and required project gates. A local source edit does not authorize a general dependency refresh.

## Execute

1. Inspect the effective dependency/build path and why the existing mechanism is insufficient. Keep the change scoped to the accepted need and preserve unrelated lockfile entries.
2. Use the repository's package manager and reproducible command/environment; reconcile the manifest and lock using that mechanism rather than hand-writing guessed resolved versions.
3. Inspect relevant transitive/runtime consequences, generated resources and conditional build steps. Follow [SDK transport](../rules/sdk-transport.md) if an SDK transport dependency is replaced/excluded.
4. Produce the affected artifact, then inspect its actual contents and intended entrypoint. Missing assets or dynamically loaded dependencies can be invisible to a source-only test.
5. Verify the relevant consumer/runtime path and existing native command gates. A failed apply/build step must not be hidden by checking an older artifact; no build result authorizes deployment.

## Verify and deliver

Check the changed graph and final artifact at the claimed runtime boundary, alongside the required project checks. Distinguish installation, compilation, packaging, startup and real integration. A configuration-only claim may need a focused parser/contract check rather than a full application launch.

Record manager/tool/runtime identity, changed dependency/artifact scope, commands and limits through the [delivery record](../delivery.md). Keep actual release/existing-consumer validation within its applicable stage-05 policy.

## Project bindings

Bind lockfile/upgrade policy, allowed dependencies, build commands, artifact/resource inventory and runtime compatibility. No toolchain, package or version is a new global default.
