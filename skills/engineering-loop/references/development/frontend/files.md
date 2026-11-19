# F6 Files and media

**ID:** `dev.frontend.files` · **Status:** available execution baseline; uploader/media conventions remain pending.

## Scope and inputs

Use for affected upload, preview, progress, cancel, resume or download behavior. Identify selected content, accepted file constraints, actual storage/service path, actor/resource ownership and completion result. A preview-only change does not automatically change storage or authorize media processing.

Use the relevant [interactive-slice guidance](../../ui.md#test-the-uncertain-decision-before-replication) for uncertain user interaction, preserving the accepted flow and target.

## Execute

1. Trace selected content through preview, request/session identity and final stored/downloaded resource. Keep original, preview and generated output identities distinct; do not replace an accepted source merely because a display variant exists.
2. Apply the actual contract's size/type/availability constraints. Client metadata or a progress indicator is not proof of accepted/stored bytes; do not introduce a new quota or content limit without a maintained basis.
3. Use [R7](../rules/uploads.md) when resume identity, direct storage or quota changes, and [R2](../rules/access.md) for signed/owned resources. Establish content identity before session reuse; matching name, size and time is insufficient.
4. Preserve input and relevant recovery information on the affected failure path. Distinguish local abort, server cancellation and completed storage according to the existing protocol; a stopped progress indicator alone proves none of them.
5. If the implementation creates temporary preview resources, release its owned resources when no longer used without invalidating a still-visible/downloadable result. Reuse the project's existing lifecycle instead of adding a new storage mechanism.

## Verify

- Check an accepted file and the relevant rejection, interruption or same-file recovery path against the actual resource result.
- Verify only the triggered storage/access boundary; for generated output-property claims use [actual runtime/rendering](../../verification-boundaries.md#generated-media-and-document-properties).
- A working browser preview does not prove durable storage, authorized download, content fidelity or generated-artifact validity. Keep those claims separate.

## Deliver

Record the changed file/session/resource boundary, constraints source, actual success/failure evidence and remaining storage/integration limits through [delivery records](../delivery.md). Do not include credentials, signed URLs or private file contents in reusable examples.

## Team binding — pending

Upload widget, storage adapter, file constraints, media presentation and download policy remain bound to actual project contracts; no resumability or transformation capability is added by this guide.
