# Conditional Vue behavior checks

**ID:** `dev.stack.vue` · Vue 3 behavior-check baseline available; team conventions remain project-bound. Confirm the actual Vue/compiler version and Options/Composition API style before selecting a check. This is not an upgrade instruction or a Vue 2 coding standard; a copy-only edit does not need this body.

## Reactive values and props

Trace which reactive object/ref/getter the consumer observes. Destructuring an ordinary reactive object's primitive field can disconnect it from later changes; replacing the tracked object reference can also break an existing connection. Check the actual usage, including ref unwrapping context. See [reactivity fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html).

Keep the project's accepted ownership between parent props and child updates. Check the installed compiler before judging destructured props: Vue 3.5+ supports the documented reactive destructure transform in the same script-setup block, while passing a resulting value to a watcher/composable is different from passing a reactive source. Do not impose a blanket destructuring rewrite. See [props and reactive destructure](https://vuejs.org/guide/components/props.html).

## Watchers and asynchronous work

For an affected watcher, identify the source, result owner and cleanup of obsolete work. Use an API supported by the installed version; `onWatcherCleanup` requires Vue 3.5+ and synchronous registration. Check flush timing only when the callback needs the updated component DOM. See [watcher cleanup and timing](https://vuejs.org/guide/essentials/watchers.html).

Ignoring or cancelling a stale client request does not reverse a server commitment. Follow [async/idempotency](../rules/async-idempotency.md) or [concurrent edits](../rules/concurrent-edits.md) only when that boundary applies.

## Verify and bind

Verify the actual source changing, a relevant obsolete response and owned cleanup through the accepted visible result. Preserve legitimate compile-time reactivity and existing version/API conventions. Do not introduce polling, two-way ownership or a recovery policy merely to fix a local update.

The linked official sources cover current Vue 3. Resolve version-specific behavior before applying it. Router/store/form/UI libraries, component events, directory conventions and verification commands remain the selected project's existing bindings; this body selects none of them.
