# Independent-destination restore observations — 2026-11-02

## Preparation and conditions

This reuses the small standard-library queue service, not a production application. The owner first completed `before-backup`, created a separate SQLite backup through the backup API, then completed `after-backup` in the original database. The original service was stopped and its database moved into a private read-denied directory. Independent preflight inspected both databases: the backup contains only `before-backup`, while the original also contains `after-backup`; the restore destination did not exist.

One real Codex CLI invocation ran on macOS arm64, CLI `0.166.0-alpha.5.1`, requesting `gpt-6.1-sol`. Serving identity and reasoning effort were not independently frozen. The supplied reference package was the v0.1.15 entrypoint and operations guide, plus the operator request and an explicit backup-cutoff note. This is a guided single-version sample, not a no-skill comparison. Prompt SHA256: `f33756c548326f8b18cea29192c03ec2c1f73213ecbefb987ce7bec26aff2f86`.

The entire CLI process tree ran under `read_guard`, denying the project repository and private original/evaluator directory; the external workspace and minimal CODEX_HOME remained available. This protects specified local directories, not the whole filesystem, network or credentials. Internal CLI bypass did not remove the inherited outer policy. Raw configuration and credentials are not included in these artifacts. A transient network reconnect appeared in the event stream, followed by a completed turn and CLI exit 0; no timing benefit is inferred.

## Operator actions

The model restored into `restore/restored.db`, started the unchanged service against that destination, inspected the recovery point, replayed the retained request, submitted a new request and restarted the restored service. It reported `before-backup` present and `after-backup` absent, without representing the missing post-backup work as recovered. Its runtime receipt identifies the PID, port, database path and file identity. Its attempt to inspect process arguments with `ps` was denied in its environment; process identity therefore required separate outside verification rather than relying on that self-report.

Frozen backup SHA256: `f9152ae4b80f289cd8e0c28802e67b61be66dc7d3a960b476410bf4acb550f8e`.
Service source SHA256: `60fd2ca3ca54def3ace25085f48cc728b8e6a79dcbb007d0263f69b6e58b2432`.

Original database rows were independently observed before dispatch, but its byte hash was first recorded during the model run. That hash can establish preservation after its observation, not retroactive pre-dispatch byte identity.

## Independent acceptance

The independent verifier checked the actual process arguments and database identity outside the guard, confirming a distinct restored file rather than reuse of the original or backup. The restored service retained `before-backup` exactly once and had no `after-backup` row or output. HTTP replay did not duplicate the retained output; an independently submitted new request completed. Another service restart against the restored database preserved all three retained/new job-output pairs unchanged.

Backup and service hashes remained equal to their frozen values. The original still contained `after-backup` and its bytes matched the during-run sample; this does not establish an unrecorded pre-dispatch byte hash. Event inspection observed file copying from the independent backup, followed by service-driven checks, not manual reconstruction of historical rows. Both the model's final service and the independently restarted service were stopped after verification.

This demonstrates local recovery into a separate destination at the observed backup cutoff, including subsequent writes and restart persistence. It does not demonstrate recovery of post-backup work, off-host disaster recovery, encrypted-backup access, production RPO/RTO or a causal skill benefit. The missing `after-backup` item is an explicit data-loss boundary, not a restored success. Raw database copies, process records, prompts, commands, gate receipt and verifier observations remain local under ignored `evals/results/backup-restore/`.
