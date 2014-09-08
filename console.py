#!/usr/bin/env python


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))


class Console(object):
    def __init__(self, rover):
        grid = rover.grid
        self.w = grid.w
        self.h = grid.h
        self.rover = rover
        self.print_grid()

    def __setitem__(self, key, val):
        y, x = key
        self.characters[x * self.w + y] = val

    def __str__(self):
        self.print_grid()
        rows = chunker(str(self.characters), self.w)
        return '\n'.join(rows)

    def print_rover(self):
        self[self.rover.x, self.rover.y] = 'R'
        if self.rover.direction == Direction.N and self.rover.y-1 >= 0:
            self[self.rover.x, self.rover.y-1] = '^'
        elif self.rover.direction == Direction.S and self.rover.y+1 < self.h:
            self[self.rover.x, self.rover.y+1] = 'v'
        elif self.rover.direction == Direction.E and self.rover.x-1 >= 0:
            self[self.rover.x-1, self.rover.y] = '<'
        elif self.rover.direction == Direction.W and self.rover.x+1 < self.w:
            self[self.rover.x+1, self.rover.y] = '>'

    def print_grid(self):
        self.characters = bytearray('.' * self.h * self.w)
        self.print_rover()


if __name__ == '__main__':
    from direction import Direction
    from grid import Grid
    from rover import Rover
    rover = Rover(0, 0, Direction.S, Grid(10, 10))
    consoleGrid = Console(rover)
    while True:
        cmds = raw_input('Enter commands: ')
        rover.move(cmds)
        print consoleGrid
