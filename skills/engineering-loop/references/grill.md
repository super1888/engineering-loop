# Challenge the current slice across routes

Apply this built-in grill-me-style check to every engineering stage and selected specialist skill. Its purpose is to counter agreement bias: an agent tends to adopt the asker's framing, confirm the proposed solution and stop looking. Find where the request or plan is wrong before work depends on it. Reuse answers while their relevant conditions remain unchanged; a stage or specialist change needs only its affected questions, not a restarted interview. No external grill-me installation or tool is required.

## Choose the depth

| Depth | Use for | Minimum |
|---|---|---|
| **Light** | A clear, local, reversible task inside settled decisions, such as an approved copy edit or a scoped fix | Steps 1–2 of the method, and step 4 whenever evidence contradicts the request. Zero user questions is valid when evidence settles them |
| **Full** | Every stage 01 or 02 deliverable (requirements, product or technical design, architecture, delivery plan); a decision in another stage that is costly to reverse or makes a new commitment on architecture, permissions, stored data or external effects beyond what was already accepted | The whole method and the written outputs for that decision. Stage 01 and 02 deliverables also need the independent check and the gate |

Depth follows the decision, not the asker's confidence or urgency. Implementing accepted behavior in stage 03, including a scoped fix, stays Light unless it makes such a new commitment. Only the decision owner can waive a Full step, explicitly and by naming the step. Saying the matter is already decided or urgent is not a waiver: give the evidence and written outputs briefly, then follow the owner's decision. Record what was waived and by whom, and do not present the result as fully challenged.

## Method

1. **Separate the problem from the proposed solution.** Restate the outcome the person needs and treat their suggested solution as one candidate. Read available project evidence first, or delegate the lookup; never ask the user for facts the project or tools can supply. Distinguish an observed fact, accepted decision, proposal and unknown; investigate conflicts rather than silently choosing one source.
2. **Find the decisive assumption** and one relevant failure example or legitimate exception. Check whether accepted behavior and evidence address it. When discussion cannot settle an empirical or visual question, propose a bounded investigation or representative prototype within existing authority rather than rephrasing the question.
3. **Ask in dependency order.** Ask only questions whose prerequisites are settled and whose answer changes behavior, acceptance, authority or costly rework. While the problem itself is still unclear, ask open questions without offered options, because options steer the answer. Once the problem is clear, give each narrow decision a recommendation, meaningful alternatives, consequences and reversibility. Batch independent questions; respect a preference for one at a time.
4. **Disagree with evidence.** When facts conflict with the asker's stated view, say so plainly and show the evidence before proceeding. Do not soften a supported objection into agreement, and do not drop it after pushback that adds no new fact. Follow the authorized owner's informed choice and record it as their decision with its accepted cost; do not reopen it without new facts.
5. **Hold dependent work.** Keep implementation and external actions that depend on an open decision waiting for it. Silence is not acceptance. Continue independent authorized work and make low-impact reversible engineering choices under existing authority. Do not introduce another approval merely because the route changed.
6. **Stop** when no unresolved decision can change the current slice and evidence supports its next action. A bounded investigation can itself be that slice.

## Full depth: written outputs

Produce these before presenting the result as ready. Put them in the stage record's existing fields (for example the interview and review tables of the requirements record, or the assumptions and pending items of the plan), otherwise in the task record or reply. They are content, not a new document or a template change.

- **Assumptions:** each assumption the conclusion depends on, marked as a sourced fact, confirmed by a named person, or unverified.
- **Alternative:** at least one materially different option, including doing less, reusing what exists or not building, with the reason it lost. If no credible alternative exists, say why.
- **Disconfirming case:** the concrete situation in which the preferred option fails, and the evidence that would reveal it.
- **Coverage:** every stated requirement and every effect found during the challenge, marked covered, excluded (by whom) or open.
- **Open decisions:** each with its owner and the work that waits on it.

## Full depth: independent check and gate

Before presenting a stage 01 or 02 deliverable as ready, have a reviewer in fresh context examine it where the host provides one. This deliverable is the stated need for that reviewer; it does not add reviewers to other work. Give it the original request, accepted facts and the draft only, without the author's reasoning, summary or conclusion. Ask what is missing, wrong, unsupported or more than the confirmed scope needs. Reconcile each finding against evidence; another agent's agreement is not proof. When no independent reviewer is available, state that the deliverable was not independently checked.

Do not implement, scaffold, create the planned task batch or take an external action that depends on a stage 01 or 02 result until its decision owner has confirmed the recorded result. Preparing the draft, investigating and bounded prototypes requested for the decision are not blocked. Authorization given earlier to build or to create tasks stays valid and is not asked again: it takes effect once the result it depends on is confirmed. Confirming the recorded result is one step, not a new approval for each action.

## Signs of going along

Stop and return to the method when any of these appears:

| Sign | Correction |
|---|---|
| Agreeing with a claim that was not checked | Check it or mark it unverified |
| Planning the suggested solution before stating the problem | Return to step 1 |
| Asking for facts the repository or tools hold | Look them up |
| Offering options before the problem is understood | Ask an open question |
| Withdrawing a supported concern after pushback without new facts | Restate the evidence; let the owner decide and record it |
| Declaring a design ready without the written outputs | Produce them |
| Adding components, states or safeguards nobody required | Tie each to a confirmed requirement or remove it |

Passing this check means the current decisions support proceeding. It does not guarantee that no problems remain, replace actual verification or review of the implementation, or authorize work beyond the user's scope.
