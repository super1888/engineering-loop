# Desktop implementation trial — 2026-11-02

## Initial frozen task and actual implementation

Both CLI runs used a separate CODEX_HOME but bypassed the filesystem sandbox: workspace-only restrictions were prompt instructions, not enforced filesystem isolation. The initial command log contains no oracle references; the second explicitly discovered/read and ran the repository oracle. It must not be treated as hidden acceptance or independent discovery. No credentials or configuration contents are retained in this report.

Host: macOS arm64. Reasoning effort was not fixed or recorded; the exact CLI build was not retained in the per-run receipt. The model name below is the requested selection, not an independently verified serving identity.

A fresh local Codex CLI invocation requested `gpt-6.1-sol`, supplying v0.1.14 entrypoint/UI guidance and the task's user-request portion, not its independent acceptance list. The disposable workspace contained the two intentionally incomplete fixture files. CLI exit was 0; only `app.js` changed. No commit, publication or mobile breakpoint was introduced. The candidate ran syntax and simulated-DOM checks and explicitly left rendered behavior unverified. Its process did not inherit the Playwright module path; browser tooling was available on the host and was subsequently used by a separate verifier. This is one enhanced-version implementation sample, not a baseline/enhanced comparison.

Initial prompt SHA256: `8e2023cf0bbd68f73df3d0c2e40a654d25c4aad7477eb20353bb3820c88fbbb9`.
Initial candidate `app.js` SHA256: `bbfaf43075e3f8c548213995cb8eb9c21b695e1ceb4969f45c5cde19dfa66040`.
Unchanged `index.html` SHA256: `2571cf0f34dd567b3e4f44ee7c73ab83f90a336d52352d51686cec0d427b45a0`.

## Independent browser observations

Chrome 156.0.8078.80 exercised desktop widths 1280 and 1024. The independent oracle reported 6/8 scenarios passed: filtered item details, delayed/failed refresh followed by successful retry with fresh data, and keyboard/desktop layout checks passed at both widths. Each failure concerned an explicit empty-state text assertion. Diagnostic interactions confirmed zero rows for no match and all three rows restored on clearing, with no page errors.

The original task's “visible empty result” did not explicitly require no-results wording or count semantics. An independent review therefore judged these two oracle assertions stronger than the accepted contract. The original 6/8 result is retained; it is not evidence of a confirmed implementation defect. No claim of full visual quality, mobile support or reliable skill benefit follows from the passing interaction samples. Screenshots and raw browser reports remain local.

## Post-observation clarification

A second fresh implementation was authorized after explicitly clarifying no-results feedback and filtered-count meaning in TASK.md. It starts from the initial candidate, so it is a known-answer repair, not independent discovery or a new matched efficacy comparison. The second CLI exited 0 and changed `app.js` and `index.html`. It discovered the host Playwright/Chrome setup and ran the now-visible oracle itself; that self-check is not the independent verifier result.

Second prompt SHA256: `fcfcd7668856fbdc7935d2490009bf27ba0b3bdbe09dcbd1f5ea610bed13e3c2`.
Second candidate `app.js`: `00c12f4c8bfeacb5be0347448d2e48b03398b555de150fdc88d6980234387ba1`; `index.html`: `1068c67f21a3ccd004362c0a2e8c22b7f6d1ee68d5645746bfee2fec6686e8aa`.

A separate verifier reran the unchanged oracle against the frozen second candidate in Chrome 156: exit 0, 8/8 scenarios passed at the two desktop widths, including explicit empty feedback and clear restoration. API responses were routed locally, not a real backend. Independent screenshots and reports remain in ignored `refined-screenshots/` and `refined-browser.json`. These results establish the checked local behaviors after an explicit known correction; they do not prove automatic skill routing, hidden-test generalization, mobile quality, or a net benefit over the base model.

The screenshots named `empty-and-clear` capture the post-clear state (three restored rows), not the no-match state. They support restoration layout only. A separate `1280-empty-state.png` was subsequently captured and inspected by the main agent and verifier: “0 matching items” and explicit no-match/clear-filter feedback are visible, with no stale rows. This is evidence for that static desktop state, not general visual quality.
