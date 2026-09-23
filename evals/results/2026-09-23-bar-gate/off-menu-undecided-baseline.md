# Online Ordering Requirements

## Scope

This document defines the currently agreed requirements for ordering drinks and packaged snacks through the online flow. It records unresolved policies without selecting behavior for them.

## Accepted behavior

1. The online menu presents listed drinks and packaged snacks.
2. A customer can order a listed item only when the item is identifiable and sufficient stock can be reserved.
3. The system accepts an order only after reserving the required stock.
4. When an order is accepted, the system returns an order number.
5. Payment occurs after order acceptance; payment is not a prerequisite for reserving stock or returning the order number in this slice.
6. If sufficient stock cannot be reserved, the order must not be accepted and no order number may be returned for it.

## Acceptance examples

| Request | Known state | Required online outcome |
| --- | --- | --- |
| Sparkling water | Listed; five units available | An order within available quantity may be accepted after its stock is reserved, then an order number is returned. A request exceeding reservable stock is not accepted. |
| House lager | Listed; zero stock | The order is not accepted because stock cannot be reserved. |
| “星云特调” | Not identifiable as a specific menu item | The request is not accepted as a normal menu-item order because the item cannot be identified. This does not decide whether it may later be handled as an off-menu request. |
| “蛋炒饭” | Known off-menu request | Online acceptance or rejection is not specified until the off-menu policy is decided. |

## State boundary

An order number confirms that stock was reserved and the order was accepted. It does not confirm payment or guarantee that later inventory synchronization will not reveal a shortage.

## Open business decisions

### Online off-menu requests

- Decision owner: bar manager.
- Decision required: whether the online system may take off-menu requests after availability and price are confirmed, and what online flow applies if it may.
- Until decided, no requirement authorizes online acceptance of off-menu requests. “蛋炒饭” must remain an unresolved acceptance case, and “星云特调” must not be inferred to be either a listed item or an approved off-menu item.

### Shortage discovered after acceptance

- Decision owner: operations manager.
- Decision required: what happens when inventory synchronization reveals a shortage after an order was accepted, including whether the order is cancelled, substituted, or refunded and what the customer is told.
- Until decided, this document does not prescribe cancellation, substitution, refund, or customer-notification behavior for that condition.

## Non-goals

- Expanding the online menu.
- Defining payment processing beyond its position after order acceptance.
- Defining staff handling of off-menu requests outside the online system.
- Selecting either unresolved business policy above.

## Verification criteria

The requirements are satisfied when evidence shows that:

1. A listed, identifiable item with sufficient stock is accepted only after stock reservation and returns an order number.
2. A listed item with zero stock, represented by House lager, is not accepted.
3. An unidentified request, represented by “星云特调,” is not treated as a normal menu-item order.
4. The online outcome for known off-menu requests, represented by “蛋炒饭,” remains pending the bar manager's decision.
5. No cancellation, substitution, refund, or notification policy is asserted for a post-acceptance shortage before the operations manager decides it.
