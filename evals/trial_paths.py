"""Normalize known trial-root spellings without changing sibling paths."""

from pathlib import Path
import re
import tempfile


def neutralize_trial_paths(message: str, directory: Path) -> str:
    """Remove known trial-root spellings, including a lexical temporary-root alias."""
    parent = directory.absolute().parent
    resolved = directory.resolve().parent
    roots = {str(parent), str(resolved)}
    temporary = Path(tempfile.gettempdir())
    try:
        suffix = resolved.relative_to(temporary.resolve())
    except ValueError:
        pass
    else:
        roots.add(str(temporary / suffix))
    roots.update(root.replace("\\", "/") for root in tuple(roots))
    for root in sorted(roots, key=len, reverse=True):
        # A sibling sharing the prefix is not inside this trial root.
        message = re.sub(re.escape(root) + r"(?=$|\.(?:\s|$)|[\\/\s\"',;:!?()\[\]])", "<trial-root>", message)
    return message

