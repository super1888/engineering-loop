# Coordinate implementation, specification and verification

Use when concurrent contributors need ownership, disagreement resolution or contract-change coordination. Delegate only when available, authorized and useful. Roles are responsibilities, not a required agent count: a coordinator, implementer and verifier may suffice; separate specification and test work only when their scope justifies it. A small local task needs no agent team or coordination service.

## Assign bounded ownership

| Responsibility | Owns | Authority boundary |
|---|---|---|
| Coordinator | Effective agreement, task boundaries, dispute routing and integrated acceptance | Resolves engineering choices within existing authority; routes consequential business or scope decisions to the authorized owner |
| Implementer | Scoped code, self-checks and evidence of specification problems | Does not silently change accepted behavior or weaken acceptance |
| Specification reviewer (SDD) | Alignment with effective requirements and architecture; maintenance of accepted specification changes | Can challenge both code and specification, but cannot invent business policy |
| Test verifier (TDD where useful) | Expected outcomes from accepted examples, boundary tests and integrated behavior | Does not derive correctness solely from the implementation or rewrite expectations merely to pass |

Give each contributor only the relevant agreement/version, paths and contracts owned, prerequisites, expected result and checks. Agree who owns shared files and integration before overlapping work. Serialize conflicting writes, including specification/test files and shared build or Git state, according to project policy. Do not assign two agents the same repair without a concrete reason.

## Resolve disagreements with evidence

An implementer or reviewer challenging a specification provides the effective rule, a concrete conflicting fact or usage scenario, consequence, proposed correction and affected work. The coordinator distinguishes:

- Stale text or a check defect with an established authoritative answer: correct within scope and retain the basis; do not re-ask a settled decision.
- A different implementation preserving accepted behavior: decide within existing engineering authority.
- An unresolved contradiction or consequential change to business behavior, acceptance or architecture: use [requirements.md](requirements.md) to investigate and obtain the appropriate decision, with alternatives and impact.

Documentation is not immune to correction, and implementation convenience is not evidence that it is wrong. Agent agreement or majority vote does not settle a disputed requirement. Pause only work dependent on the unresolved decision; continue independent authorized work. If investigation adds no evidence, report the concrete decision/blocker rather than cycling between speculative implementation and review.

## Keep active work on the effective agreement

Reuse the project's tracker or task state for the effective agreement/version, ownership, unresolved decisions and evidence pointers. An accepted change records what it supersedes and sends the relevant delta to affected contributors. Identify impacted code, tests and prior evidence; revise or stop obsolete dependent assignments before their results are integrated. Reading a message is not proof of adaptation: check that returned artifacts use the effective agreement. Do not broadcast whole histories or make every agent reload all references.

An existing file or message can be sufficient. Propose a shared coordination service only for demonstrated needs, with appropriate authorization; it is not a prerequisite. If used, distinguish advisory ownership from enforced writes and handle stale reservations. Notifications do not replace reconciliation.

## Review meaningful boundaries

Review the first representative slice before replication, a material shared-contract change, an explicit specification conflict, or the integrated result. Select checkpoints by current risk rather than reviewing every edit or continuously polling unfinished code. Findings name the relevant agreement and identifiable code state, trigger, consequence and evidence. Code changes invalidate only affected findings and checks; reuse still-valid results.

For critical behavior, establish test expectations from accepted scenarios before or alongside implementation where useful. A verifier may inspect code for risks, but expected results need an independent basis. Preserve legitimate alternative implementations and exceptions. Source conformance, observable behavior and task usefulness require different evidence; use [verification.md](verification.md).

The coordinator reconciles findings, accepted specification changes and affected contributor results, then verifies combined behavior at an identifiable integrated state. Separate green checks or a clean merge are insufficient. Report passed, failed and unrun evidence and any remaining decision. Stop when the requested result and required checks are complete; extra reviewers need a current unresolved reason.
