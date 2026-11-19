# F7 Accessibility and target devices

**ID:** `dev.frontend.accessibility-targets` · **Status:** available execution baseline; project support thresholds remain pending.

## Scope and inputs

Use for affected keyboard/focus, accessible controls, status feedback, zoom, long content or overflow. Apply the [target-device gate](../../ui.md#frontend-design-gate-desktop-by-default): desktop is the default; explicit and existing mobile behavior remains effective. Identify the representative task, affected state, target and claimed accessibility property.

## Execute

1. Follow the actual task with realistic content on the accepted target. Inspect the rendered control structure rather than assuming source attributes or a UI-library wrapper produce the intended role/name.
2. Traverse the affected interaction by keyboard. Check operability, visible focus and logical order; when opening/closing or navigation changes, preserve a useful focus destination through the accepted flow.
3. Inspect relevant control names, relationships, contrast and dynamic feedback. Apply [R9](../rules/rendered-ui.md) and its selected accessibility/status checks; a role/name assertion alone does not prove an announcement occurred.
4. Check the reported desktop width, long/missing content and actual browser zoom when relevant. A narrow window is not a phone requirement, and a smaller viewport is not proof of browser zoom.
5. Interpret automated scan results at the affected element. Keep definite violations, incomplete checks and manual findings distinct; do not alter colors solely to turn an uncertain scan green.

## Verify

- Record actual target, route, content/state and the affected keyboard or visible result. Use a nearby unaffected layout when a repair could regress it.
- Where the claim requires assistive-technology behavior, retain that actual evidence or report it unverified; DOM attributes and geometry cannot establish every accessibility claim.
- Do not use a broad new device matrix, forced interaction or fixed waits to hide an unresolved state. Unavailable required rendering/interaction evidence remains a limitation.

## Deliver

Record the property examined, actual observed result, scan/manual distinctions and unrun dimensions through [delivery records](../delivery.md). State the supported target without claiming broader device or accessibility certification.

## Team binding — pending

Browser/device support, accessibility thresholds and assistive-technology combinations remain project requirements. This guide does not impose a new certification target or authorize removing existing device behavior.
