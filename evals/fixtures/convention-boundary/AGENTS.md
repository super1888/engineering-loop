# Synthetic project conventions

- Follow ORDER.md for accepted behavior. Work only in this exercise workspace.
- Stable order limits belong in `order_constants.py` with names that describe their meaning.
- Keep comments that explain a current business or storage constraint. Correct comments when the constraint changes; remove comments that have become false.
- A one-use incidental value does not need a named constant merely to shorten a function.
- Run `python -m unittest discover -s tests -v` after changing behavior. Do not weaken existing tests.
