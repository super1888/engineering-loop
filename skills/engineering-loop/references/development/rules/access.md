# R2 Identity, roles and resource access

**ID:** `dev.risk.access` · **Status:** available verification pointer; project role/resource policy remains project-owned.

**Trigger:** The affected path changes identity propagation, role checks, resource ownership or access shared by users. Follow the actual actor and resource through the changed calls; a frontend/backend label does not bound that path.

Read and apply [Cross-user and role access](../../verification-boundaries.md#cross-user-and-role-access). That section owns the access-path evidence requirement and its successful/unauthorized controls. Reuse the project's maintained permission contract; an unresolved business permission is not a policy to invent in implementation.

**Nearby exception:** A formatting-only change that does not affect access need not create a new role matrix. Existing authorization remains effective, including on the ordinary successful path.

**Verification:** Identify the actor, owned/shared resource, expected allowed and rejected results, artifact and environment in the existing acceptance record. Concrete role matrices and framework middleware conventions are pending project/team detail, not supplied here.
