# Diagnose operation failures without blind repair loops

**Challenge focus:** What observed impact and tested hypothesis justify the next action, and which evidence will establish recovery rather than merely a restarted process?

Identify observed symptom, time window, affected users/jobs, environment, and current version. Preserve the distinction between a user's report and what the available evidence shows. Correlate relevant logs, queue states, traces, and recent code/configuration changes without exposing sensitive payloads.

Form a hypothesis and collect the least invasive discriminating evidence. Check service identity, business prerequisites, and dependencies before changing code. An unavailable price/configuration, an authentication mismatch, and a transport timeout are different failures even if the UI labels them alike.

For an API failure, record the actual HTTP status and any application response code separately from the same request. A response-body code resembling 404 does not prove that the HTTP route or resource is missing. Check a successful request to the same resource and route/method evidence where available before classifying the failure. Inspect protected runtime configuration only through an authorized read path; lack of access under an ordinary user account does not establish that configuration is absent. Keep the cause unconfirmed until discriminating evidence is available.

Run only authorized operational actions. Bound retries and their side effects; a timeout may mean an unknown result, not a safe-to-repeat failure. On repeated failure without new information, change the hypothesis or present a concrete blocker and options.

When an authorized repair changes externally managed configuration, inventory the current bindings and reusable artifacts first. Use the service's conditional update token when available so a concurrent admin change is not overwritten. For uploaded configuration artifacts, establish the selected file's content identity and check the stored version or digest after upload where the service exposes it; after an ambiguous write result, read current state before repeating the write. Keep credentials in the approved restricted channel or local secret store, outside project artifacts and reports. Confirm the effective configuration, then exercise the affected path with the intended non-admin role; an admin save or connection test alone does not prove recovery. A read-only audit does not authorize activation.

Verify both service recovery and the affected behavior. Record the triggering condition, cause where established, fix/recovery, evidence, and remaining uncertainty. Feed a demonstrated recurring error into an appropriate regression, check, runbook correction, or scoped lesson. Do not create recurring monitoring or external notifications unless requested.

## Prepare to operate a service when its risk warrants it

For a service entering real use, identify the critical business path and the existing evidence that operators can observe it: successful outcomes, completion latency, failed work or backlog age where relevant. Derive thresholds and observation windows from accepted service expectations or measured baseline; unknown targets remain gaps, not invented service guarantees. A responding HTTP endpoint or accepted job does not prove downstream work progresses. Reuse the project's telemetry and runbooks; a local script or an intentionally manual test worker does not need a monitoring platform or automatic processing merely to satisfy this guide.

Identify who responds to a meaningful signal, where they find the relevant version/configuration and correlated evidence, and which authorized recovery action the runbook permits. Where a controlled rehearsal is justified, establish a working baseline, introduce a bounded fault in an isolated environment, and verify both detection and recovery of the original business work. Check retained data, duplicate effects, new work and persistence after restart as applicable; a green health check alone is insufficient. Keep deliberately manual or degraded modes when their accepted purpose requires them. Define the stopping condition before disruptive actions; preparing a runbook does not authorize deployment, fault injection in a shared service, or new external alerts.

For state whose loss would matter, establish the required recovery point, tolerable outage, usable backup and restore prerequisites with the responsible owner. A backup file's existence is not proof of recoverability: when risk warrants it, restore representative data into an isolated destination and exercise the affected read/write path. Separate that evidence from a restart that reuses intact storage, and record untested restore or dependency boundaries explicitly. Use [release.md](release.md) for cutover, migrations and release-specific recovery; this readiness check does not impose a deployment system or claim production acceptance.

## Bound a production action and close on user-facing evidence

These are conditions on an authorized action, not a grant of authority.

Before an action that changes a running service (restart, configuration change, rollback, restore, data repair), write in the operations record: the target; the largest set of users, jobs or data it can affect; the observation that counts as success; the observation that aborts or reverses it; and who may stop it. Start with the smallest reversible scope and widen only after the success observation.

Each production change needs approval that names that action and scope, from a person with authority over the service. A request to diagnose, the existence of a runbook, or approval of a different action is not that approval. Approval already given for this action and scope, or standing authority that project policy grants for it, is not asked again.

Judge recovery where users meet the service: the affected path, correctness of the affected records, and backlog drained, over a stated window. A cleared alert is evidence, not the verdict. When that evidence is missing, report the state as mitigated, name the unverified boundary, and do not report it resolved.

For an incident record:

- Never supply a time, figure, name or cause that no source shows. An unknown becomes an open question with the evidence that would settle it.
- Give each timeline entry its source. Mark an interval without evidence as a gap; do not bridge it.
- Report time to detect (start to first detection) apart from time to mitigate (detection to mitigation). Slow detection is its own finding.
- Before following one causal chain, list candidates across change, infrastructure, configuration and data, detection, process and dependencies, each marked confirmed, suspected or ruled out. Trace only confirmed ones, and keep the trigger apart from the underlying cause.
- Keep observed facts, causal hypotheses and unresolved uncertainty in separate entries.
