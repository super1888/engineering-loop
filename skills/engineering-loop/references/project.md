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

Link to maintained sources rather than duplicating their content. A representative implementation is a starting point to inspect, not proof that every detail should be copied. If none exists, establish one narrow working slice before generating many similar modules. Do not import a whole architecture or toolchain solely to fill the map.

For a mechanically checkable constraint, locate its enforcement. A documented command that CI never runs is different from an active gate. When authorized and proportional, connect or repair the existing check and demonstrate that it catches a representative violation as well as accepting valid behavior. Otherwise state the enforcement gap; do not claim documentation prevents violations.

For relevant prior lessons, load only those matching this project's domain, stack or failure boundary. Confirm that their assumptions still apply and their safeguards run here. Keep local exceptions explicit, with a reason and a condition for reconsideration; do not copy every historical rule into every new project.

When multiple people or agents work concurrently, agree affected files/modules, shared contract ownership, prerequisites and who integrates the result before overlapping implementation. Serialize unresolved shared-contract decisions; parallelize work whose boundaries are settled. Follow the project's Git and build-isolation policy. A clean merge and separate green checks do not verify combined behavior: check affected interactions on an identifiable integrated state.
