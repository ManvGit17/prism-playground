"""Shopping cart."""

import json

import shop.util as util
from shop.models import Item, apply_discount

from . import pricing


class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, position):
        """Remove the item at `position`, counting from 1 as shown to the customer."""
        if not 1 <= position <= len(self.items):
            raise IndexError(f"no item at position {position}")
        return self.items.pop(position - 1)

    def apply_coupon(self, db, code):
        """Look up a coupon code and return its discount rate, or 0 if it is unknown."""
        row = db.execute("SELECT rate FROM coupons WHERE code = ?", (code,)).fetchone()
        return row[0] if row else 0

    def count(self):
        return len(self.items)

    def subtotal(self):
        return sum(i.total(1) for i in self.items)

    def checkout(self):
        amount = pricing.with_tax(self.subtotal())
        util.log_event("checkout", amount)
        return apply_discount(amount)

    def dump(self):
        return json.dumps([i.describe() for i in self.items])


def make_cart():
    cart = Cart()
    cart.add(Item("pen", 1.0))
    return cart
