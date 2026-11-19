# I6 Verify an actual file and storage chain

**ID:** `dev.integration.storage` · **Status:** available execution baseline; storage/session contracts remain pending.

Use for delegated upload, signed access, resumability, ownership or actual storage quota. A local preview with unchanged storage/access does not require replacing the upload protocol. Apply the matching parts of [R7](../rules/uploads.md).

## Inputs

Identify the actual content/file identity, actor/resource ownership, producer/client/storage adapter versions and target configuration. Locate the maintained upload/session, signed-access, storage-retention and quota contracts; keep signing material and credentials outside artifacts and logs.

## Execute

1. Trace content selection, access issuance, transfer, storage acceptance and final resource registration/read-back. Distinguish preview, declared metadata, accepted bytes and a completed stored artifact.
2. Before session reuse, establish original content identity under R7; matching filename, size and timestamp are insufficient. Use a new session when accepted identity cannot be established.
3. Follow the actual actor/resource path through direct storage and signed access under [R2](../rules/access.md). A returned URL or upstream permission check does not by itself prove the intended consumer can access the file.
4. For quota claims, check bytes accepted and retained by storage, including relevant unfinished objects; a proxy/request-size limit alone does not establish that bound.
5. Reconcile unknown transfers or registration results under [R4](../rules/async-idempotency.md) where applicable. Apply only the existing authorized cleanup/retention policy; do not delete unrelated objects to make a check pass.

## Verify

- Verify the accepted file's identity and the affected upload/read/download outcome on the actual storage path, with a valid unchanged-file control for resumability.
- Include relevant unauthorized access, changed-file or unfinished-upload/quota cases. Exercise signed-link expiry only against the accepted access contract, without inventing a duration.
- Separate local preview, mocked storage, real retained bytes and generated-artifact validity; use [output-property checks](../../verification-boundaries.md#generated-media-and-document-properties) only when that claim applies.

## Deliver

Record safe resource/content references, tested actors, adapter/artifact/target identity, retained-state observations and untested boundaries through the existing [delivery record](../delivery.md). Do not copy credentials or signed access values into the task.

## Team bindings — pending

Bind actual adapters, session identity, signed-access, download, quota and cleanup contracts. No universal storage layout, retention period or uploader component is supplied.
