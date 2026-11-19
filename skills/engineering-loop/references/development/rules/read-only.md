# R3 Read-only promises and delegated effects

**ID:** `dev.risk.read-only` · **Status:** available existing boundary guidance.

**Trigger:** The accepted flow promises inspection/read-only behavior and delegates queries, refreshes or resource resolution. Trace the calls that establish the promise rather than selecting by method name alone.

When the accepted flow is read-only, trace the delegated calls rather than relying on query names: inspection may reconcile status, and resource resolution may register data. Reuse the existing fact projection through a narrow read boundary and leave a check that detects those writes. Preserve refresh and registration in flows that require them; do not impose a universal ban on mutating queries.

**Nearby exception:** A deliberately mutating flow keeps its authorized refresh, registration and other required effects. Do not turn a local read-only repair into a project-wide prohibition.

**Verification:** Use [verification.md](../../verification.md) to match the check to the promise, including actual delegated effects and a legitimate mutating control where relevant. If the investigation reveals a disputed behavior contract, resolve that bounded decision through [requirements.md](../../requirements.md).
