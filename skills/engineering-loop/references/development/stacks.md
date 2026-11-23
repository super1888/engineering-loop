# Bind actual module stacks to maintained conventions

Read when a selected scenario's change can be affected by stack-specific rules, or when maintaining a binding. Discovery, conditional React/Vue behavior checks and partial team rule files for some stacks are available; other team-specific choices remain **pending** unless the selected project supplies them. A team rule file records extracted team practice awaiting confirmation; nothing here authorizes a new framework, package or upgrade.

## Discover and select

- Identify the affected module, language/framework and relevant version from its actual manifests, build/lock files, entrypoints and representative implementation. A top-level package list or a user keyword alone may not identify a monorepo module.
- Preserve effective AGENTS/project instructions and their full-read requirements. A stack binding narrows optional specialist detail; it cannot waive a project rule or authorize an upgrade, dependency installation or parallel framework.
- Select an existing maintained reference or available specialist only within its stated scope/exclusions. Use [specialists.md](../specialists.md) when selecting/delegating one. Do not load unrelated framework guides.
- If a missing fact is inspectable, investigate it. Ask only if a consequential unresolved choice affects this slice. With no specialized standard, reuse the project's actual conventions; block only a necessary unresolved condition.

## React

Read [React behavior checks](stacks/react.md) only when an affected React state/effect boundary is involved, or when its adapted section's triggers apply (data loading, a server/client boundary, a heavy import or a shared component's props). Use the installed runtime/framework and its maintained project rules; a copy-only edit does not need this body.

Team-specific conventions: read [team frontend rules](stacks/frontend-team.md) before implementing a component, style, data-handling or test change in a React module. A settled copy-only edit does not need them. They cover components and styles, antd 6, data handling and testing, and list the product choices that remain open. They are partial: extracted from the team's products and awaiting confirmation as the shared standard.

## Vue

Read [Vue behavior checks](stacks/vue.md) only for the matching Vue 3 reactivity/props/watch boundary. Detect the actual version/API style first; Vue 2 work follows its own maintained project/version guidance. Team-specific conventions remain pending.

Team-specific conventions:

<!-- Reserved for an accepted reference, scope/version, representative example and owning check. -->

## Backend stacks

Status: partial. Bind the actual module's language, framework and persistence stack. Read the matching team rule file before implementing a change its rules can affect:

| Module stack | Team rules | Basis |
|---|---|---|
| Java / Spring with MyBatis-Plus | [java-spring.md](stacks/java-spring.md) | Two team services; mostly build-enforced in one |
| Python / FastAPI with SQLAlchemy | [python-fastapi.md](stacks/python-fastapi.md) | One team service |
| PostgreSQL or MySQL schema, index, migration or locking query | [sql.md](stacks/sql.md) | Public sources; unconfirmed for the team |

The first two files hold extracted team practice, not assumed language rules, and each lists the choices that remain open. Each also carries a separate section adapted from public sources; it is unconfirmed for the team and a team rule wins where they differ. Another stack has no team rule file yet: use the project's maintained conventions and do not borrow rules from a different stack.

## Engineering and other stacks

Status: pending. Library, script, CLI, tooling and other platform work use their maintained project sources.

Team-specific conventions:

<!-- Reserved for accepted bindings without imposing a Web-only taxonomy. -->

## Add a binding

Record stable ID, available/partial/pending/retired status, module/stack/version scope, trigger and exclusion, maintained reference, related scenario/risk conditions, representative example and verification. Keep source and version discoverable in the project's existing records; leave unknown ownership/version facts unknown. Promote a slot only when its actual guidance exists and has an applicable check.
