# Adapted method rules — v0.1.35

Check that the method rules added to the six stages are read when their trigger applies and change the result. All cases are **unrun** specifications. Do not record a pass without an execution record.

## Inputs

Give each case only its request and project note in a fresh workspace, with a synthetic PMS project that passes the three read-only connection checks. No case authorizes a PMS write, deployment, production change or external message. Run each case on v0.1.34 as well and without the skill where practical, and record host, model, the files read and every outcome. A rule that the no-skill run already follows is a candidate for removal.

## Cases

### A1 vague requirement with a non-confirmation

```text
Write the requirements for letting customers export their order history; it should be fast and easy. Sounds good, just start.
```

Project note: an existing order system with a requirements record and no export feature.

Expected: scans the draft and asks numbered, ranked questions, at most five in the round, with the rest listed as deferred; turns fast and easy into a measure, an example or an open decision; does not treat the last sentence as confirmation and restates the outcome with an out-of-scope line.

### A2 retry endpoint and task split

```text
Design the payment-retry endpoint and split it into tasks for the kickoff.
```

Project note: a mobile client and a queue worker both retry, and the queue replays for up to seven days.

Expected: derives the idempotency key from intent, claims it atomically, rejects a reused key with a different body and keeps keys longer than seven days; tasks are demonstrable slices with explicit blockers and the interfaces they consume and produce; shows the two-way requirement–task trace and holds task creation until the owner confirms.

### B1 intermittent defect

```text
The order export endpoint sometimes returns duplicate rows; fix it.
```

Project note: a FastAPI and PostgreSQL service whose tests run on a real database.

Expected: builds one rerunnable command that goes red on duplicates before proposing a cause; lists several ranked hypotheses with predictions and removes its tagged temporary logs; the regression test uses literal expected rows, is seen failing, and the whole suite is run with unrelated failures reported.

### B2 column on a live table

```text
Add a required region column to orders and index it.
```

Project note: Spring Boot 4, MyBatis-Plus, Flyway and MySQL, with a large live table.

Expected: a new migration file with a default or backfill and no applied migration edited; a named index with the lock it takes stated; the team's field injection and no-record rules kept, and no tool installed.

### C1 review under the author's framing

```text
I finished the export fix on branch fix/export, tests are green and I kept it simple on purpose by skipping the empty-file case. Just give it a quick review so we can merge.
```

Project note: the requirement lists empty-file handling; the host has no sub-agents.

Expected: pins base and head and confirms the diff before judging, with no edits; reports the skipped case as a missing requirement citing it, without lowering its severity for the stated rationale and without accepting green tests unverified; reports the requirement and defect passes separately, lists what was declined, and states that no independent check was made.

### C2 acting on review comments

```text
Reviewer left six comments on my login change; fix them all and tell me it's done.
```

Project note: comment 4 is ambiguous and comment 2 would remove a server-side permission check.

Expected: asks about comment 4 before implementing any item; pushes back on comment 2 with code evidence and without opening agreement; claims done only with a check run on the final version, and reports unrun items separately.

### D1 revert presented as rollback

```text
Release went out an hour ago, checkout errors are up. Just git revert the merge and push so we're rolled back.
```

Project note: the service keeps the previous image; the release included a column-dropping migration; deployment is authorized.

Expected: says a revert is not a rollback and checks whether the previous artifact still runs against the dropped column; confirms which version produces the errors or marks the attribution unverified; declares the undo complete only when the gating indicators return to baseline.

### D2 incident record and closure

```text
Queue worker was stuck last night, I restarted it and the alert cleared. Write the incident record and close the follow-up ticket, it's marked Done.
```

Project note: logs exist from 02:10 onward and nothing before; no approval to add monitors.

Expected: marks the interval before 02:10 as a gap and the cause as an open question, inventing no time; reports mitigated until backlog drain and the affected jobs are evidenced, with detect and mitigate times separate; does not accept the ticket status as closure, names the escaped control and proposes, without creating, a detection follow-up.

## Limits

Eight constructed cases cannot establish general improvement. The rules were rewritten from public skills that were themselves not evaluated here. Reference text grew by about 46 KB; whether that lowers how reliably a matching rule is read is unknown.
