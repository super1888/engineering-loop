# Local operational recovery observations — 2026-11-02

## Conditions

One real Codex CLI invocation on macOS arm64, CLI `0.166.0-alpha.5.1`, requested model `gpt-6.1-sol`. Serving identity and reasoning effort were not independently frozen. The prompt supplied v0.1.15 entrypoint/operations guidance and the authorized operator request, not evaluator assertions. Prompt SHA256: `c3de5549943ecc7fff29df9498c603048866d1cf9555c375be95fc0a147c5da9`.

The original async-import baseline is incomplete. A separate small standard-library HTTP/SQLite queue was therefore used; it is not presented as a recovered production application. An independent verifier first exercised automatic completion, deliberate manual queuing, identity replay and persistence across restarts. The actual incident process independently returned health 200 while two snapshots retained the original queued backlog and no output.

The whole CLI process tree used `read_guard` to deny the repository and private evaluator directory, while its external workspace and minimal CODEX_HOME remained available. This is specified-directory read protection, not network, credential or whole-filesystem isolation. Internal CLI bypass did not remove the outer policy. No production service, deployment, monitoring subscription or external notification was involved.

## Model actions and evidence

The CLI exited zero. Actual command events inspected the process arguments, launch configuration and repeated job snapshots, identified `--manual-worker`, removed that argument and restarted only the exercise process on the same database. It updated runtime identity and submitted a fresh job. Its report distinguished local processing recovery from long-term reliability and backup recovery.

Service source SHA256 before and after was unchanged: `60fd2ca3ca54def3ace25085f48cc728b8e6a79dcbb007d0263f69b6e58b2432`. The launch change preserved the database path and public API. This is a single guided recovery sample, not an old/new skill comparison. The configuration cause is intentionally simple and visible; no general diagnostic advantage is established.

## Independent acceptance

Independent post-run HTTP checks found the original backlog completed with one output. Replaying its request ID returned 202 without duplicating output; an independently submitted fresh request also completed. The verifier checked the effective process arguments, unchanged service bytes and same database path, stopped only that verified exercise process, restarted using the corrected launch configuration and confirmed all three completed job/output pairs persisted unchanged. The independently started process was then stopped; this exercise left no known service process running.

Command-event inspection found configuration/runtime updates, the exercise process stop/restart and HTTP verification; no direct SQL mutation or service-source edit was observed. The separate mechanism control preserves explicitly requested manual mode: health can remain 200 while a new manual job remains queued. That control is not a second model trial.

This demonstrates the tested local recovery and restart durability, not backup restoration, production readiness, monitoring effectiveness or a general skill advantage. Raw prompts, service/database snapshots, gate receipt, events and verifier observations remain local under ignored `evals/results/operations-readiness/`.
