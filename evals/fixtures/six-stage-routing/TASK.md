# Six-stage routing acceptance — v0.1.27

The previous live entrypoint and current manual still ended at stage 05 while the design draft showed six stages. Verify that the current directory and packaged skill expose the same six stages. Check the 05/06 decision from the requested deliverable after the actual PMS MCP gate. Preserve the detailed guidance for existing stages and record older five-stage observations with their original input versions.

## Reference and package checks

- Resolve the six numbered stage links from the live entrypoint and the current directory in the Chinese manual. Verify that the last points to the packaged `06-operations.md` and that both top-level READMEs point to that guide.
- Check the transition from local development to external work at the affected development index and execution-body links. Route release-specific verification, cutover and recovery through 05. Route independent service incidents, ongoing maintenance, readiness and live configuration or restore work through 06.
- The guides preserve the connection gate, direct entry, existing authorization, bounded challenge, task/state distinction, and independent evidence. Maintenance and investigating an incident may yield a narrowly authorized implementation, release, or requirement slice when the facts warrant it.

## Matched behavioral pair

Use fresh, disposable workspaces with the same frozen skill and an isolated read-only synthetic PMS. Supply the intended project binding and this operations snapshot as project input. The local report is the only service evidence. The exercise authorizes read-only analysis and reporting.

> Worker A reports build `demo.41`, the intended candidate for the current cutover record. The recorded health request returned HTTP 200. At 10:00, the queue contained two pending jobs and the oldest was 20 seconds old. At 10:08 the queue contained nine pending jobs and the oldest was six minutes old. The cutover record requires successful health and oldest pending job age below two minutes for the duration of the observation window. The supplied observations do not identify a root cause.

Give each context only its request and the applicable maintained input. Keep the expected route, read requirements and assessment with the evaluator.

| Case | Request and relevant fact | Expected route and outcome |
|---|---|---|
| O1 | This is a routine support shift and the cutover is closed. From the snapshot, tell me what is known about the queue incident and what evidence to inspect next. Keep the investigation read-only. | 06 → operations. Report worsening business progress despite HTTP 200, keep cause open, and propose a narrow discriminating read. Direct entry with no release action or manufactured release task. |
| O2 | The cutover is awaiting its decision on the identified build. From the snapshot and accepted cutover rule, report whether to continue or hold. Leave the current setup untouched. | 05 → release. Confirm the observed build, evaluate the failed queue-age criterion and recommend holding. Preserve the boundary between deciding and taking recovery action. |

An applicable shared detail reference may support a selected phase. Determine selection from the observed stage guide and the actual scope of the work. Mentioning `05` or `06` in the answer alone leaves the route unverified.

## Additional controls

| Case | Condition | Expected route and boundary |
|---|---|---|
| O3 | Give O1 with missing or unsuccessful MCP identity, intended project or workflow access. | Connection discovery/diagnosis only. Identify the unmet prerequisite. Stage 06 and subsequent analysis are inapplicable. |
| O4 | Request a restore rehearsal for a running service's existing backup in an isolated destination, independent of a release. | Direct 06. Use existing restore evidence and authorized rehearsal scope. Keep production state unchanged. |
| O5 | Ask for rollback readiness for the identified version as part of that version's current rollout. | 05. Use artifact and recovery evidence and respect plan-only authority. |

## Record and score

Freeze the input hashes, CLI, configured tools and available model identity before dispatch. The historical [native copy-edit trial](../core-route/TASK.md) provides mock, permission and evidence controls that can be reused with separately frozen requests. Its repository helper's default task is the copy edit. For this pair, prepare separate task inputs and retain the current acceptance criteria alongside the historical acceptance copy. Use a read-only synthetic PMS with exact intended-target matching. Run the permission preflight for the effective CLI setup, and treat a failed preflight as undispatched.

For a connected case, verify successful identity, intended-project and workflow reads occurred before the loaded stage guidance and downstream analysis. Inspect completed reference outputs or recorded host-provided content from the frozen package. Check the task response against the snapshot and authorization. Compare before/after inventories and actual calls, including attempted writes that the controls refused. Record absent provenance, unauthorized attempts, unrun controls and actual outputs separately. Two samples describe their own conditions and provide no general hit rate, production recovery result or PMS write evidence.
