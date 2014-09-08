class Grid(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def wrap(self, x, y):
        return x % self.w, y % self.h
