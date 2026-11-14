"""Prices and tax."""

TAX = 0.2


def with_tax(amount):
    return round_price(amount * (1 + TAX))


def round_price(value):
    return round(value, 2)
