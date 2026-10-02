"""Execute trusted candidate sources without reusing or changing their bytecode."""

from contextlib import contextmanager
import sys
import tempfile


@contextmanager
def fresh_python():
    with tempfile.TemporaryDirectory(prefix="eval-pycache-") as cache:
        previous = sys.pycache_prefix, sys.dont_write_bytecode
        sys.pycache_prefix, sys.dont_write_bytecode = cache, True
        try:
            yield [sys.executable, "-B", "-X", f"pycache_prefix={cache}"]
        finally:
            sys.pycache_prefix, sys.dont_write_bytecode = previous
