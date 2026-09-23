# Worked scenarios (illustrative, not benchmark results)

## A bounded bug

**Request:** “Logout fails, but the UI shows me as signed out. Fix it.”

Investigate the existing session behavior and tests. Reproduce a rejected logout, preserve the current session on rejection, show an actionable retry result, and verify successful logout still clears the session. Reuse the project's checks. Do not create an architecture document or ask again whether logout should work.

## An uncertain batch feature

**Request:** “Make imports faster and handle failures.”

Measure queue time versus processing time. Ask about unresolved duplicate and partial-failure behavior in the same round if independent. After that choice, determine the necessary recovery UI. Implement one complete slice before expanding concurrency; verify no duplicate side effects after a lost response. Do not invent a universal thread count.

## A bounded order-flow requirement

**Request:** “Document the online ordering flow for our bar. Do not implement yet.”

Suppose the accepted online scope is listed drinks and snacks; staff may handle off-menu requests separately. Document one successful menu order and three distinct boundaries:

| Guest request | Meaning | Observable outcome before an order or charge |
|---|---|---|
| Unclear item name | The product cannot yet be identified | Ask the guest to clarify; do not guess a menu item. |
| Fried rice, known to be off-menu online | The requested product is identified but unsupported in this flow | Explain the online scope; do not create an online order. Staff handling remains a separate path. |
| A listed drink now sold out | The item is supported but temporarily unavailable | Show the availability change and let the guest choose again; do not describe it as permanently excluded. |

Define exactly when “order accepted” promises fulfillment and what effects may already have occurred. If stock can disappear after that point, record the unresolved cancellation, substitution or refund decision with its owner before specifying recovery behavior. These examples illustrate the distinction; they are not universal menu or payment rules.

## Resuming after an architecture replacement

**Request:** “Continue from the handoff.”

The handoff references a deleted adapter. Inspect its recorded revision, the replacement change, current entrypoint, and accepted decisions. Update the effective task state rather than recreating the removed architecture. Ask only if the desired behavior remains ambiguous.

## Small change: leave quietly

**Request:** “Change the Save button label to Save draft.”

Apply the existing project workflow and relevant consistency checks. No broad interview, lifecycle plan, new dependency, or release operation follows from this request.

## Preparing a release

**Request:** “Prepare this approved feature for release; do not deploy.”

Identify the verified revision, artifact, configuration and migration/recovery needs. Produce a reviewable release note and unrun-check list. Do not publish. If publication is already explicitly authorized in another task, reuse that scope rather than inventing a new approval gate.

## Starting a domain-heavy project

**Request:** “Build purchasing and inventory with our domain expert.”

Map existing terms, module/data ownership, commands and current work. For the first receipt slice, ask the expert about unresolved over-receipt, retry and reversal behavior using concrete quantities. Record confirmed examples and open decisions in the existing requirement source. Implement and verify one complete receipt behavior before generating other document types. Do not invent accounting policy or demand decisions about every future module.

## Integrating concurrent contributions

Two contributors own purchasing and stock. They first agree who owns the receipt contract and which module writes stock. One proposes a new quantity unit while the other uses the existing unit. Resolve that shared decision before overlapping implementation; a merge without textual conflicts cannot settle it. Verify the integrated receipt path with the accepted unit and failure behavior.

## Transferring a demonstrated lesson

A receipt retry once increased stock twice. Preserve a regression showing the failure and the valid distinct-receipt case. Record why existing tests missed the retry. In a second project, inspect whether the same operation-identity boundary exists, then adapt and run the safeguard there. Do not mandate a particular database or a global ban on retries. Until the new project's check runs, the lesson has been considered, not demonstrated as adopted.
