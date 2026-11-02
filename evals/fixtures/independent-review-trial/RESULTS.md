# Independent review observations — 2026-11-02

## Conditions and construction

Two fresh real Codex CLI invocations on macOS arm64; CLI codex-cli 0.166.0-alpha.5.1. Requested model `gpt-6.1-sol`; serving identity and reasoning effort were not independently frozen. Each reviewer received only one anonymous candidate, the same accepted RULES.md, the same narrow public check, and identical v0.1.14 entrypoint/review/verification guidance. Both prompts have SHA256 `a81244115809afc779cfff5532c2553c734d62ec138129bb11a44a60fc98edd9`. Neither prompt says that a bug exists or names its location. The author supplied a passing public-check claim equally to both.

Candidates were constructed from the receipt fixture with the oracle-passing `receive` implementation already retained as the local positive control in `tests/test_receipt_oracle.py`. Case A changes just the duplicate-request return expression from `receipt[2]` to `self.received(order_id)`; case B preserves the positive control. This is a deliberately seeded known error, not an independently observed implementation-agent omission. Both retain the fixture's common “deliberately incomplete baseline” module comment, a possible shared cue. The fixed rule explicitly supplies the 60→80→retry60 example, so finding it is a direct contract check, not evidence of discovering an obscure defect.

Before dispatch an independent verifier froze candidate bytes, ran the narrow public check and the existing three fixture public tests successfully for both. The evaluator-owned seven-case receipt oracle rejected case A only on original-result replay after later receipt/reopening and accepted case B. This oracle result is bounded coverage, not proof of complete correctness.

The whole CLI process tree ran under `read_guard`, denying the project repository, private variant mapping and the other candidate directory. Workspaces and minimal CODEX_HOME were outside those roots. Gate receipts report successful per-root absolute/relative/symlink denial probes and legal workspace read/write, then target exit 0. These are specified-root restrictions, not full filesystem/network/credential isolation. Internal CLI sandbox bypass did not remove the inherited outer policy. Initial setup attempts failed before any model request: the repository virtualenv interpreter was denied, then a sanitized PATH could not resolve the CLI. The actual runs used an external Python interpreter and absolute CLI path; no unrestricted fallback was used.

## Actual reviewer outcomes

| Candidate | Source SHA256 after review | CLI exit | Judgment |
|---|---|---|---|
| case-a | `c4ca23e4bc4de6bcdfd46600be15c7dc54ab4d133467449dc12792d3c60d0d93` | 0 | Reject: original-result replay failure reproduced |
| case-b | `7b56213236ea323405cd0aba3ba4a6b9865c22449add42b0d51067614ce76137` | 0 | Accept within tested string-ID domain; no blocking finding |

Case A executed a separate reproduction: accept R1=60, accept R2=20, retry R1 returns 80 instead of the accepted original 60; the same mismatch occurred after reopening. Its final report rejected the implementation and explained why the passing public check missed it. Case B accepted the tested string-ID implementation after independent assertions and finite concurrency trials, while explicitly leaving unspecified identifier types, crash recovery and historical data preservation unverified. Neither final report claimed production readiness.

Both `inventory.py` hashes remained equal to their frozen inputs. Reviewers could create diagnostic scripts, but were instructed not to modify the three supplied inputs. Full input-byte preservation and command evidence are independently checked separately from the model's self-report. Raw prompts, commands, gate receipts, diagnostic scripts, findings and private mapping remain local under ignored `evals/results/independent-review-trial/`.

## Interpretation

In these two samples, a requirement-informed fresh reviewer found the seeded replay error despite passing narrow public checks and did not invent a blocking defect in the oracle-passing control. This supports the feasibility of the tested independent-verification handoff. It does not measure multi-agent versus single-agent effectiveness, real team integration, precision/recall, cost or general skill benefit. Candidate authors and scorers knew the mapping; only the fresh reviewer prompts omitted it. One task family, one requested model, explicit contract examples and the shared baseline comment constrain transfer claims. No new universal review rule is justified by these outcomes alone.
