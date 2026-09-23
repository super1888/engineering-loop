# Short-prompt specialist routing trial, 2026-09-23

This local trial asked whether a short order-creation request could select the right project skills while retaining useful regression tests. Two tasks were used: a backend/form change and a backend-only change that explicitly left the form alone. The fixture, user task text, public tests and independent acceptance were held constant within each task. Each condition started in a separate synthetic Git workspace and used a fresh, sequential Codex CLI invocation.

| Variant | Difference from the same fixture |
|---|---|
| A | Minimal project `AGENTS.md`; engineering-loop and project skills available for discovery. |
| B | A plus one `AGENTS.md` rule to select skills by affected files, read only the matching skills, and use both across the API/form boundary. |
| C | B plus one focused regression instruction in each specialist skill, limited to changed behavior boundaries not already covered. |

The exact rules, normalized prompts and source hashes are in [inputs.json](inputs.json). The CLI was version 0.146.1 on Windows, using the account default model because the earlier explicit `gpt-6-sol` selection was unavailable to this CLI account. JSON events did not identify the default model. Runs were ephemeral, ignored user configuration, used `approval_policy="never"` and `danger-full-access`, and were confined by instructions to disposable workspaces. They did not delegate. The evaluator remained outside those workspaces; this was procedural separation, not a process sandbox.

| Task | A | B | C |
|---|---|---|---|
| Full order creation | Read engineering-loop, backend and form skills; backend/form oracle passed; added tests in both existing files. | Read backend and form skills; backend/form oracle passed; added no persistent tests. | Read backend and form skills; backend/form oracle passed; added one focused test in each existing file. |
| Backend only | Read engineering-loop and backend skills; backend oracle passed; added a backend test; form unchanged. | Read backend skill; backend oracle passed; no persistent test; form unchanged. | Read backend skill; backend oracle passed; added one backend test; form unchanged. |

All applicable public tests passed after the runs. In the backend-only task, the form oracle fails against the intentionally untouched `NotImplementedError` stub; that failure is expected, not a task failure. C's full-task tests cover invalid local quantity without an API call and rejected backend input without consuming an ID. Its backend-only test covers the rejected-input ID boundary. Patches and final messages are retained here. The independent oracle was validated against the incomplete fixture and a known valid implementation before these runs; [test_routing_oracle.py](../../../tests/test_routing_oracle.py) records those checks.

The recorded CLI input/output token counts were 343,075/4,671 (full A), 197,385/2,760 (full B), 153,492/2,741 (full C), 206,519/3,125 (backend A), 154,254/2,317 (backend B), and 136,727/2,253 (backend C). Cached input counts are in [outcomes.json](outcomes.json). These are observed usage counts, not a controlled price or wall-time comparison; stochastic runs and differing tool paths can explain part of the variation. Completed-command failure counts include exploratory commands and public tests run against the original stubs, not final acceptance failures.

Decision: for this synthetic project, keep the routing rule short and put the focused regression requirement in the specialist skills. B preserved accepted behavior and file scope but lost durable tests; C recovered those tests without adding a role-heavy user prompt or editing the excluded form. A also left tests, so the trial does not prove C is universally better than the minimal baseline. It does not test actual multi-agent delegation, HR-project conventions, comment preservation, constant placement, or human review effort. A held-out real-project case and repeated runs are needed before generalizing the output-quality or cost claim.
