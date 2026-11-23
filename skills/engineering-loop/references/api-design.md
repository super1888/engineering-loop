# API contract and idempotency design

Use from [stage 02](stages/02-design.md) when a design adds or changes an interface that another module, team, client or external system consumes: an HTTP or RPC operation, an event, a webhook or a shared schema. Write the result in the project's existing API document or the plan's API field. It adds no document format, framework or dependency.

## Start from consumers and authority

- List each consumer and the job it needs done before listing routes or fields. An operation or field that no consumer job needs stays out.
- Name the authoritative owner of each exposed entity's data and schema. A mapping or aggregation layer does not become the authority by returning the data.
- For each operation, state who may act on which object, checked on the server per object and tenant. Being signed in is not authorization; name the test that proves the check runs.
- Record unanswered policy as an open decision with its owner under the [common challenge](grill.md). Do not settle it inside the contract.

## Make the representation explicit

Decide and write down where each applies:

- **Absent and null:** whether an absent field means unknown, not applicable, withheld or default, and whether null differs from absent. In a partial update, say which one leaves a value alone and which clears it.
- **Defaults:** who applies them (server, client or generated code) and whether changing one later alters behavior for existing callers.
- **Enums:** open or closed, and what a consumer must do with a value it does not know.
- **Quantities and time:** unit, precision, rounding, currency and time zone for every number and timestamp.
- **Ordering:** the default sort and the tie-break that makes it deterministic.
- **Pagination:** the model and page limits, token expiry, and what a consumer sees when records change between pages (repeats, gaps or a stable snapshot).
- **Errors:** one shape across operations, a stable machine-readable code and whether a retry is safe.
- **Accepted and completed:** for asynchronous work, what the first response promises and how the consumer learns the final result.

## Design retries for every state-changing operation

State whether repeating the call is safe. When it is not and any client, queue or person can retry it, design the key before implementation:

- Derive the key from the intent (the client's request identifier or an immutable business identifier), never from the attempt. A value the retrying layer generates makes every retry a new request; a key built only from user and amount merges two legitimate requests.
- Claim the key in one atomic write under a unique constraint, then act. A read followed by a write lets two concurrent retries both proceed.
- Store a fingerprint of the request with the key. Reject the same key with a different body; do not replay the first response.
- Choose what a duplicate receives while the first attempt is still running: a conflict, a bounded wait or a pending status. Never let it through because the first looks stuck.
- Treat a timeout as an unknown outcome, not a failure. Record the intent before calling out, and state how an unknown result is resolved: a status query or a reconciliation.
- Keep keys longer than the longest path that can deliver the same intent again, including queue replays and manual resends.
- A key does not settle competing different updates. Use a version check or state that the last write wins and what is lost.

## Assess a change per consumer

- An added field, enum value or changed default is not automatically safe. Strict decoders, generated clients, exhaustive switches, caches and signature checks can break on it. Check each known consumer or mark it unverified.
- For a removal or a change of meaning, name the successor, the migration path and the evidence that consumers have moved; a date alone is not evidence. Sequence it with the expand, migrate, contract steps in [delivery-planning.md](delivery-planning.md).
