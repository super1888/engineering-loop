# Tests that can fail for the right reason

**ID:** `dev.method.testing` · **Status:** available method, adapted from public test-first practice. Project test tooling and the team stack rules win where they differ.

Use when a test is written or changed in the current slice. It does not make a test mandatory where the [shared core](core.md) accepts a consistency check, and it adds no test framework.

## Before writing a test

- List the public seams under test: the interfaces where behavior is observed without reaching inside. Give each a line on what it catches and what it misses. Raise it with the developer only when the choice of seam is consequential and the accepted design does not fix it.
- Name the production change that would make the test fail. If no change can be named, redesign the test around an observable behavior. If only a deliberate decision could fail it (a constant, exact wording, private structure), test the behavior that depends on the decision instead.
- Take the expected value from a literal, a hand-checked fixture or the contract. A value computed by the code under test, its helpers or a builder shared with the setup passes whatever the code does.

## The loop

- Work in vertical slices: one test, the code that passes it, then the next test. Writing every test first fixes their shape before the implementation has taught anything.
- Where the slice is built test-first, run the new test before the code exists and read the failure. It must fail on the assertion for the missing behavior. An import error or a typo is not that failure, and an immediate pass means it exercises existing behavior.
- When a red result was forced by editing code or a fixture, confirm the edit actually took effect before trusting it.

## Doubles

- Replace only a system boundary: an external service, time, randomness, sometimes the file system. Keep the module's own collaborators real. A stack rule that requires a real database stands.
- Before replacing a method, list its side effects and keep real the ones the test depends on.
- Never assert on the double itself. An assertion that fails only when the double is removed checks nothing about the product.
- A fake response carries every documented field of the real one, not just the fields this test reads.
- Give each branch (success, error, malformed) its own fixture, so the wrong branch cannot satisfy the expectation.
- A method called only from tests belongs in test utilities, not on the production class.
- Wait on the condition, with a timeout and a clear message, not on a fixed delay. A fixed delay is valid only for behavior that is itself timed, with the reason written beside it.

## Before finishing

- Mutate the changed code in your head: a wrong constant or argument, the wrong branch, a missing state change or side effect, an empty return, missing validation for empty, malformed or unauthorized input. Each realistic mutation should fail at least one test. One that survives marks unprotected behavior or a tautological test.
- Run the project's whole suite, or its documented targeted command where the whole suite is impractical, and say which. Do not stop at the file you touched. Report every failure by name, including those the change did not cause.

## Signs of a test that cannot fail

- Setup and assertion share one object, or the expectation sits behind a loop or helper.
- It can fail only by crashing or by a missing selector.
- It searches source text, or asserts that a constant equals itself.
- It would still pass if only the framework remained.
- Mock setup is more than half of the test.

Evidence boundaries and independent acceptance stay with [verification](../verification.md).
