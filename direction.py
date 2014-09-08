DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class Vector(object):
    def __init__(self, dir):
        self.dir = dir

    def __mul__(self, s):
        d = DIR[self.dir]
        return d[0] * s, d[1] * s

    def left(self):
        return Vector((self.dir - 1) % len(DIR))

    def right(self):
        return Vector((self.dir + 1) % len(DIR))

    def __repr__(self):
        return 'NWSE'[self.dir]

    def __eq__(self, other):
        return self.dir == other.dir


class Direction(object):
    N = Vector(0)
    W = Vector(1)
    S = Vector(2)
    E = Vector(3)
