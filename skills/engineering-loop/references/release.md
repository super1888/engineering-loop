# Prepare an identifiable, recoverable release

**Challenge focus:** Which artifact will reach which consumers, and are migration, recovery, acceptance evidence and execution authority sufficient?

First determine whether the request authorizes preparation, staging, or actual publication. Preserve existing authorization; ask only for a missing material choice or an action outside scope. Prepare a concrete reviewable artifact before requesting any required final approval.

Follow the project's release process. Tie the build artifact to the verified source and configuration, including uncommitted-state evidence when relevant. Coordinate edits/builds so the artifact under test is not silently replaced; avoid repackaging a file an active process is still using.

Before adding a release preflight to CI, run it against the existing isolated CI fixtures as well as the intended release artifact. For byte or permission checks, identify what the target actually uses: Git object contents can differ from a Windows checkout or archive after line-ending conversion, and Windows Git Bash does not establish Unix file-mode behavior. Compare checksums on the relevant bytes and use a Linux fixture or CI run for Unix permissions; preserve a valid failing gate until its cause is known.

For a branch-driven deployment, inspect the workflow on the target ref, not just the current checkout. Confirm what update actually triggers publication, which environment it reaches, and the effects of its smoke checks. Apply each repository's rules to its own work; an authorized deployment-triggering push in one repository is not barred or permitted by another repository's local push policy.

For schema changes, use the project's baseline/upgrade policy and cover the applicable empty, existing-data, interrupted, and rerun paths. Separate code rollback, data restoration, and forward repair. Reverting code cannot recover deleted data. Verify recovery prerequisites appropriate to the impact.

When a production migration requires off-host recovery, verify before migration that its recoverable point covers the agreed cutover state. A fresh backup left on the migrating host does not make an older off-host copy current.

When a release pauses writes or drains expiring write credentials, budget that window together with backup, migration and health checks against the actual job timeout. Arrange recovery outside the job for abrupt runner loss; a shell exit trap cannot cover every termination. Check every rollback entrypoint against the resulting schema, not only the automatic failure path.

If the old version issued write-capable links or leases, check whether they remain effective after switching versions. Stop new issuance and let existing rights expire or revoke them before publishing data under keys they can still change; verify how unfinished work resumes.

When replacing a feature or removing its routes, inventory existing user artifacts and their access paths even if the database schema is retained. Verify migration, read-only access, or export against representative existing data before calling the replacement ready.

Prepare the release scope, required configuration, migration order, artifact identity, smoke checks, and recovery decision. Reuse existing runbooks. Execute authorized steps and then verify the deployed version, essential user path, and relevant error signals. A successful upload or health endpoint alone is not a full release acceptance.

Hiding a feature in the UI or build does not disable its server endpoints. For a deferred feature, inspect the target environment's effective ingress and test anonymous access to relevant state-changing or streaming routes while preserving intentionally public paths. A 200 behind a single-page app fallback can be the app's index rather than the intended service; check an endpoint-specific response shape or marker before claiming that an upstream route is reachable or exposed.

For commands operators must run during a maintenance window, check that copying them from the saved runbook into the intended shell preserves their syntax. Markdown indentation can break here-doc or here-string delimiters even when a rendered code block looks correct.

When a release relies on a limit enforced by an external ingress or proxy, verify its effective configuration and a bounded over-limit probe in the target environment; changing a template does not activate the limit.

If a new frontend build replaces versioned assets, check whether already-open pages can still fetch the files they reference, especially lazy-loaded code. Preserve those files or verify a recovery path appropriate to the project's state; a fresh-page smoke check does not cover existing sessions.

Record actual outcome and untested boundaries. Never convert a skipped external check into a success claim.

## Choose the undo path before the rollout

These are conditions on an already authorized release; naming an undo path does not authorize running it.

Promote the artifact that passed its checks. Rebuilding per environment produces a different artifact that the earlier evidence does not cover; where the build forces it, record that and rerun the affected checks on the rebuilt artifact. Where the project can separate installing a version from exposing it to users, record which step the authorization covers and which one each check observed.

Before the rollout, name the undo path for each changed layer and confirm its prerequisite:

| Undo path | Holds only when |
|---|---|
| Switch the behavior off | The change sits behind a runtime switch whose off position was exercised on the new version |
| Redeploy the previous artifact | That exact artifact is retained and still runs against the resulting schema, data and configuration |
| Roll forward with a fix | The fix is small enough to pass the same gates in the time the impact allows |
| Restore data | See [migration-safety.md](migration-safety.md) |

A version-control revert is not a rollback. It builds an artifact that has never run in the target and leaves schema, data, configuration and switch state as they are; treat it as a roll-forward that needs the full gates.

Gate the rollout on error and latency signals split by version and compared with the previous version over the same window, not on an aggregate before and after. Before undoing, confirm the suspected version is the one producing the errors. Where signals cannot be split by version, record the attribution as unverified.

Completion, recorded in the release record's recovery, stop-point and verification fields:

- Preparation: artifact identity, target, the undo path and prerequisite evidence per layer, the indicators and thresholds that stop or reverse the rollout, and who may call it.
- Executed release: the deployed version, user path and those indicators observed over the agreed window.
- Executed undo: the same indicators back at baseline, not the redeploy command exiting.
