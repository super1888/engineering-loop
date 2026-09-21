# Findings

- Existing stage references already require independent acceptance, risk-based verification and local-first learning. Extend them without repeating a full lifecycle.
- Missing operational connection: project fact/check/owner mapping; business invariant capture; shared contract coordination; demonstrated transfer of lessons.
- cases.json is an unexecuted protocol. Distribution checks are not behavioral evidence.
- No fixture runner exists. Add a small standard-library receipt fixture and separate oracle, not a model orchestration platform.
- Compare two isolated same-input tasks once. A paired trial is diagnostic, not statistical evidence of benefit.

- Both candidates passed 13 local tests and 7 independent oracle tests; original requirements and tests were preserved. No skill advantage is established. The skill candidate updated existing WORK.md; the control did not.
- The copy trial modified only the requested label and passed the local structural check.
- First independent oracle runs exposed a real helper defect: transaction contexts did not close SQLite connections, causing Windows cleanup errors. Reproduced using a focused resource test, fixed with explicit closing, and reran both candidates and the faulty baseline without altering business assertions.
- The original faulty baseline still fails 14 assertions across 7 oracle methods. Details, sanitized logs, replayable patches and source hashes live in evals/results/2026-09-21-local/; docs/LESSONS.md records the narrowly applicable safeguard.
- Independent read-only review found no actionable standards/spec defects; runtime results are supported separately by command evidence.
