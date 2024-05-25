import numbers
import collections.abc
from app import VeryImportantClass, decorator


class HackedClass(VeryImportantClass):
    def __getattribute__(self, item):
        attr = super().__getattribute__(item)
        if item.startswith('_'):
            return attr
        elif isinstance(attr, numbers.Number):
            return attr * 2
        elif callable(attr):
            return decorator(attr)
        elif isinstance(attr, collections.abc.Container):
            return type(attr)()
        else:
            return attr

