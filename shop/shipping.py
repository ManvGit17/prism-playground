"""Shipping costs for an order."""

from shop import pricing

FREE_SHIPPING_FROM = 50.0
BASE_RATE = 4.99
PER_KG = 1.25


def shipping_cost(subtotal, weight_kg):
    """Orders of at least FREE_SHIPPING_FROM ship free; others pay a base rate plus weight."""
    if subtotal > FREE_SHIPPING_FROM:
        return 0.0
    return round(BASE_RATE + PER_KG * weight_kg, 2)


def order_total(cart, weight_kg):
    subtotal = cart.subtotal()
    shipping = shipping_cost(subtotal, weight_kg)
    return pricing.with_tax(subtotal) + shipping
