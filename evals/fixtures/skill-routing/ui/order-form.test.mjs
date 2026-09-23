import assert from "node:assert/strict";
import test from "node:test";
import { submitOrder } from "./order-form.mjs";

test("submits mapped fields and returns the saved order", async () => {
  const calls = [];
  const postJson = async (path, payload) => {
    calls.push({ path, payload });
    return { status: 201, body: { id: 1, item_name: "Pen", quantity: 2 } };
  };
  const result = await submitOrder({ itemName: " Pen ", quantity: "2" }, postJson);
  assert.deepEqual(calls, [{ path: "/orders", payload: { item_name: "Pen", quantity: 2 } }]);
  assert.deepEqual(result, { ok: true, order: { id: 1, item_name: "Pen", quantity: 2 } });
});

test("keeps input when the server rejects the order", async () => {
  const fields = { itemName: "Pen", quantity: "2" };
  const result = await submitOrder(fields, async () => ({ status: 400, body: { error: "closed" } }));
  assert.deepEqual(result, { ok: false, error: "closed", fields });
});
