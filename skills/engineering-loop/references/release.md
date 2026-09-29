# Prepare an identifiable, recoverable release

First determine whether the request authorizes preparation, staging, or actual publication. Preserve existing authorization; ask only for a missing material choice or an action outside scope. Prepare a concrete reviewable artifact before requesting any required final approval.

Follow the project's release process. Tie the build artifact to the verified source and configuration, including uncommitted-state evidence when relevant. Coordinate edits/builds so the artifact under test is not silently replaced; avoid repackaging a file an active process is still using.

For a branch-driven deployment, inspect the workflow on the target ref, not just the current checkout. Confirm what update actually triggers publication, which environment it reaches, and the effects of its smoke checks. Apply each repository's rules to its own work; an authorized deployment-triggering push in one repository is not barred or permitted by another repository's local push policy.

For schema changes, use the project's baseline/upgrade policy and cover the applicable empty, existing-data, interrupted, and rerun paths. Separate code rollback, data restoration, and forward repair. Reverting code cannot recover deleted data. Verify recovery prerequisites appropriate to the impact.

When a release pauses writes or drains expiring write credentials, budget that window together with backup, migration and health checks against the actual job timeout. Arrange recovery outside the job for abrupt runner loss; a shell exit trap cannot cover every termination. Check every rollback entrypoint against the resulting schema, not only the automatic failure path.

If the old version issued write-capable links or leases, check whether they remain effective after switching versions. Stop new issuance and let existing rights expire or revoke them before publishing data under keys they can still change; verify how unfinished work resumes.

When replacing a feature or removing its routes, inventory existing user artifacts and their access paths even if the database schema is retained. Verify migration, read-only access, or export against representative existing data before calling the replacement ready.

Prepare the release scope, required configuration, migration order, artifact identity, smoke checks, and recovery decision. Reuse existing runbooks. Execute authorized steps and then verify the deployed version, essential user path, and relevant error signals. A successful upload or health endpoint alone is not a full release acceptance.

When a release relies on a limit enforced by an external ingress or proxy, verify its effective configuration and a bounded over-limit probe in the target environment; changing a template does not activate the limit.

If a new frontend build replaces versioned assets, check whether already-open pages can still fetch the files they reference, especially lazy-loaded code. Preserve those files or verify a recovery path appropriate to the project's state; a fresh-page smoke check does not cover existing sessions.

Record actual outcome and untested boundaries. Never convert a skipped external check into a success claim.
