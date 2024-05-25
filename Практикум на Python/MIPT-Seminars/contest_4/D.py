import functools
from collections import OrderedDict


def cache(size):
    def wraps(func):
        cached = OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args
            for item in kwargs.items():
                key += item
            if key in cached:
                return cached[key]
            value = func(*args, **kwargs)
            cached[key] = value
            if len(cached) > size:
                cached.popitem(last=False)
            return value
        return wrapper
    return wraps


@cache(2)
def foo(value, **kwargs):
    print("calculate foo for {}".format(value))
    return value


foo(1, a=1)
foo(2)
foo(1)
foo(2)
foo(3)
foo(1)

