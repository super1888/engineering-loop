# Existing-client release observations — 2026-11-02

## Construction and conditions

A small loopback HTTP fixture serves two desktop pages and version-specific lazy modules. Its active/retained configuration is read on each request, with no-store responses. Before model dispatch, an independent browser control reproduced a health-200/fresh-v2 success while an already-open v1 page failed its first delayed module request after an unretained switch. A retained-v1 positive control preserved that page's unsaved draft and loaded its details. This is a synthetic release boundary, not a production deployment.

One real Codex CLI invocation used CLI `0.166.0-alpha.5.1`, requested model `gpt-6.1-sol`, and the v0.1.18 entrypoint/release guide. Serving identity and reasoning effort were not independently frozen. Prompt SHA256: `96ebf8cf0278d61addf2324c84e8d9869bfa6911d6d6317538be2fe902365d97`. It received the operator request and fixture files, not the evaluator's oracle or acceptance implementation. The whole process tree used the specified-directory read guard against the repository and private evaluator directory; this is not complete filesystem, network or credential isolation.

Two preliminary capability attempts ended before any model dispatch with native Node startup failures while launcher output streams were opened in the protected repository tree. Selecting the parent Node 24 alone did not resolve the second failure. A subsequent run with output streams outside that tree passed an actual guarded Playwright/Chrome launch-and-close probe, then dispatched the model under the unchanged deny policy. These setup observations do not establish a general Node-version diagnosis, timing benefit or a need to relax protection. Raw failed-attempt logs are retained locally.

## Model artifact

The CLI exited 0. Among the frozen application inputs, only `deployment.json` changed, to `{"active":"v2","retained":["v1"]}`. Service and page/module bytes remained unchanged. The model reported a local Chrome self-check and stopped its self-check server; this self-report is distinct from independent acceptance. No production change, publication or installation was authorized or performed.

Candidate service SHA256: `8e1f15054bc01a71d55b17318e672ecefb886e271b2ba678c0f500b9701b81ff`.
Candidate deployment SHA256: `7d355967e54ef27a03f8e2032083ac1e378d7c9644064e33fac22ec109cc118d`.
All source identities and the before/after application manifests remain in local records.

## Independent acceptance and limits

A separate evaluator ran the frozen candidate through real browser interactions in a disposable copy. All three checks passed: fresh v2 plus health, existing v1 draft/lazy continuity across cutover, and an explicit retained-asset rollback control. The candidate bytes were unchanged by that evaluator and v2 remained active in the submitted configuration.

The rollback control is evaluator-supplied: it explicitly retains v2 before switching active back to v1, then tests a newly opened v2 document whose lazy module has not yet been requested. This demonstrates the local retention mechanism, not that the model generated a complete rollback policy. The old-v1 positive path likewise starts with a document whose lazy import has not already failed. Recovery of a document that already failed an import is not covered by these frozen checks and is not claimed; no reload was used to discard its unsaved draft.

The scenario validates prevention of the sampled local existing-session breakage. It does not establish real CDN/browser-cache behavior, a retention lifetime, mobile compatibility, production rollback safety, native skill discovery or a causal skill advantage. Test processes were cleaned up. Raw prompts, source/config hashes, guard receipts, failed setup attempts and browser reports remain ignored/local under `evals/results/release-existing-clients/`.
