from shop import Item
from shop.pricing import *


def old_total(amount):
    return with_tax(amount)


def make_item():
    return Item("old", 1.0)
