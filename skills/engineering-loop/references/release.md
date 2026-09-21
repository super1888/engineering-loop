# Prepare an identifiable, recoverable release

First determine whether the request authorizes preparation, staging, or actual publication. Preserve existing authorization; ask only for a missing material choice or an action outside scope. Prepare a concrete reviewable artifact before requesting any required final approval.

Follow the project's release process. Tie the build artifact to the verified source and configuration, including uncommitted-state evidence when relevant. Coordinate edits/builds so the artifact under test is not silently replaced; avoid repackaging a file an active process is still using.

For schema changes, use the project's baseline/upgrade policy and cover the applicable empty, existing-data, interrupted, and rerun paths. Separate code rollback, data restoration, and forward repair. Reverting code cannot recover deleted data. Verify recovery prerequisites appropriate to the impact.

Prepare the release scope, required configuration, migration order, artifact identity, smoke checks, and recovery decision. Reuse existing runbooks. Execute authorized steps and then verify the deployed version, essential user path, and relevant error signals. A successful upload or health endpoint alone is not a full release acceptance.

Record actual outcome and untested boundaries. Never convert a skipped external check into a success claim.
