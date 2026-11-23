# Conditional React behavior checks

**ID:** `dev.stack.react` · Behavior-check baseline available; project architecture/library choices remain project-bound. Use for an affected React state/effect scenario, or when the adapted section's triggers apply, not every JSX or copy edit. Confirm the installed React and host-framework versions and preserve existing routing, data and component conventions.

## State and event ownership

Trace the state owner and the render that created a handler. State writes schedule another render; an existing handler keeps its render's values. Check delayed callbacks or successive updates against the intended operation rather than assuming a setter immediately changes that local value. See [state snapshots](https://react.dev/learn/state-as-a-snapshot).

Separate a derivable display value, event-triggered action and synchronization with an external system. Reuse the project's established mechanism; do not add duplicated state or an effect solely to copy derivable props/state. See [when an effect is unnecessary](https://react.dev/learn/you-might-not-need-an-effect).

## Effects and asynchronous work

For a changed synchronization effect, identify its reactive inputs and owned subscription, timer or request. Check matching cleanup and stale-result handling when the input changes or the component unmounts. A development setup/cleanup cycle exposing a leak needs a scoped repair, not a default removal of the project's development checks. See [effect synchronization and cleanup](https://react.dev/learn/synchronizing-with-effects).

Cancellation or ignoring an obsolete response protects client state; it does not undo an accepted server write. Use [async/idempotency](../rules/async-idempotency.md) or [concurrent edits](../rules/concurrent-edits.md) when that actual business boundary is involved.

## Verify and bind

Use accepted examples to check the affected event/render result, changed input, relevant obsolete response and cleanup. Test only the boundary changed; a synchronous text edit needs no asynchronous matrix. Distinguish client behavior, service integration and user acceptance through the scenario's owning evidence rules.

These official sources describe current React behavior; verify the relevant API against the installed version before use. Framework server/client boundaries, state/query libraries, component packages, naming/layout and test commands remain the selected project's existing choices. This file authorizes no new package or upgrade.

## Adapted from public sources (unconfirmed for the team)

Also read for a change to data loading, a server/client boundary, a heavy import or a shared component's props. A project or team rule wins where they differ.

- Start independent requests together and await them together. Where B needs only A, chain B onto A so C is not held back.
- With TanStack Query, queries in sibling components and plain `useQuery` calls run in parallel; several suspending queries in one component run one after another. The waterfall is a query enabled by another's result, or a child mounted only after its parent's data.
- In a server-rendered tree an awaited fetch in a parent blocks every child. Fetch in siblings and wrap the slow part in `Suspense` so the shell streams first.
- A server action is a public endpoint. Validate, authenticate and authorize inside it; a middleware or page guard does not cover a direct call.
- Never hold request or user data in a mutable module-level variable on the server: concurrent renders share it.
- Pass a client component only the fields it reads. Every prop crossing the boundary is serialized into the page.
- Load a heavy component that the first render does not need (editor, chart, map) with a dynamic import and a literal path. A variable path makes the bundler include every candidate.
- A named import from a large barrel entry can load the whole package on a cold start. Use the build's existing import optimisation, or the library's documented per-module path if it ships types.
- Run the effect of a click or submit in its handler, not through state plus an effect.
- Never define a component inside another component's body. It remounts on every render: an input that loses focus on each keystroke is the sign.
- When a shared component is about to gain another boolean mode prop, split it into explicit variants composed from shared parts.
- Build-time variables exposed to the browser are public; no secret goes in them. A link or redirect target taken from data is a relative path or an allowlisted `https` origin, never `javascript:`.
