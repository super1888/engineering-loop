"""Independent backend/form checks for the synthetic skill-routing fixture."""

import argparse
from pathlib import Path
import subprocess

from python_source import fresh_python


BACKEND = """from backend.orders import create_order
store = []
first = create_order(store, {'item_name': ' Pen ', 'quantity': 20})
assert first == {'id': 1, 'item_name': 'Pen', 'quantity': 20}
assert not isinstance(first['id'], bool)
for payload in (
    {},
    {'item_name': 'Pen'},
    {'quantity': 1},
    {'item_name': '  ', 'quantity': 1},
    {'item_name': None, 'quantity': 1},
    {'item_name': 123, 'quantity': 1},
    {'item_name': 'Pen', 'quantity': None},
    {'item_name': 'Pen', 'quantity': '2'},
    {'item_name': 'Pen', 'quantity': -1},
    {'item_name': 'Pen', 'quantity': 0},
    {'item_name': 'Pen', 'quantity': 21},
    {'item_name': 'Pen', 'quantity': 1.5},
    {'item_name': 'Pen', 'quantity': 1.0},
    {'item_name': 'Pen', 'quantity': True},
):
    try:
        create_order(store, payload)
    except ValueError:
        pass
    else:
        raise AssertionError(f'Accepted invalid payload: {payload}')
    assert store == [{'id': 1, 'item_name': 'Pen', 'quantity': 20}]
second = create_order(store, {'item_name': 'Paper', 'quantity': 1})
assert second == {'id': 2, 'item_name': 'Paper', 'quantity': 1}
assert not isinstance(second['quantity'], bool)
assert store == [{'id': 1, 'item_name': 'Pen', 'quantity': 20}, second]
expected_store = [dict(order) for order in store]
for quantity in range(2, 20):
    expected = {'id': len(expected_store) + 1, 'item_name': 'Paper', 'quantity': quantity}
    expected_store.append(expected)
    assert create_order(store, {'item_name': 'Paper', 'quantity': quantity}) == expected
    assert store == expected_store
print('routing-oracle-complete:backend')
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
const minimum = await submitOrder({ itemName: ' Paper ', quantity: '1' }, async (path, payload) => {
  calls.push({ path, payload });
  return { status: 201, body: { id: 8, item_name: 'Paper', quantity: 1 } };
});
assert.deepEqual(calls[1], { path: '/orders', payload: { item_name: 'Paper', quantity: 1 } });
assert.equal(calls.length, 2);
assert.deepEqual(minimum, { ok: true, order: { id: 8, item_name: 'Paper', quantity: 1 } });
for (let quantity = 2; quantity < 20; quantity++) {
  const order = { id: quantity + 8, item_name: 'Paper', quantity };
  const result = await submitOrder({ itemName: ' Paper ', quantity: String(quantity) }, async (path, payload) => {
    calls.push({ path, payload });
    assert.deepEqual({ path, payload }, { path: '/orders', payload: { item_name: 'Paper', quantity } });
    return { status: 201, body: { ...order } };
  });
  assert.equal(calls.length, quantity + 1);
  assert.deepEqual(result, { ok: true, order });
}
for (const invalid of [
  { itemName: ' ', quantity: '1' },
  { itemName: 'Pen', quantity: '-1' },
  { itemName: 'Pen', quantity: '0' },
  { itemName: 'Pen', quantity: '21' },
  { itemName: 'Pen', quantity: '1.5' },
  { itemName: 'Pen', quantity: '2x' },
]) {
  const count = calls.length;
  const original = { ...invalid };
  const bad = await submitOrder(invalid, async () => { calls.push('unexpected'); });
  assert.equal(bad.ok, false);
  assert.equal(typeof bad.error, "string");
  assert.ok(bad.error.trim());
  assert.deepEqual(bad.fields, original);
  assert.equal(calls.length, count);
}
const originalFields = { ...fields };
const rejected = await submitOrder(fields, async () => ({ status: 400, body: { error: 'closed' } }));
assert.deepEqual(rejected, { ok: false, error: 'closed', fields: originalFields });
console.log('routing-oracle-complete:form');
"""


def assess(workspace: Path) -> dict[str, str | None]:
    results = {}
    with fresh_python() as python:
        commands = {
            "backend": [*python, "-c", BACKEND],
            "form": ["node", "--input-type=module", "-e", FORM],
        }
        for name, command in commands.items():
            result = subprocess.run(command, cwd=workspace, capture_output=True, text=True,
                                    encoding="utf-8", errors="replace", timeout=15)
            if result.returncode:
                results[name] = result.stderr.strip() or result.stdout.strip() or f"Process exited with code {result.returncode}"
            elif f"routing-oracle-complete:{name}" not in result.stdout.splitlines():
                results[name] = "Behavior checks did not reach completion"
            else:
                results[name] = None
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
