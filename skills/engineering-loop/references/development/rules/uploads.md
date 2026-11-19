# R7 Upload identity, recovery and storage

**ID:** `dev.risk.uploads` · **Status:** available existing identity guidance and verification pointers.

**Trigger:** The change affects resumable-file identity, delegated/direct upload, storage quotas or an upload's actor/resource access. Select the applicable sub-boundary; a preview component alone does not imply every storage concern changed.

Before reusing a resumable upload session, establish that the selected file has the original content; matching name, size and modification time is insufficient. Start a new session when content identity cannot be established.

For direct-storage quota claims, read [Direct-upload storage quotas](../../verification-boundaries.md#direct-upload-storage-quotas). When shared actors/resources are affected, also apply [Cross-user and role access](../../verification-boundaries.md#cross-user-and-role-access). Those maintained sections own their detailed checks; a new uploader does not create a new permission policy.

**Nearby exception:** An unchanged metadata display does not require replacing the existing upload protocol or adding resumability. Keep required checks for any actually changed access or rendering boundary.

**Verification:** Verify content identity and valid unchanged-file recovery on the actual affected path, plus only the triggered storage/access checks. Concrete uploader, storage SDK and component conventions remain pending project/team detail.
