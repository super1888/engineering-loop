# R8 SDK dependency and transport changes

**ID:** `dev.risk.sdk-transport` · **Status:** available verification pointer.

**Trigger:** A change excludes or replaces an SDK's transitive dependency and may affect the real request path. Identify the consuming module, resulting dependency set and actual adapter rather than selecting a rule from an SDK name alone.

Read and apply [SDK transport after dependency changes](../../verification-boundaries.md#sdk-transport-after-dependency-changes). That section owns the real-transport evidence requirement, local-probe option, security boundary and distinction from provider acceptance.

**Nearby exception:** An unaffected pure serialization change does not require an unrelated transport probe or a paid provider call.

**Verification:** Record the affected SDK path and actual runtime/dependency identity with the applicable result. Provider-specific adapters, dependency versions and package constraints remain with the project's maintained conventions; none is installed or approved merely by this route.
