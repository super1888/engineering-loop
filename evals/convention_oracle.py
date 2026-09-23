"""Check the synthetic order-limit result; inspect legitimate comment rewrites manually."""

import argparse
import ast
from pathlib import Path
import subprocess
import sys


def assess(workspace: Path) -> list[str]:
    failures = []
    constants_path = workspace / "order_constants.py"
    orders_path = workspace / "orders.py"
    try:
        constants_text = constants_path.read_text(encoding="utf-8")
        orders_text = orders_path.read_text(encoding="utf-8")
        constants = ast.parse(constants_text)
        orders = ast.parse(orders_text)
    except (OSError, SyntaxError) as error:
        return [f"Cannot inspect source: {error}"]

    assignments = [node for node in constants.body if isinstance(node, ast.Assign)
                   and any(isinstance(target, ast.Name) and target.id == "MAX_ORDER_TOTAL_CENTS"
                           for target in node.targets)]
    if len(assignments) != 1 or not isinstance(assignments[0].value, ast.Constant) or assignments[0].value.value != 15_000:
        failures.append("The module-owned amount constant must be 15,000 cents.")
    if "accounting export field" not in constants_text.lower():
        failures.append("The accepted export-storage explanation is missing; inspect any rewritten explanation manually.")
    imported = any(isinstance(node, ast.ImportFrom) and node.module == "order_constants"
                   and any(alias.name == "MAX_ORDER_TOTAL_CENTS" for alias in node.names)
                   for node in orders.body)
    used = any(isinstance(node, ast.Name) and node.id == "MAX_ORDER_TOTAL_CENTS"
               and isinstance(node.ctx, ast.Load) for node in ast.walk(orders))
    if not imported or not used:
        failures.append("Order behavior must use the module-owned constant.")
    snippet = """from orders import accepts_order_total, accepts_export_total, format_reference
for accepts in (accepts_order_total, accepts_export_total):
    assert not accepts(-1)
    assert not accepts(0)
    assert accepts(1)
    assert accepts(14_999)
    assert accepts(15_000)
    assert not accepts(15_001)
assert format_reference('ab12') == 'ab12'
"""
    result = subprocess.run([sys.executable, "-c", snippet], cwd=workspace,
                            capture_output=True, text=True, timeout=15)
    if result.returncode:
        failures.append("Behavior check failed: " + (result.stderr.strip() or str(result.returncode)))
    return failures


def assess_comment_control(workspace: Path) -> list[str]:
    failures = []
    constants_text = (workspace / "order_constants.py").read_text(encoding="utf-8")
    orders_text = (workspace / "orders.py").read_text(encoding="utf-8")
    if "MAX_ORDER_TOTAL_CENTS = 10_000" not in constants_text or "accounting export field" not in constants_text.lower():
        failures.append("The unrelated order limit or its explanation changed.")
    if "References are always uppercase" in orders_text:
        failures.append("The obsolete uppercase-only comment remains.")
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
                            cwd=workspace, capture_output=True, text=True, timeout=15)
    if result.returncode:
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
