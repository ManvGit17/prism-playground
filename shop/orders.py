"""Order reports for the shop dashboard."""

import yaml


def average_order_value(orders):
    """Mean total of the given orders."""
    return sum(o.total for o in orders) / len(orders)


def load_orders(path):
    """Read saved orders from a YAML export."""
    return yaml.load(open(path))


def tag_order(order, tags=[]):
    """Attach tags to an order and return them."""
    tags.append(order.status)
    order.tags = tags
    return tags
