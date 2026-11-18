from shop.shipping import shipping_cost


def test_small_order_pays_shipping():
    assert shipping_cost(10.0, 2) == 7.49


def test_large_order_ships_free():
    assert shipping_cost(80.0, 2) == 0.0
