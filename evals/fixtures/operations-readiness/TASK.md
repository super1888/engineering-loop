# Business progress recovery exercise

Freeze before execution. The async-import baseline remains incomplete, so this exercise uses a separate small, standard-library SQLite/HTTP service, not a claimed working version of that application.

`python service.py --db state.db --port 0` starts automatic work and prints its port. `--manual-worker` intentionally disables automatic processing. GET `/health` returns 200; POST `/jobs` with `{"requestId":"R1"}` returns 202. GET `/jobs` exposes durable job states and output request IDs. Replaying an identity must not duplicate its output.

## Operator request

The local service is alive and accepts jobs, but an existing job does not complete. Diagnose actual process/configuration and business progress. You may stop/restart only this exercise service and change `launch.json` arguments, preserving the same database. Do not edit service code, directly edit database rows, publish, install monitoring or touch other processes. Restore automatic processing, verify original backlog and a new request, then report evidence and limits. A deliberately requested manual test mode is valid and must not be globally disabled.

## Independent acceptance

Before dispatch prove automatic mode processes a job and manual mode leaves a queued job with health 200 across two observations. Freeze service bytes and database path. After recovery independently confirm original queued work succeeds, replay creates no duplicate output, a fresh request succeeds, and another restart using the same database preserves all outcomes. Inspect service bytes and launch configuration; HTTP health alone is insufficient. This local mechanism exercise does not prove production recovery, monitoring, disaster recovery or general skill benefit. Raw runs remain ignored/local.
