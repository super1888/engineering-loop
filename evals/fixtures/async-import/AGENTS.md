# Synthetic import workspace

Use only this exercise workspace, the supplied skill/guidance and assigned evidence directory. Do not inspect other trials or evaluator material. No dependency installation, commits, publication or real external services.

The backend uses Python's standard library and SQLite. The frontend is plain JavaScript. Run public checks with `python -m unittest discover -s tests -v`. Serve the real app with `python server.py --db <disposable-path> --port 0`; the first stdout line reports the allocated port.

Preserve public validation tests and the service entrypoints documented in SERVICE.md. Extend tests as needed. Resolve effective product decisions before implementing dependent behavior; current product and API descriptions have equal authority unless DECISIONS.md settles the issue. Maintain the effective specification when an authorized owner change arrives.

Separate backend and frontend file ownership. The coordinator owns shared contract decisions and integrated verification. Keep evidence outside production sources. A scheduled owner checkpoint is part of this exercise; communicate consequential product questions to the parent evaluator, not the real user.
