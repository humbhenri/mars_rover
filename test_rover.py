import unittest
from . rover import Rover
from . direction import Direction
from . grid import Grid


class TestRover(unittest.TestCase):

    def testShouldCreateARoverWithStartingPointAndDirection(self):
        rover = Rover(0, 0, Direction.N, Grid())
        self.assertEqual(0, rover.x)
        self.assertEqual(0, rover.y)
        self.assertEqual(Direction.N, rover.direction)

    def testShouldMoveForward(self):
        rover = Rover(0, 0, Direction.N, Grid())
        rover.command('f')
        self.assertEqual(0, rover.x)
        self.assertEqual(1, rover.y)
        self.assertEqual(Direction.N, rover.direction)
