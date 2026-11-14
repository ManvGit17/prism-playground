"""Helpers."""

import functools


def cached(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        return fn(*args)

    return wrapper


@cached
def slugify(text):
    """Make a slug."""
    return _clean(text).replace(" ", "-")


def _clean(text):
    return text.strip().lower()


def log_event(name, value):
    print(name, value)
