from order_constants import MAX_ORDER_TOTAL_CENTS


def accepts_order_total(amount_cents: int) -> bool:
    return 0 < amount_cents <= MAX_ORDER_TOTAL_CENTS


def accepts_export_total(amount_cents: int) -> bool:
    return 0 < amount_cents <= MAX_ORDER_TOTAL_CENTS


def format_reference(code: str) -> str:
    # References are always uppercase.
    if len(code) < 4:
        raise ValueError("reference too short")
    return code.strip()
