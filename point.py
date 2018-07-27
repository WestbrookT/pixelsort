

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_compare(self, comparator):
        self._lt = comparator

    def __lt__(self, other):
        return self._lt(self, other)