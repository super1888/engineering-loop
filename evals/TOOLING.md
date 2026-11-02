# Evaluation and distribution maintenance corrections — 2026-11-02

These are reproduced tool defects and mechanism controls, not new model trials or proof of improved model behavior. Existing trial reports retain their historical scores; passing an older oracle establishes only its then-covered paths.

## Receipt output before guarded work

The previous wrapper could run the target and only afterward discover that the receipt parent was a regular file. It also followed an already-present dangling receipt symlink after resolving the path. Synthetic local reproductions observed target side effects without a usable receipt, or creation of the symlink destination.

The wrapper now rejects an existing lexical leaf before resolution and exclusively reserves/initializes the receipt before probe or target dispatch. States distinguish prepared, running, completed and failed; probe failure records no target dispatch. Tests retain legitimate parent-directory symlinks and exact target exit codes. This is not a guarantee against every later disk fault, adversarial mutation or crash. See [receipt controls](../tests/test_read_guard.py).

## Failed refresh retains the full inventory

A candidate that kept only the currently filtered rows after HTTP 503 previously passed all eight frontend oracle scenarios, yet clearing the filter showed one of the three original items. The same accepted contract already required retaining existing data.

The oracle now captures all original rows and details before refresh, clears the filter after failure and compares the complete unordered snapshot, then restores the filter and continues retry checks. Negative controls lose hidden rows or corrupt quantity/description; valid retry labels and stable quantity formatting remain accepted. No new business rule or fixed row order/number format is imposed. See [browser controls](../tests/test_frontend_target_oracle.py). Historical eight-scenario reports are not retroactively rescored by this correction.

A retained [guarded implementation candidate](fixtures/read-guard-trial/RESULTS.md) was separately rerun with the corrected oracle: exit 0, eight of eight desktop scenarios passed, including the expanded inventory check. Its source identities remained `c4f40d3191adb1f95be3d84049db20308913582c413d867a213ff0920c3df41f` (`app.js`) and `f2b2917d4c047aec7207339c0ab313fde390ceb6ce6510f824bcc4e59c95347a` (`index.html`). The new raw result is retained locally as `maintenance-full-inventory.json`; this is an artifact recheck, not another model invocation or a rewrite of the historical score.

## Local environment files stay local

A root `.venv` dependency README containing an upstream-only relative link, or a non-project JSON file, previously caused project distribution checks to fail. Only root-local `.venv` content is now excluded, matching the existing ignore convention. Project documents and nested fixture/payload directories with that name remain checked. This changes validation scope, not traversal performance. See [distribution controls](../tests/test_distribution.py).

## Preserve unrelated path prefixes

A summary containing another absolute path formed as `/archive` plus a known trial root was previously changed inside that unrelated path. The normalizer now checks a left boundary as well as the existing sibling suffix boundary. Controls preserve common embedded prefixes while retaining standalone roots, punctuation and aliases. This is scoped text normalization, not an exhaustive parser or confidentiality guarantee. See [path controls](../tests/test_trial_paths.py).
