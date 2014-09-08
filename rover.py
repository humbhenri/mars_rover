class Rover(object):
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.commands = {'f': 1, 'b': -1}

    def move(self, cmds):
        for cmd in cmds:
            self.__move_one_cmd(cmd)

    def __move_one_cmd(self, cmd):
        if cmd in 'fb':
            dx, dy = self.direction * self.commands[cmd]
            self.x = self.x + dx
            self.y = self.y + dy
            self.x, self.y = self.grid.wrap(self.x, self.y)
        elif cmd == 'l':
            self.direction = self.direction.left()
        elif cmd == 'r':
            self.direction = self.direction.right()
