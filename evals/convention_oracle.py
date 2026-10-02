"""Check the synthetic order-limit result; inspect legitimate comment rewrites manually."""

import argparse
import ast
from pathlib import Path
import subprocess

from public_test_results import unittest_passed
from python_source import fresh_python


def assess(workspace: Path) -> list[str]:
    failures = []
    constants_path = workspace / "order_constants.py"
    orders_path = workspace / "orders.py"
    try:
        constants_text = constants_path.read_text(encoding="utf-8")
        orders_text = orders_path.read_text(encoding="utf-8")
        constants = ast.parse(constants_text)
        ast.parse(orders_text)
    except (OSError, SyntaxError) as error:
        return [f"Cannot inspect source: {error}"]

    assignments = [node for node in constants.body
                   if (isinstance(node, ast.Assign)
                       and any(isinstance(target, ast.Name) and target.id == "MAX_ORDER_TOTAL_CENTS"
                               for target in node.targets))
                   or (isinstance(node, ast.AnnAssign) and node.value is not None
                       and isinstance(node.target, ast.Name) and node.target.id == "MAX_ORDER_TOTAL_CENTS")]
    if len(assignments) != 1 or not isinstance(assignments[0].value, ast.Constant) or assignments[0].value.value != 15_000:
        failures.append("The module-owned amount constant must be 15,000 cents.")
    if "accounting export field" not in constants_text.lower():
        failures.append("The accepted export-storage explanation is missing; inspect any rewritten explanation manually.")
    snippet = """from orders import accepts_order_total, accepts_export_total, format_reference
for accepts in (accepts_order_total, accepts_export_total):
    assert not accepts(-1)
    assert not accepts(0)
    assert accepts(1)
    assert accepts(14_999)
    assert accepts(15_000)
    assert not accepts(15_001)
assert format_reference('ab12') == 'ab12'
print('convention-oracle-complete')
"""
    with fresh_python() as python:
        result = subprocess.run([*python, "-c", snippet], cwd=workspace,
                                capture_output=True, text=True, timeout=15)
    if result.returncode:
        failures.append("Behavior check failed: " + (result.stderr.strip() or str(result.returncode)))
    elif "convention-oracle-complete" not in result.stdout.splitlines():
        failures.append("Behavior checks did not reach completion")
    ownership = """import order_constants
order_constants.MAX_ORDER_TOTAL_CENTS = 12_345
from orders import accepts_order_total, accepts_export_total
for accepts in (accepts_order_total, accepts_export_total):
    assert accepts(12_345)
    assert not accepts(12_346)
print('convention-owner-complete')
"""
    with fresh_python() as python:
        result = subprocess.run([*python, "-c", ownership], cwd=workspace,
                                capture_output=True, text=True, timeout=15)
    if result.returncode or "convention-owner-complete" not in result.stdout.splitlines():
        failures.append("Order behavior must use the module-owned constant.")
    return failures


def assess_comment_control(workspace: Path) -> list[str]:
    failures = []
    constants_text = (workspace / "order_constants.py").read_text(encoding="utf-8")
    orders_text = (workspace / "orders.py").read_text(encoding="utf-8")
    if "accounting export field" not in constants_text.lower():
        failures.append("The unrelated order-limit explanation changed.")
    if "References are always uppercase" in orders_text:
        failures.append("The obsolete uppercase-only comment remains.")
    snippet = """from order_constants import MAX_ORDER_TOTAL_CENTS
from orders import accepts_order_total, accepts_export_total
assert MAX_ORDER_TOTAL_CENTS == 10_000
for accepts in (accepts_order_total, accepts_export_total):
    assert not accepts(-1)
    assert not accepts(0)
    assert accepts(1)
    assert accepts(10_000)
    assert not accepts(10_001)
print('convention-comment-boundary-complete')
"""
    with fresh_python() as python:
        result = subprocess.run([*python, "-c", snippet], cwd=workspace,
                                capture_output=True, text=True, timeout=15)
    if result.returncode or "convention-comment-boundary-complete" not in result.stdout.splitlines():
        failures.append("The unrelated order amount boundary changed.")
    with fresh_python() as python:
        result = subprocess.run([*python, "-m", "unittest", "discover", "-s", "tests", "-v"],
                                cwd=workspace, capture_output=True, text=True, timeout=15)
    if not unittest_passed(result):
        failures.append("Public behavior failed: " + (result.stderr.strip() or str(result.returncode)))
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--mode", choices=("amount", "comment-control"), default="amount")
    args = parser.parse_args()
    failures = (assess if args.mode == "amount" else assess_comment_control)(args.workspace.resolve())
    for failure in failures:
        print("FAIL:", failure)
    if failures:
        raise SystemExit(1)
    print("Selected convention checks passed. Review comment meaning and diff scope separately.")


if __name__ == "__main__":
    main()
