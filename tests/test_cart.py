from shop.cart import Cart, make_cart
from shop.models import Item


def test_make_cart():
    cart = make_cart()
    assert cart.subtotal() == 1.0


class TestCart:
    def test_checkout(self):
        cart = Cart()
        cart.add(Item("a", 2.0))
        assert cart.checkout() > 0

    def helper(self):
        return Cart()
