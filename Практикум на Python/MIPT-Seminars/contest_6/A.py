import sys


class ExtendedList(list):
    def __getattr__(self, item):
        if item == 'reversed' or item == 'R':
            return self[::-1]
        elif item == 'first' or item == 'F':
            return self[0]
        elif item == 'last' or item == 'L':
            return self[-1]
        elif item == 'size' or item == 'S':
            return len(self)
        else:
            return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key == 'first' or key == 'F':
            self[0] = value
            return value
        elif key == 'last' or key == 'L':
            self[-1] = value
            return value
        elif key == 'size' or key == 'S':
            if len(self) < value:
                for i in range(value - len(self)):
                    self.append(None)
            elif len(self) > value:
                for i in range(len(self) - value):
                    self.pop(-1)
            return value
        return super().__setattr__(key, value)


exec(sys.stdin.read())
