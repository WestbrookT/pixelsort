


class Pixel:

    def __init__(self, r=255, g=255, b=255, a=255, tup=None):
        if tup != None:
            self.r = tup[0]
            self.g = tup[1]
            self.b = tup[2]
            if len(tup) == 4:
                self.a = tup[3]
        else:
            self.r = r
            self.g = g
            self.b = b
            self.a = a

    def set_compare(self, comparator):
        self._lt = comparator

    def __lt__(self, other):
        return self._lt(self, other)