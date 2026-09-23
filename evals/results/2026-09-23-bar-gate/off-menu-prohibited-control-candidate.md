# Online ordering requirements

## Outcome and scope

This slice defines how the current online ordering flow handles drinks and packaged snacks that are listed on the online menu. An online order is accepted only after the requested stock has been reserved. On acceptance, the customer receives an order number. Payment occurs later and is not part of order acceptance.

The online flow must not accept requests that cannot be identified as a listed menu item or requests for known off-menu items. Off-menu requests are not fulfilled through staff, and there is no manager-exception path.

Expanding the menu and defining recovery after a post-acceptance inventory shortage are outside the settled scope of this slice.

## Requirements

1. The ordering flow must accept orders only for identifiable items currently listed on the online menu.
2. If a customer request cannot be identified as a specific listed item, the flow must not create or accept an order for that request. It must communicate that the request cannot be identified as a menu item and must not represent it as an off-menu exception awaiting staff or manager approval.
3. If a requested item is known to be off-menu, the flow must reject the request. It must not create an order, reserve stock, initiate payment, forward the request to staff for fulfillment, or offer a manager-exception path.
4. A listed item can be accepted only when the requested quantity can be reserved from available stock.
5. If adequate stock cannot be reserved, the flow must not accept the order or issue an order number. Because payment occurs later, no payment is initiated for this unsuccessful attempt.
6. After successfully reserving the requested stock, the flow must accept the order and return an order number. Acceptance does not mean payment has completed.
7. The flow must keep these outcomes distinct:
   - a request that cannot be mapped to a specific menu item;
   - an identifiable but prohibited off-menu request;
   - a listed item that is temporarily unavailable because stock cannot be reserved; and
   - a listed item whose stock is successfully reserved and whose order is accepted.

## Acceptance examples

| Request and starting condition | Required observable outcome | Commitment at that point |
| --- | --- | --- |
| Customer requests “星云特调”; the name is not yet identifiable as a specific listed menu item. | The request is not accepted, and the customer is told it cannot be identified as a menu item. No staff or manager exception is offered. | No order number, stock reservation, or payment. |
| Customer requests “蛋炒饭”; it is a known off-menu request. | The request is rejected as off-menu. It is not routed to staff or a manager for an exception. | No order number, stock reservation, or payment. |
| Customer requests House lager; it is listed but has zero stock. | Stock cannot be reserved, so the order is not accepted and the item is treated as unavailable rather than off-menu. | No order number or payment. |
| Customer requests one sparkling water; it is listed and five units are available. | One unit is reserved, the order is accepted, and an order number is returned. | An accepted order and stock reservation exist; payment has not yet occurred. |

## Unresolved business decision

Inventory synchronization can reveal a shortage after an order has already been accepted. The required customer and operational outcome in that state is not yet defined. In particular, this document does not authorize automatic cancellation, substitution, or refund behavior.

The operations manager owns the decision among cancellation, substitution, refund, or another recovery policy. Requirements and acceptance criteria for that recovery path must be added only after the decision is approved. Until then, the normal acceptance requirements above are valid, but the post-acceptance shortage path is explicitly unspecified.

## Verification

Requirement verification must cover each acceptance example and confirm the resulting order-number, reservation, and payment state. Verification of post-acceptance shortage recovery is blocked pending the operations manager's policy decision; no recovery outcome should be treated as approved in the meantime.
