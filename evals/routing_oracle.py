"""Independent backend/form checks for the synthetic skill-routing fixture."""

import argparse
from pathlib import Path
import subprocess
import sys


BACKEND = """from backend.orders import create_order
store = []
first = create_order(store, {'item_name': ' Pen ', 'quantity': 20})
assert first == {'id': 1, 'item_name': 'Pen', 'quantity': 20}
for payload in (
    {'item_name': '  ', 'quantity': 1},
    {'item_name': 'Pen', 'quantity': 0},
    {'item_name': 'Pen', 'quantity': 21},
    {'item_name': 'Pen', 'quantity': 1.5},
    {'item_name': 'Pen', 'quantity': True},
):
    try:
        create_order(store, payload)
    except ValueError:
        pass
    else:
        raise AssertionError(f'Accepted invalid payload: {payload}')
assert len(store) == 1
second = create_order(store, {'item_name': 'Paper', 'quantity': 1})
assert second['id'] == 2
assert len(store) == 2
"""

FORM = """import assert from 'node:assert/strict';
import { submitOrder } from './ui/order-form.mjs';
const calls = [];
const fields = { itemName: ' Pen ', quantity: '20' };
const good = await submitOrder(fields, async (path, payload) => {
  calls.push({ path, payload });
  return { status: 201, body: { id: 7, item_name: 'Pen', quantity: 20 } };
});
assert.deepEqual(calls, [{ path: '/orders', payload: { item_name: 'Pen', quantity: 20 } }]);
assert.deepEqual(good, { ok: true, order: { id: 7, item_name: 'Pen', quantity: 20 } });
for (const invalid of [
  { itemName: ' ', quantity: '1' },
  { itemName: 'Pen', quantity: '0' },
  { itemName: 'Pen', quantity: '21' },
  { itemName: 'Pen', quantity: '1.5' },
]) {
  const count = calls.length;
  const bad = await submitOrder(invalid, async () => { calls.push('unexpected'); });
  assert.equal(bad.ok, false);
  assert.deepEqual(bad.fields, invalid);
  assert.equal(calls.length, count);
}
const rejected = await submitOrder(fields, async () => ({ status: 400, body: { error: 'closed' } }));
assert.deepEqual(rejected, { ok: false, error: 'closed', fields });
"""


def assess(workspace: Path) -> dict[str, str | None]:
    commands = {
        "backend": [sys.executable, "-c", BACKEND],
        "form": ["node", "--input-type=module", "-e", FORM],
    }
    results = {}
    for name, command in commands.items():
        result = subprocess.run(command, cwd=workspace, capture_output=True, text=True, timeout=15)
        results[name] = None if result.returncode == 0 else (result.stderr.strip() or result.stdout.strip())
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    args = parser.parse_args()
    results = assess(args.workspace.resolve())
    for name, failure in results.items():
        print(f"{name}: {'PASS' if failure is None else 'FAIL: ' + failure}")
    if any(results.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
