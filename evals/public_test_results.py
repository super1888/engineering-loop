"""Require executed, unskipped tests in native synthetic-fixture reports."""

import re
import subprocess


def unittest_passed(result: subprocess.CompletedProcess[str]) -> bool:
    return (result.returncode == 0
            and re.search(r"^Ran [1-9]\d* tests? in ", result.stderr, re.M) is not None
            and result.stderr.rstrip().endswith("\nOK"))


def node_tap_passed(result: subprocess.CompletedProcess[str], minimum_tests: int) -> bool:
    counts = {name: int(count) for name, count in re.findall(
        r"^# (tests|pass|fail|cancelled|skipped|todo) (\d+)$", result.stdout, re.M)}
    return (result.returncode == 0
            and counts.get("tests", 0) >= minimum_tests
            and counts.get("pass") == counts.get("tests")
            and all(counts.get(name) == 0 for name in ("fail", "cancelled", "skipped", "todo")))
