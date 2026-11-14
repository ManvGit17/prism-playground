from shop import pricing


def test_with_tax():
    assert pricing.with_tax(10) == 12.0
