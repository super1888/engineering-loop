# Order form behavior

When a user enters a product name and quantity and submits the form, create one order and return its server-issued ID. Trim the name and accept quantities 1 through 20. Blank names, noninteger quantities and out-of-range quantities fail locally without calling the API. A backend rejection also reports an error. On any failure, keep the original form fields so the user can correct them.

`submitOrder(fields, postJson)` returns `{ok: true, order}` on success and `{ok: false, error, fields}` on failure. It must pass `/orders` and the API payload to `postJson`. This fixture tests form submission logic rather than rendered layout or a production HTTP service.
