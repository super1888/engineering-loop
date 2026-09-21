# Accepted receipt behavior

The exercise owner has approved these rules. No additional business decision is needed for this change.

`Inventory(path)` opens an SQLite database. `create_order(order_id, ordered)` creates an order; `received(order_id)` reports its received quantity; `close()` closes the connection. Preserve these APIs and existing data.

`receive(order_id, quantity, request_id)` records a receipt and returns the cumulative received quantity **at that receipt's original acceptance**.

- Quantities in this exercise are positive integers; invalid quantities are rejected with `ValueError` and no writes. Unknown orders raise `KeyError`.
- Each request ID identifies one immutable receipt across all orders. The same ID/order/quantity returns its original result without another write, including after reopening the database and after later receipts.
- Reusing a request ID with a different order or quantity raises `ValueError` without changing any data.
- Received quantity cannot exceed ordered quantity. Reject an excessive receipt with `ValueError`, leaving both order and receipt records unchanged. A rejected request ID is not consumed.
- Competing database connections must preserve these rules. Duplicate requests may both succeed with the same result, but only one receipt is recorded. Distinct receipts that jointly exceed the remaining quantity cannot both succeed.
- A receipt's identity, original result and inventory update must persist atomically. Use the existing `receipts` table for accepted receipts.

Accepted examples:

| Starting state | Actions | Outcome |
|---|---|---|
| Order A: 100 ordered, 0 received | Receive 60 using R1; retry R1 | Both return 60; received remains 60 |
| Order A: received 60 from R1 | Receive 20 using R2; retry R1 | R2 returns 80; R1 returns 60; received remains 80 |
| R1 belongs to A, quantity 60 | R1 with quantity 50 or order B | Reject; no changes |
| Order A: 100 ordered, 60 received | Receive 50 using R3 | Reject; received remains 60; R3 is unused |

Out of scope: HTTP/UI, authentication, units of measure, partial acceptance, returns, accounting, external services, deployment and production migrations.
