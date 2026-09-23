# Connect the workflow to the project's engineering system

Use when starting a project or a cross-boundary change whose working rules are missing or conflicting. Reuse existing project instructions and decisions; a routine local edit does not need onboarding. Resolve only what the next slice depends on, not the entire future architecture.

Build a short map in the project's existing source of truth, or the conversation when sufficient:

| Find or settle | Connect it to |
|---|---|
| Domain terms, invariants, accepted examples and open business decisions | Authoritative requirement and the person/role who can settle an unknown |
| Module responsibilities, dependency direction and data-write ownership | Existing API/schema, a representative implementation, relevant architecture checks |
| Shared contracts, permissions, transactions and migration policy | Contract owner and the checks protecting affected boundaries |
| Commands and environments for this slice | What each check proves, how it is invoked locally/in CI, unavailable prerequisites |
| Current work, integration owner and recovery state | Existing tracker, branch/isolation policy and evidence location |

Link to maintained sources rather than duplicating their content. Check the relevant guidance against the effective decisions and current entrypoints: a missing reference or obsolete version is a gap to reconcile, not a reason to recreate retired structure. Code alone does not establish which convention was approved. Keep the current agreement readable without replaying its history; retain superseded decisions separately or clearly mark them. Repair affected guidance within scope, without an unrelated documentation rewrite.

When asked to follow a reference project, inspect a representative implementation and its maintained rules. Establish which responsibilities, dependency directions, boundary objects and shared-code ownership are inherited, which differ, and which remain unresolved. Apply explicit choices without asking again; surface consequential conflicts with the target project's accepted constraints. Directory names alone do not establish equivalence. Do not import business models, secrets, historical exceptions or a whole toolchain merely because they occur in the reference.

Check one representative working slice against the inherited conventions before multiplying similar implementations. Reuse an existing verified slice when applicable; do not require a new scaffold or approval stage for routine work. Keep stack-specific layouts and style choices in an explicitly selected project reference, not in universal workflow rules.

For a mechanically checkable constraint, locate its enforcement. A documented command that CI never runs is different from an active gate. When authorized and proportional, connect or repair the existing check and demonstrate that it catches a representative violation as well as accepting valid behavior. Associate it with the protected rule, scope, diagnostic and legitimate exceptions. Use semantic review for responsibilities the check cannot decide. Otherwise state the enforcement gap; do not claim documentation prevents violations. A failed gate calls for an implementation fix unless evidence establishes a check defect or an accepted rule change.

For relevant prior lessons, load only those matching this project's domain, stack or failure boundary. Confirm that their assumptions still apply and their safeguards run here. Keep local exceptions explicit, with a reason and a condition for reconsideration; do not copy every historical rule into every new project.

When concurrent contributors need shared ownership, specification-dispute resolution or change notifications, use [collaboration.md](collaboration.md). Keep the effective agreement and evidence in the existing project workflow. Roles do not require a fixed agent count, and a shared coordination service is optional. A clean merge and separate green checks do not establish integrated correctness.

When the project offers specialist skills, select them from the requested outcome, affected stack and their stated scope. Give contributors the relevant skill and project convention pointers; do not make the user choose internal routes. A broad coding-style skill does not replace a maintained project rule or representative implementation. Check the resulting code against those sources, not against a claimed agent specialty or skill invocation.

When writing a project specialist skill, make its activation scope and applicable check explicit. If the accepted behavior changes a boundary that existing tests do not cover, direct that specialist to leave one focused regression in the existing tests. Keep this instruction with the responsible project skill rather than adding testing ceremony to unrelated tasks.
