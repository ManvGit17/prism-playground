"""Domain models."""


class Item:
    """A thing for sale."""

    tax_free = False

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total(self, qty):
        return self.price * qty

    @property
    def label(self):
        return self.name.title()

    @label.setter
    def label(self, value):
        self.name = value


class DiscountItem(Item):
    def total(self, qty):
        base = super().total(qty)
        return apply_discount(base)

    def describe(self):
        return f"{self.name}: {self.total(1)}"


def apply_discount(amount):
    """Take ten percent off."""
    return amount * 0.9
