# F1 Components and styles

**ID:** `dev.frontend.components` · **Status:** available execution baseline; team components/tokens remain pending.

## Scope and inputs

Use for an authorized component, copy or style change. Design-only work stays in [stage 02](../../stages/02-design.md). Identify the affected component/callers, accepted content and action, actual target, existing design tokens and applicable state variants. Do not infer behavior from a visual reference alone.

## Execute

1. Locate the project's incumbent component and closest accepted usage. Reuse its public inputs, tokens and package conventions; use [template matching](../templates.md) only for an actual shared-template need.
2. Separate copy-only, visual and behavior changes. Keep a settled label edit local to the approved text; do not replace its handler, introduce a new button type or restart interface design.
3. For a real variant/state change, map each affected input to its observable result, including only relevant loading, disabled, focus or failure states. A destructive-looking variant does not authorize a destructive business action.
4. Preserve the control's action and semantics through composition: inspect the rendered interactive element and accessible name when those properties change, rather than assuming a wrapper forwards them.
5. Validate one representative usage before propagating a shared change. Inspect affected callers for incompatible defaults; add only the necessary variant instead of a parallel component system.

## Verify

- For settled copy-only work, compare the accepted text and preserve unrelated content and action; scoped consistency checks can suffice.
- For appearance/interaction claims, use [R9](../rules/rendered-ui.md) on the accepted target and affected states, including representative long content where it matters.
- When action availability or resource permission changes, apply [R2](../rules/access.md); hidden or disabled presentation alone is not access enforcement.

## Deliver

Record changed component/callers, reused source or template identity, affected inputs/states and the applicable consistency/rendering evidence through [delivery records](../delivery.md). Distinguish an implemented variant from an unverified visual proposal.

## Team binding — pending

Approved tokens, component packages/versions, variant names, icon set, template IDs and examples remain project/team choices. Bind them to an actual maintained source and owning check; this baseline supplies none of those defaults.
