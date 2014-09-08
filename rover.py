class Rover(object):
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def command(self, cmd):
        if self.is_fwd(cmd):
            self.y += 1

    def is_fwd(self, cmd):
        return cmd == 'f'
