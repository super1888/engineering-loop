# F8 Frontend engineering

**ID:** `dev.frontend.engineering` · **Status:** available execution baseline; toolchain standards remain pending.

## Scope and inputs

Use for an affected frontend build, asset path, dependency, runtime compatibility or performance defect. Identify the actual module, build configuration/lockfile, relevant entrypoint, accepted runtime target and representative reproduction. Deployment execution follows stage 05 authority, not this implementation branch.

## Execute

1. Reproduce the affected build/runtime condition using the repository's maintained commands and environment. Establish which stage fails before changing bundler, dependency or code; a source compilation success is not a runtime conclusion.
2. Locate the current ownership of configuration, assets and dependency versions. Reuse it rather than introducing a second toolchain or automatically upgrading packages; a necessary new dependency needs its current reason and maintenance impact established.
3. For asset/public-path changes, trace the requested resource from the actual built entrypoint through its resolved URL/module path. Check the affected loading mode instead of treating a source import or development server as production-artifact proof.
4. For a dependency or shared-build boundary, use the relevant [engineering catalog](../scenarios/engineering.md); apply [R8](../rules/sdk-transport.md) only when an actual SDK transport path is affected. Release compatibility claims belong with their applicable stage-05 evidence.
5. For performance work, compare the same representative interaction/artifact and environment before/after where feasible. Isolate the measured cause and preserve the accepted behavior; do not invent a budget or hide a defect by reducing the requested workload.

## Verify

- Run the owning project checks and the actual affected runtime/resource path; distinguish development preview, built artifact and deployed environment.
- For visible behavior/performance conclusions, use [R9](../rules/rendered-ui.md) and record the relevant state/measurement. Package metadata or a smaller bundle alone does not prove the user task improved.
- Retain unrelated working paths and project-required checks; a repaired local build does not authorize or establish deployment.

## Deliver

Record the configuration/dependency/artifact change, reproduced condition, owning commands and observed runtime or measurement limits through [delivery records](../delivery.md). Link maintained version/configuration rather than duplicating it in a parallel standard.

## Team binding — pending

Bundler/package manager, asset conventions, browser policy and performance budgets remain actual project choices. No framework migration, dependency approval policy or universal limit is supplied here.
