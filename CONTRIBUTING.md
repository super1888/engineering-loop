# Contributing

Small reproducible failures are more useful than longer universal rules. English and Chinese reports are welcome.

Before a change, describe the observed failure, the smallest context needed, expected behavior, host/model/version, and a counterexample where the new rule must stay out of the way. Remove credentials, personal data, private code, and proprietary project names.

Keep the entrypoint small; conditional detail belongs in a focused reference. Reuse project conventions, preserve existing authorization, and do not introduce mandatory tools or frameworks without a demonstrated need. Add or revise a behavioral case when changing behavior. Maintain installation and English/Chinese README parity.

Use Python 3.12 to match CI (the repository tools require Python 3.10+). Create a local virtual environment with `python3.12 -m venv .venv` and activate it with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in PowerShell. If using uv, `uv venv --python 3.12 .venv` can provision the interpreter. Node.js 22 must also be on PATH for the JavaScript evaluation fixtures. No third-party Python packages are required for these repository checks. The virtual environment stays local and is ignored by Git. On macOS, the recorder tests currently require a canonical temporary path: after activation, run `export TMPDIR="$(python -c 'import tempfile; from pathlib import Path; print(Path(tempfile.gettempdir()).resolve())')"` if the system temporary directory uses a symlink alias. This avoids the known `/var` versus `/private/var` fixture normalization mismatch; it does not verify alias handling in the recorder.

Run `python scripts/check.py` and `python -m unittest discover -s tests -v`. These are packaging checks. If you run a model evaluation, record conditions and actual outcomes separately using [the evaluation protocol](evals/README.md); keep raw runs local and commit only a concise, reviewable conclusion when it changes the project. Do not mark unrun cases as passing.

Changes to workflow guidance, metadata, or packaging need a plugin version bump before release. Keep marketplace metadata and release notes consistent. Avoid bundling third-party skill text without its applicable license and attribution.

Do not post sensitive vulnerability details in a public issue. Follow [SECURITY.md](SECURITY.md).
