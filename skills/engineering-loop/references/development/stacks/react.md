# Conditional React behavior checks

**ID:** `dev.stack.react` · Behavior-check baseline available; project architecture/library choices remain project-bound. Use only for an affected React state/effect scenario, not every JSX or copy edit. Confirm the installed React and host-framework versions and preserve existing routing, data and component conventions.

## State and event ownership

Trace the state owner and the render that created a handler. State writes schedule another render; an existing handler keeps its render's values. Check delayed callbacks or successive updates against the intended operation rather than assuming a setter immediately changes that local value. See [state snapshots](https://react.dev/learn/state-as-a-snapshot).

Separate a derivable display value, event-triggered action and synchronization with an external system. Reuse the project's established mechanism; do not add duplicated state or an effect solely to copy derivable props/state. See [when an effect is unnecessary](https://react.dev/learn/you-might-not-need-an-effect).

## Effects and asynchronous work

For a changed synchronization effect, identify its reactive inputs and owned subscription, timer or request. Check matching cleanup and stale-result handling when the input changes or the component unmounts. A development setup/cleanup cycle exposing a leak needs a scoped repair, not a default removal of the project's development checks. See [effect synchronization and cleanup](https://react.dev/learn/synchronizing-with-effects).

Cancellation or ignoring an obsolete response protects client state; it does not undo an accepted server write. Use [async/idempotency](../rules/async-idempotency.md) or [concurrent edits](../rules/concurrent-edits.md) when that actual business boundary is involved.

## Verify and bind

Use accepted examples to check the affected event/render result, changed input, relevant obsolete response and cleanup. Test only the boundary changed; a synchronous text edit needs no asynchronous matrix. Distinguish client behavior, service integration and user acceptance through the scenario's owning evidence rules.

These official sources describe current React behavior; verify the relevant API against the installed version before use. Framework server/client boundaries, state/query libraries, component packages, naming/layout and test commands remain the selected project's existing choices. This file authorizes no new package or upgrade.
