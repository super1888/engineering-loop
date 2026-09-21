# Diagnose operation failures without blind repair loops

Identify observed symptom, time window, affected users/jobs, environment, and current version. Preserve the distinction between a user's report and what the available evidence shows. Correlate relevant logs, queue states, traces, and recent code/configuration changes without exposing sensitive payloads.

Form a hypothesis and collect the least invasive discriminating evidence. Check service identity, business prerequisites, and dependencies before changing code. An unavailable price/configuration, an authentication mismatch, and a transport timeout are different failures even if the UI labels them alike.

Run only authorized operational actions. Bound retries and their side effects; a timeout may mean an unknown result, not a safe-to-repeat failure. On repeated failure without new information, change the hypothesis or present a concrete blocker and options.

Verify both service recovery and the affected behavior. Record the triggering condition, cause where established, fix/recovery, evidence, and remaining uncertainty. Feed a demonstrated recurring error into an appropriate regression, check, runbook correction, or scoped lesson. Do not create recurring monitoring or external notifications unless requested.
