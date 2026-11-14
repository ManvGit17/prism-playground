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
