import sys
import functools


def takes(*types):
    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(min(len(types), len(args))):
                if not isinstance(args[i], types[i]):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return wraps


exec(sys.stdin.read())
