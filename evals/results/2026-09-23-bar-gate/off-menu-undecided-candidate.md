# Online Ordering Requirements

## Scope

This document defines the current requirements for ordering drinks and packaged snacks through the online menu. It records unresolved business decisions without assuming their outcomes.

The following are outside this slice:

- Expanding the online menu.
- Taking payment; payment occurs after order acceptance.
- Defining staff handling of off-menu requests outside the online system.
- Choosing a cancellation, substitution, or refund policy for shortages discovered after acceptance.

## Current ordering behavior

1. A customer may submit an order for an identifiable item that is listed on the online menu.
2. Before accepting the order, the online flow must reserve the requested stock.
3. The order is accepted only after the stock reservation succeeds.
4. On acceptance, the system returns an order number.
5. Acceptance does not mean that payment has occurred.
6. If the item cannot be identified as a specific listed menu item, the system must not treat the request as a listed-item order or accept it through that path.
7. If a listed item has insufficient available stock, the system must not accept the order or return an order number.

## Observable examples

| Request | Classification | Required online outcome |
|---|---|---|
| One sparkling water, with five units available | Identifiable listed item with stock | Reserve one unit, accept the order, and return an order number. No payment has occurred at acceptance. |
| House lager, with zero stock | Identifiable listed item without stock | Do not accept the order and do not return an order number. |
| “星云特调” | Not yet identifiable as a specific menu item | Do not treat it as a listed-item order. Do not accept it or return an order number through the listed-item flow. This requirement does not decide whether an online off-menu-request flow will exist. |
| “蛋炒饭” | Known off-menu request | Online handling is not yet specified. The system must not assume either acceptance or rejection as the permanent policy until the bar manager decides whether online off-menu requests are allowed. |

## Inventory changes after acceptance

Inventory synchronization may reveal a shortage after an order has already been accepted and assigned an order number. Such an order must be distinguishable from an order rejected before acceptance: it remains an accepted order with a subsequently discovered fulfillment problem until an approved policy says otherwise.

The customer and operational outcome for this state is not yet specified. In particular, these requirements do not authorize automatic cancellation, substitution, or refund.

## Open business decisions

### Online off-menu requests

- **Decision owner:** Bar manager.
- **Decision needed:** Whether the online system may take off-menu requests, including a known request such as “蛋炒饭”.
- **Blocked requirements:** The online entry method, availability and price confirmation, acceptance criteria, customer messaging, and whether an order number may be issued for an off-menu request.
- **Current constraint:** Staff handling after manager confirmation does not establish permission for the online system to accept these requests.

### Shortage discovered after acceptance

- **Decision owner:** Operations manager.
- **Decision needed:** What happens when inventory synchronization reveals a shortage after acceptance.
- **Blocked requirements:** Customer notification and the rules for cancellation, substitution, or refund.
- **Current constraint:** No one of those remedies is the default, and payment timing does not by itself resolve the policy.

## Acceptance checks

- A listed, identifiable item with sufficient stock is reserved before acceptance, then receives an order number.
- A listed item with zero stock is not accepted and receives no order number.
- An unidentifiable request is not accepted as though it were a listed item.
- The requirements do not convert the known off-menu example into either an online acceptance rule or a permanent rejection rule.
- An accepted order affected by a later synchronization shortage is surfaced as an unresolved fulfillment state without inventing a cancellation, substitution, or refund outcome.
- Order acceptance and payment remain separate events.
