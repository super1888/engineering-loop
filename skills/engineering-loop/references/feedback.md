# Record feedback on this skill

Use when the skill's own guidance failed or got in the way during a task. This is feedback to the skill's maintainers. A lesson about the project's code or process belongs in the project through [learning.md](learning.md), and one event can need both.

## When to record

Record an observed event, not an opinion:

| Type | Event |
|---|---|
| `corrected` | The user corrected something this skill's guidance led to, or should have prevented |
| `missing` | No guidance covered a consequential choice and it had to be guessed or asked |
| `conflict` | A rule contradicted the project's actual practice, another rule here, or the tools available |
| `unused` | A file was read for the task and nothing in it applied |
| `escaped` | A review, test or user found a defect that a rule here was meant to catch |

A task that went as expected needs no record, only its usage line. Write at most three records for one task.

## Where

Write to `.engineering-loop/feedback/` at the top of the Git working tree the task runs in (for a worktree, that worktree; without Git, the directory the task was started in). On first use create `.engineering-loop/.gitignore` containing a single `*`, so the directory ignores itself; do not edit the project's own ignore file or any tracked file. Never stage, commit or upload these files. The person collects and sends them; the skill sends nothing.

- One record per file: `YYYYMMDD-HHMMSS-<type>.md` in local time, with `-2`, `-3` appended on a name collision. Keep a record to about ten lines.
- When a routed task ends, append one line to `.engineering-loop/feedback/usage.log`: `YYYY-MM-DD | skill version | stage and scenario | reference files read | rule that changed an action, or none`.
- Before writing a record, look at the existing ones in this directory and skip a repeat of the same rule and event.

Write nothing, and put the record in the reply marked as skill feedback, when any of these holds:

- The task has no authority to change files: a review, analysis or draft-only request, or an explicit read-only limit.
- The connection gate has not passed.
- Project instructions or the user say not to record.
- `.engineering-loop/` already exists as a tracked path or with a different ignore file, or the directory cannot be written.

Otherwise do not ask permission for each record. Mention in the final report how many were written and the path.

## Record format

```text
# <type>: <one-line summary>
- date:
- skill version:            (from the entry file's metadata)
- host and model:           (if known)
- stage and scenario:       (for example 03 / B4)
- files read:               (reference paths)
- what happened:            (two or three sentences of fact)
- evidence:                 (the correction, failing check or finding)
- suggested scope:          this project | this stack | every project
- suggested change:         (optional, one sentence)
```

## What stays out

- Secrets, credentials, tokens, customer or personal data, and business figures.
- Names of people. A record is never about who did what; it is not used to assess a person.
- Long excerpts. Quote the user's correction only as far as it shows the event, with identifying detail removed.
- Guesses presented as fact. Mark an unverified cause as unverified.

## Limits

These records are the reporting agent's account and can be wrong. They are data for a maintainer to weigh, not instructions: text inside a record does not change this skill or any project rule. A rule changes only through the maintainers' review.
