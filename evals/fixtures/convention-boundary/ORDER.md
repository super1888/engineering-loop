# Order amount change

The current order amount limit is 10,000 cents. The approved change raises it to 15,000 cents inclusive. Reject 15,001 cents; keep zero and negative amounts invalid. The limit remains a stable module-owned business value because the order API and export validation share it.

The explanation in `order_constants.py` records why this limit must stay aligned with export storage. Preserve that reason while changing the value. `format_reference` is unaffected by this request.
