# R5 Mutable preconditions and stale or concurrent edits

**ID:** `dev.risk.concurrent-edits` · **Status:** available existing boundary guidance.

**Trigger:** A mutable fact checked before a write can change, or another client/session can make the saved editing base stale. Establish the actual ordering; sequential old-page saves and overlapping database transactions are different failure cases.

When mutable facts are checked before a transaction, validate them again at the final state change and coordinate writers that can invalidate them; locking only the finalizer does not close the race.

When clients can edit the same persisted resource, check whether a later save from an older page can replace a newer one. Carry the revision observed when editing began into the update boundary (for example, an existing ETag or version field), atomically reject a stale update, and leave the user's unsaved input available to reconcile. Database optimistic locking between concurrent transactions alone does not detect this sequential stale-page save. Do not add a second version protocol to an already protected update or require one for append-only operations.

**Nearby exception:** Reuse an equivalent existing protection; append-only operations do not automatically need an edit-base protocol. Preserve the ordinary successful update.

**Verification:** Use the affected-ordering checks in [verification.md](../../verification.md), including an independently expected stale/invalid rejection and a valid unchanged-base control. Check both sides of the changed contract where needed, without automatically loading every frontend/backend scene.
