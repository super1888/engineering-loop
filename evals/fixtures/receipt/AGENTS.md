# Receipt fixture project

This is an isolated exercise, not a production ERP. Python standard library only.

- `inventory.py` owns order and receipt persistence. Keep its public API.
- Accepted behavior is in `RULES.md`; do not change it to fit the implementation.
- `python -m unittest discover -s tests -v` runs local checks. CI is not configured here; do not claim it ran.
- Use `WORK.md` for a short task status if needed. Do not create another planning system, a Git branch, or a worktree.
- Preserve existing tests; add meaningful cases as needed. No installation, network calls, publication or changes outside this fixture.
