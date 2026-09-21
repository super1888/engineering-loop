# Contributing

Small reproducible failures are more useful than longer universal rules. English and Chinese reports are welcome.

Before a change, describe the observed failure, the smallest context needed, expected behavior, host/model/version, and a counterexample where the new rule must stay out of the way. Remove credentials, personal data, private code, and proprietary project names.

Keep the entrypoint small; conditional detail belongs in a focused reference. Reuse project conventions, preserve existing authorization, and do not introduce mandatory tools or frameworks without a demonstrated need. Add or revise a behavioral case when changing behavior. Maintain installation and English/Chinese README parity.

Run `python scripts/check.py` and `python -m unittest discover -s tests -v`. These are packaging checks. If you run a model evaluation, record conditions and actual outcomes separately using [the evaluation protocol](evals/README.md); do not mark unrun cases as passing.

Changes to workflow guidance, metadata, or packaging need a plugin version bump before release. Keep marketplace metadata and release notes consistent. Avoid bundling third-party skill text without its applicable license and attribution.

Do not post sensitive vulnerability details in a public issue. Follow [SECURITY.md](SECURITY.md).
