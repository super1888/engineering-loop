# Demonstrated project lessons

Keep this small. Business/stack defects belong with their executable safeguards; a local incident is not automatically a generic skill rule.

## Saved instructions overwritten by presentation defaults (2026-10-01; not behavior-evaluated)

- **Trigger and environment:** In a Windows/Vue/TypeScript application, an already rendered media artifact became stale when the user clicked Next without editing its instructions. The page shared a payload constructor between rendering and stage navigation.
- **Cause and missed check:** The constructor always wrote the current UI language's defaults over four saved instructions. The backend correctly rejected the changed source digest; compilation and new-project checks did not exercise a saved custom instruction or a language change. Disabling invalidation would have hidden a real source change.
- **Correction and evidence:** The shared constructor preserves saved strings, including explicit empty strings, and fills only absent fields. Local regression cases covered retained instructions, another language's defaults and missing fields. After deployment, actual navigation retained the same artifact digest and report. Restoring the original test settings also recovered that artifact without rerendering. These are application observations, not measured skill behavior.
- **Applicability, cost and controls:** Useful when presentation defaults feed persisted inputs tied to downstream evidence. Inspect all callers of the shared constructor; do not impose a new state layer. Explicit user edits must still change the source and invalidate dependent evidence, and a new object must still receive its defaults.
- **Owner and review:** Maintainers own the synthetic `presentation-defaults-saved-evidence` case. It remains unrun; no general skill paragraph or transferable benefit is claimed from this incident. Evaluate the preserved-input and legitimate-edit controls before promotion; retire the candidate if current implementation and verification guidance already catches it reliably.

## Cross-host script transport candidate (2026-10-01; not behavior-evaluated)

- **Trigger and environment:** A Windows/CPython3.12.3 maintenance helper sent an LF Bash script to Linux through a text-mode subprocess. Receiver-side syntax checking rejected a carriage return after `case ... in`; inspecting the local string alone showed valid LF content.
- **Cause and evidence:** The text-mode stdin transport changed line endings. The same script sent as explicit UTF-8 bytes passed receiver-side syntax validation and a read-only runtime check. Invalid operation and release-identity controls still failed before mutation. This is transport evidence, not a model evaluation or proof that a maintenance action was executed.
- **Correction and candidate:** The local helper preserves script bytes and validates the intended receiver before any maintenance mutation. No generic workflow paragraph was added from this one incident. Expected benefit is distinguishing transport damage from invalid source or a broken remote runtime; cost is inspecting that boundary when the evidence conflicts.
- **Counterexample and owner:** Ordinary text payloads whose contract tolerates native newline conversion, and an already byte-preserving transport, should remain unchanged. Maintainers own the synthetic `cross-host-script-transport` case. It is unrun; evaluate it and those controls before promoting guidance or claiming transferable benefit. Retire the candidate if existing verification guidance already handles the boundary reliably.

## Read-only delegation candidate (2026-10-01; not behavior-evaluated)

- **Trigger:** A cost estimate intended to be read-only reused an archive inspection that first refreshed a run. The downstream refresh could reconcile status and register a resource; a reference-resolution query also wrote registrations. This was found by tracing implementation before release on Windows with Java21.
- **Correction and evidence:** The application reused its owner-checked archive projection through a separate read boundary. A local regression checked the projection, ownership rejection, output mismatch and absence of lifecycle/registration calls; existing execution inspection kept its refresh behavior. This is application evidence, not an engineering-loop model evaluation.
- **Candidate:** `implementation.md` makes downstream side effects explicit only when the accepted flow promises read-only behavior. Expected benefit is avoiding an accidental write behind a query name; cost is inspecting that boundary. Approved reconciliation and registration are the counterexample, and must remain available.
- **Evaluation and owner:** Maintainers own the synthetic `read-only-delegation-side-effects` case in `evals/cases.json`. It has not been run. Evaluate that case and its execution control before claiming transferable benefit; retire the added guidance if it merely repeats effective project checks without improving behavior.

## SQLite transaction completion does not release the connection

- **Trigger and evidence:** During the 2026-09-21 trial, the independent oracle's temporary database cleanup failed on Windows with file-in-use errors for both candidate implementations.
- **Root cause:** The evaluator used an SQLite connection as a transaction context and assumed that leaving it also closed the connection. Its inspection/trigger connections could remain open until collection.
- **Why checks missed it:** Distribution checks did not execute the oracle. The incomplete receipt fixture failed before many inspection paths, so its initial failures did not establish that the evaluator cleaned up a successful run correctly.
- **Correction:** The evaluator explicitly closes the connections it creates; transaction contexts remain around its writes. Candidate implementations and accepted business assertions were not changed to hide the failure.
- **Safeguard:** `python -m unittest discover -s tests -p test_receipt_oracle.py -v` verifies that receipt inspection releases its connection. It failed before the fix and passed after it. The normal root unittest command in existing CI includes this test.
- **Applicability:** Helpers that own SQLite connections and disposable database files, especially where open handles prevent cleanup. Do not apply this as a ban on transaction contexts or manually close a borrowed/shared application connection.
- **Owner and transfer:** Maintainers changing the oracle own this check. For another Python/SQLite project, first inspect connection ownership, then adapt and run the regression there. No second-project adoption has been demonstrated yet.
- **Review condition:** Revisit if the evaluator's persistence or ownership model changes. Remove or replace the check if the failure boundary no longer exists; do not retain an irrelevant rule solely as history.
