# Worked scenarios (illustrative, not benchmark results)

## A bounded bug

**Request:** “Logout fails, but the UI shows me as signed out. Fix it.”

Investigate the existing session behavior and tests. Reproduce a rejected logout, preserve the current session on rejection, show an actionable retry result, and verify successful logout still clears the session. Reuse the project's checks. Do not create an architecture document or ask again whether logout should work.

## An uncertain batch feature

**Request:** “Make imports faster and handle failures.”

Measure queue time versus processing time. Ask about unresolved duplicate and partial-failure behavior in the same round if independent. After that choice, determine the necessary recovery UI. Implement one complete slice before expanding concurrency; verify no duplicate side effects after a lost response. Do not invent a universal thread count.

## Resuming after an architecture replacement

**Request:** “Continue from the handoff.”

The handoff references a deleted adapter. Inspect its recorded revision, the replacement change, current entrypoint, and accepted decisions. Update the effective task state rather than recreating the removed architecture. Ask only if the desired behavior remains ambiguous.

## Small change: leave quietly

**Request:** “Change the Save button label to Save draft.”

Apply the existing project workflow and relevant consistency checks. No broad interview, lifecycle plan, new dependency, or release operation follows from this request.

## Preparing a release

**Request:** “Prepare this approved feature for release; do not deploy.”

Identify the verified revision, artifact, configuration and migration/recovery needs. Produce a reviewable release note and unrun-check list. Do not publish. If publication is already explicitly authorized in another task, reuse that scope rather than inventing a new approval gate.
