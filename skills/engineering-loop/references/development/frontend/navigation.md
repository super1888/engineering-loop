# F4 Routing and navigation

**ID:** `dev.frontend.navigation` · **Status:** available execution baseline; router conventions remain pending.

## Scope and inputs

Use for route parameters, entry/return paths, retained context or page access changes. Identify the affected entry points, accepted URLs/parameters, navigation-state owner, main action and supported back/exit destination. Styling that preserves navigation needs no route redesign.

Retain the relevant [UI task/return-path guidance](../../ui.md#start-with-a-task-and-representative-content) and [observed interaction requirements](../../ui.md#accept-the-rendered-behavior).

## Execute

1. Trace direct entry and in-app navigation through the actual router. Establish which state belongs in the URL, a page-local draft or an existing shared store; follow the maintained contract instead of adding a second state owner.
2. Preserve identity through parameter parsing/encoding; use [R1](../rules/data-fidelity.md) for affected identifiers. Handle invalid or missing input according to the existing outcome, without guessing a resource or policy.
3. Follow the representative task through its action and supported return. Retain the agreed filter/context and display changed data where the accepted flow requires it; consult the affected integration path when state crosses screens.
4. If access changes, apply [R2](../rules/access.md) at the real resource boundary. A hidden navigation item or client guard alone does not establish authorization.
5. Reuse existing dirty-exit, redirect and fallback behavior. A navigation fix does not authorize new confirmation dialogs, browsing history replacement or a new cancellation policy.

## Verify

- Exercise relevant direct/deep entry, normal navigation and the affected back/return path; check both destination and retained visible context.
- Where applicable, use an invalid/unauthorized parameter control alongside a valid one without relaxing accepted access or error behavior.
- For changed focus/navigation interaction, use [R9](../rules/rendered-ui.md); source route registration alone does not prove a usable return path.

## Deliver

Record affected routes/parameters, accepted entry/exit behavior, context ownership and actual path evidence through [delivery records](../delivery.md). Keep route documentation and callers consistent only where this change affects them.

## Team binding — pending

Router package/version, URL/query ownership, route inventory and navigation component conventions remain supplied by each project; no new routing framework or universal redirect policy is introduced.
