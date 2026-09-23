# Online Ordering Requirements

## Scope

This document defines the current online ordering slice for the bar's existing menu of drinks and packaged snacks.

The slice covers whether a requested item can be ordered, stock reservation, and order acceptance. It does not add or identify new menu items, change the menu, collect payment, or define handling for a shortage discovered after an order has been accepted.

## Requirements

### R1. Only listed menu items may be ordered

- An online order may contain only items that are identifiable as specific items on the current online menu.
- A request that is not identifiable as a specific listed menu item must not be accepted as an order item.
- A known off-menu item must not be accepted as an order item.
- Off-menu requests must not be routed to staff or a manager for an exception. The bar does not accept off-menu orders through either the online channel or staff, and there is no manager-exception path.

### R2. Stock must be reserved before acceptance

- For each requested listed item, the flow must reserve the requested stock before accepting the order.
- If the requested stock cannot be reserved, the order must not be accepted.
- A listed item with zero available stock must not be accepted in an order.

### R3. Acceptance occurs after stock reservation

- An order is accepted only after its stock has been reserved successfully.
- When an order is accepted, the flow must return an order number.
- Acceptance and the returned order number do not mean that payment has occurred. Payment happens later and is outside this slice.

### R4. A later inventory shortage is unresolved

- Inventory synchronization may reveal a shortage after an order has been accepted.
- No cancellation, substitution, or refund behavior is specified for that situation yet.
- The operations manager owns the decision about that policy. Until the decision is made, this document must not imply that any of those outcomes is automatic or available.

## Acceptance Examples

| Request | Relevant state | Required outcome |
|---|---|---|
| “星云特调” | The name is not identifiable as a specific current menu item. | Do not accept it as an order item and do not offer staff or manager escalation. |
| “蛋炒饭” | It is a known off-menu request. | Do not accept it as an order item and do not offer staff or manager escalation. |
| House lager | It is listed but has zero stock. | Stock reservation cannot succeed, so do not accept the order. |
| Sparkling water | It is listed and five units are available. | Accept a requested quantity only if that quantity is successfully reserved, then return an order number. |
| An accepted order later found short by inventory synchronization | The order already has reserved stock and an order number, but a later shortage is reported. | Do not assume cancellation, substitution, or refund behavior; the required resolution remains an open business decision. |

## Verification

The requirements are satisfied when review or testing demonstrates that:

1. Unidentifiable and known off-menu requests are rejected without an exception path.
2. Listed items are accepted only after sufficient stock is reserved.
3. Zero-stock listed items are not accepted.
4. Successful acceptance returns an order number and does not represent payment.
5. The product does not claim a cancellation, substitution, or refund policy for a shortage discovered after acceptance until the operations manager approves one.

## Open Business Decision

The operations manager must decide what happens when inventory synchronization reveals a shortage after acceptance: whether the order is cancelled, an item may be substituted, a refund is issued, or another explicitly approved policy applies. That decision is not part of the currently accepted requirements.
