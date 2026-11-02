# New-task product/UI advice follow-up

Freeze the tasks and acceptance below before execution. Compare baseline `f12204d3549848a9d585ec0a150dd3d931150cee` (0.1.12) with enhanced `8db89e7` (0.1.13). Use fresh CLI contexts, the same reduced provider configuration and explicit model, English-only replies, no tools or implementation. Supply matching entrypoint/requirements/verification references to both variants; enhanced additionally receives its UI reference. This compares supplied reference packages, not automatic discovery or a single rule. Keep raw prompts and outputs local; record prompt hashes and actual terminal results separately.

## Product task

“We are considering a daily AI digest for volunteer coordinators because the team likes AI. We have not established what coordinators miss or how they track work today. Recommend the next step in English, with at most three questions. Do not implement.”

Acceptance: (P1) examines the underlying coordination problem rather than assuming a digest; (P2) asks about current alternatives and concrete frequency/impact; (P3) proposes a bounded experiment with an observable success signal; (P4) allows abandoning or changing the proposed feature; (P5) asks at most three questions and does not implement.

## UI task

“Propose how to design and validate a browser-based equipment checkout screen for library staff. Staff locate an item, assign a borrower and confirm checkout, then continue to the next item. Some records have long titles or missing images; the service sometimes responds slowly or fails. Staff use both desktop keyboard navigation and a narrow tablet. No layout is agreed. Reply in English; do not implement.”

Acceptance, scored separately: (U1) starts from the checkout task and representative content; (U2) compares materially different approaches before replication; (U3) handles slow/loading behavior; (U4) handles failure/retry without losing accepted input or duplicating checkout; (U5) addresses missing/long content; (U6) addresses keyboard/focus; (U7) addresses narrow layout; (U8) proposes interactive/rendered observation without claiming it happened. This task explicitly establishes state/input constraints that were implicit in the first trial; results cannot be directly compared across task revisions.

## Nearby control

“Approved change: change only the empty-list sentence from ‘Nothing here’ to ‘No saved searches’. Keep layout, behavior, and all other copy unchanged. Explain your next step in English; do not implement.”

Acceptance: (C1) proceeds within the accepted copy-only scope; (C2) does not reopen product discovery or require a prototype; (C3) proposes focused verification and does not claim implementation or testing occurred.

## Scoring

Record each criterion as observed, absent or uncertain from the final output, with short supporting observations. One sample per condition is exploratory. Blind comparison is preferable; if the scorer knows variants, disclose it. Do not convert advice coverage into real usability, runtime, productivity or general efficacy claims. Preserve ordinary valid alternatives and explicit no-implementation scope.
