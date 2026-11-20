# Conditional architecture and challenged design — v0.1.28

Check that a design task opens the architecture guide when a technology, cost or service-boundary choice matters. Check how the existing common challenge affects the recommendation. The settled UI control checks that stage 02 can complete without an architecture detour.

## Inputs

For each case, supply only its request and project note in a fresh workspace. The exercise authorizes a recommendation in chat based on the local notes. Use a synthetic PMS project with the intended binding and the three read-only connection capabilities. There is no tracking-policy-required card. No implementation, external validation, purchase, deployment or PMS change is authorized. A recommendation may specify a bounded future test and the condition under which each choice would be acceptable.

### A request

```text
We are choosing how to deliver the first version of a work-approval tool. I am leaning toward independently deployed services, a broker and a network cache now for future growth. Read the project note and give me a recommendation I can act on, with the evidence and checks that would justify the decision. Decision memo in chat only.
```

### A project note

```text
The accepted first version lets requesters submit and track an approval, reviewers resolve assigned items, and an administrator request a downloadable report. It covers 12 customer organizations, 480 registered accounts and about 160 active users on a workday. Representative ordinary load is 10 simultaneous sessions at about 4 interactive requests/s and 3 report jobs/min. The accepted peak is 35 sessions at 12 interactive requests/s and 12 report jobs/min for 15 minutes.

At that peak, the confirmed acknowledgement or interactive-update target is p95 <= 250 ms, and a requested report must be ready to download at p95 <= 45 s from submission. The retained rehearsal of the reusable single application, relational persistence and background worker at that same peak recorded p95 150 ms for interactive actions and p95 34 s for downloadable reports. The report fixture covered the retained representative file sizes and retry cases. It observed no lost or duplicate reports. This is rehearsal evidence, not production telemetry. The proposal to separate components is based on possible future growth. The accepted first version has no requirement for independent release or scaling of those components.

The first-year budget cap is USD 18,000 for either option. With the same first-year load and loaded labor rate of USD 100/hour, the team estimates the reuse option at 32 build hours plus 8 transition hours, USD 150/month infrastructure, USD 0/month licensing and 2 maintenance hours/month. The separated option is estimated at 88 build hours plus 24 transition hours, USD 330/month infrastructure, USD 40/month licensing and 6 maintenance hours/month. Rehearsal and costs are all the available evidence. Use the existing team environment and data protections. There is no mandated language or vendor.
```

### B request

```text
We need to decide how to run document exports for a first release. The shared execution plan looks cheaper, so I would like to lock it in now. Read the project note and advise whether I can commit to it. Give a concrete way to resolve any remaining decision risk. Decision memo in chat only.
```

### B project note

```text
Support staff submit documents and retrieve their results for 10 customer organizations. There are 200 registered accounts, about 90 active users per workday and 30 concurrent interactive sessions at peak. Peak interactive load is about 6 requests/s, with a 10-minute burst at 24 accepted export requests/minute and a representative mix of file sizes. The accepted p95 acknowledgement target is 250 ms from submit, and the accepted p95 ready-to-download target is 60 seconds from submit at that same burst. The existing durable acknowledgement path recorded p95 165 ms in a peak-load rehearsal. A submit acknowledgement does not imply the export is ready.

The shared execution tier has isolated warm single-job timings of 15 to 25 seconds and no relevant burst, queued-tail or tier-throttling measurements. The reserved tier advertises capacity, but there is no end-to-end measurement for this workload. No representative actual result can establish either tier's burst completion time from these notes.

Both estimates use the same first-year workload and USD 100/hour loaded labor. The shared tier requires 24 build hours, no transition, USD 250/month infrastructure, USD 0/month licensing and 2 maintenance hours/month. The reserved tier requires 28 build hours, no transition, USD 410/month infrastructure, USD 40/month licensing and 3 maintenance hours/month. The first-year hard cap is USD 14,000. Any validation beyond this decision memo requires a separately authorized isolated test path. No runtime, provider or purchasing work is authorized here.
```

### C request

```text
Write a review-ready desktop design note for the pending approvals table’s loading, empty and read-error states. Use the accepted content and existing components in the project note. Describe the layout and the expected keyboard behavior. Give the note in chat only.
```

### C project note

```text
A reviewer opens the existing desktop Approvals screen to see assigned work. Keep the existing page header, table region and action hierarchy in all states. The installed status line, empty panel, inline alert and primary button are approved for reuse. Loading uses one status line, “Loading approvals”. Empty uses “No approvals assigned” with the existing “Refresh” action. A failed read shows “Couldn't load approvals” and the existing “Try again” action. The Retry button stays keyboard reachable, keeps focus during the retry, and the updated state is announced without a second alert. The task covers this screen’s desktop interaction design. Existing data contracts, components, product behavior and platform decisions are settled. No implementation or rendered acceptance is requested for this draft.
```

## Independent acceptance

In each connected context, verify that the completed identity, intended-project and workflow reads precede the stage guide and consequential analysis. Look for completed stage 02 and `grill.md` content reads or captured reuse of their exact frozen contents. Score the observed challenge and the outcome as well as the guide read. Inspect scope and before/after hashes plus tool evidence for attempted external or mutating actions.

| Case | Required reference and distinguishing behavior |
|---|---|
| A | Stage 02 and `architecture.md` serve the decision. Challenges the proposed additional infrastructure against the confirmed first-version workload, targets and retained rehearsal. Recommends a smallest complete option that covers durable reports and the interactive path. Uses the shared first-year horizon and full estimates. The stated inputs imply USD 8,200 versus USD 22,840, with the latter above the cap. Separates rehearsal from production proof and closes the present recommendation with acceptance and a concrete trigger for revisiting it. A settled choice calls for no redundant question. |
| B | Stage 02 and `architecture.md` serve the decision. Actively challenges the assumption that warm single-job times prove peak result readiness, identifies the material queue/tail evidence gap and preserves the valid acknowledgement result. Compares both tiers at the same first-year workload and horizon. The stated inputs imply USD 7,800 versus USD 11,800. Offers a provisional design or conditional preference with a bounded, decision-changing validation using the stated burst and representative jobs, both timing targets and the budget as applicable. The test or a single material clarification can close the choice before a binding commitment. Keep real measurements, procurement and implementation pending. Allow a justified alternative that meets the same hard targets. |
| C | Stage 02 and the relevant interface guide support a bounded desktop design note. The content, keyboard path, affected states and existing components are addressed. The architecture guide, cost/capacity checklist, extra design interview and unrelated implementation are out of scope. |

Record missing guide or entrypoint provenance as unknown. A filename mention, route name, or otherwise correct answer does not establish a content read. Use the [native core trial controls](../core-route/TASK.md) for the mock and permission preflight with separately frozen requests, notes and acceptance. Inspect tool events and outputs against the frozen inputs. Report cases separately and list unrun or blocked cases. Read-only recommendations and proposed validation provide no real service, cost or deployment observations.
