# Order creation contract

`backend.orders.create_order(store, payload)` is the backend operation. `payload` has `item_name` (string) and `quantity` (integer). It strips surrounding spaces from the name, rejects an empty result and quantities outside 1..20, and raises `ValueError` for invalid input without changing `store`. On success it appends `{"id": next_id, "item_name": name, "quantity": quantity}` to `store` and returns that object. IDs start at 1 and increase only for accepted orders.

The form submits to `POST /orders`. `postJson(path, payload)` returns `{status, body}`; status 201 has the order object above and status 400 has `{error: message}`. Form fields use `itemName` and a string `quantity`; map them to the API payload only when valid. The transport is supplied by the caller, so the form module needs no network dependency.
