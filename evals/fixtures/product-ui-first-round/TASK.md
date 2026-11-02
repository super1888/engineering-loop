# First-round product/UI matched trial

Run in fresh isolated contexts with the same model/configuration, no personal AGENTS, no tools, and no implementation authorization. Supply either the f12204d3549848a9d585ec0a150dd3d931150cee (v0.1.12) entrypoint plus requirements reference, or the current entrypoint plus requirements references (product/control); UI additionally supplies the matching verification reference to both variants and the new UI reference to the enhanced variant. Retain raw prompts, variant hashes and output locally. This probes advice only, not rendered UI quality.

## Product task

“We want an internal employee leaderboard to improve productivity. Managers think ranking people by completed tickets will help, but we have not interviewed employees or measured the problem. Suggest the next step, with at most three questions. Do not implement.”

## Nearby control

“Approved change: replace the button label ‘Submit’ with ‘Save’ on the settings page. No behavior or layout change. Say how you will proceed, do not implement.”

## UI task

“Design a mobile-friendly approvals screen for supervisors processing 30 requests daily. Each request has person, amount, reason and attachments. Some requests have missing evidence. We have no agreed layout. Propose a bounded way to choose and validate a design; do not implement.”

## Evaluator acceptance (do not include in model prompt)

Product: challenges whether ticket counts represent desired outcomes; investigates affected people/current alternatives or measurable loss; proposes a bounded hypothesis test with observable success and allows abandoning the feature; stays within three questions and does not implement. Control: proceeds with the accepted label change and focused validation without reopening product discovery. UI: derives layout from processing task and representative content; compares meaningful alternatives before expansion; covers missing/loading/error states and mobile/keyboard concerns; proposes actual interactive/rendered validation without claiming it was performed.

Score each criterion as observed, absent or uncertain with an output excerpt. Do not infer real usability, deployment readiness or general benefit from advice quality. One run per condition is exploratory; repeat with held-out tasks before claiming improvement.
