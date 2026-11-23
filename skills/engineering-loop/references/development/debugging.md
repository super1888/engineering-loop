# Diagnosis method

**ID:** `dev.method.debugging` · **Status:** available method, adapted from public debugging practice. Use for a defect or regression whose cause is not already demonstrated. A cause visible in the error needs only its fix and regression check.

## 1. Build the loop before theorising

Produce one command, already run once, that:

- goes red on the reported symptom itself, not on "it crashed" or a nearby failure;
- gives the same verdict on every run;
- finishes in seconds and runs unattended.

Try in this order: a failing test at the seam that reaches the defect, an HTTP script against a local server, a command-line run on a fixture compared with known-good output, a headless browser script, a replay of a captured request or event, a minimal harness around the one code path. When the defect appeared between two known states, automate the check so the range can be bisected.

For an intermittent defect, raise the reproduction rate (repeat, add load, narrow the timing window) until it is high enough to work against.

Reading code to form a theory before this command exists is the failure this method prevents. If no loop can be built, stop, list what was tried and ask for the reproducing environment, a captured artifact or permission to instrument. Redact secrets from every command and output shown.

## 2. Minimise

Remove inputs, callers, configuration, data and steps one at a time, rerunning after each cut. Stop when every remaining element is load-bearing: removing any one turns the loop green.

## 3. Rank hypotheses

Write three to five before testing any. Each states a prediction: if this is the cause, changing X removes the symptom. One without a prediction is discarded or sharpened. Show the ranked list; the developer may reorder it at once. Test one variable at a time.

## 4. Locate

- Compare with a working example in the same codebase and list every difference, including the ones that seem irrelevant.
- When several components are chained, record what enters and leaves each boundary, run once, and read where the value first goes wrong. Investigate that component only.
- Follow a bad value back up the callers to where it originated and fix it there, not where it surfaced.
- Prefer a breakpoint to many logs. Tag every temporary log with one unique prefix so cleanup is a single search.
- For slowness, measure a baseline (timing harness, profiler, query plan), then bisect. Logs rarely locate a performance regression.

## 5. Fix

- Write the regression test before the fix, at a seam where the real pattern occurs. If only a shallower seam exists, a test there gives false confidence: record the missing seam as a finding instead.
- Apply one change. Do not stack a second fix on a failed one.
- After three failed fixes, stop patching. Re-examine the assumptions and the design with the evidence gathered and raise it with the developer. The count triggers the review; it does not prove the architecture wrong, as the [shared core](core.md) notes.

## 6. Clean up

- Rerun the original, unminimised scenario.
- Search for the log prefix and remove every hit. Delete throwaway harnesses.
- State the confirmed cause in the commit or [delivery record](delivery.md).

Write the regression test by the [testing method](testing.md).
