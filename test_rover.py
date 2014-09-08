import unittest
from . rover import Rover
from . direction import Direction
from . grid import Grid


class TestRover(unittest.TestCase):

    def setUp(self):
        self.rover = Rover(0, 0, Direction.N, Grid(100, 100))

    def testShouldCreateARoverWithStartingPointAndDirection(self):
        self.assertEqual(0, self.rover.x)
        self.assertEqual(0, self.rover.y)
        self.assertEqual(Direction.N, self.rover.direction)

    def testShouldMoveForward(self):
        self.rover.direction = Direction.S
        self.rover.move('f')
        self.assertEqual(0, self.rover.x)
        self.assertEqual(1, self.rover.y)
        self.assertEqual(Direction.S, self.rover.direction)

    def testShouldMoveBackward(self):
        rover = Rover(1, 1, Direction.S, Grid(100, 100))
        rover.move('b')
        self.assertEqual(1, rover.x)
        self.assertEqual(0, rover.y)
        self.assertEqual(Direction.S, rover.direction)

    def testShouldMoveForwardDirectionNorth(self):
        self.rover.direction = Direction.N
        self.rover.y = 1
        self.rover.move('f')
        self.assertEqual(0, self.rover.y)

    def testShouldMoveBackwardDirectionNorth(self):
        self.rover.direction = Direction.S
        self.rover.y = 1
        self.rover.move('b')
        self.assertEqual(0, self.rover.y)

    def testShouldMoveForwardDirectionEast(self):
        self.rover.direction = Direction.E
        self.rover.x = 1
        self.rover.move('f')
        self.assertEqual(0, self.rover.x)

    def testShouldMoveForwardDirectionWest(self):
        self.rover.direction = Direction.W
        self.rover.x = 1
        self.rover.move('f')
        self.assertEqual(2, self.rover.x)

    def testShouldMoveBackwardDirectionEast(self):
        self.rover.direction = Direction.E
        self.rover.x = 1
        self.rover.move('b')
        self.assertEqual(2, self.rover.x)

    def testShouldMoveBackwardDirectionWest(self):
        self.rover.direction = Direction.W
        self.rover.x = 1
        self.rover.move('b')
        self.assertEqual(0, self.rover.x)

    def testShouldMoveLeft(self):
        self.rover.direction = Direction.W
        self.rover.move('l')
        self.assertEqual(Direction.N, self.rover.direction)

    def testShouldMoveRigth(self):
        self.rover.direction = Direction.W
        self.rover.move('r')
        self.assertEqual(Direction.S, self.rover.direction)

    def testShouldMoveManyCommands(self):
        self.rover.direction = Direction.S
        self.rover.move('fflff')
        self.assertEqual(2, self.rover.y)
        self.assertEqual(2, self.rover.x)
        self.assertEqual(Direction.W, self.rover.direction)

    def testShouldMoveToAnotherEdgeOfTheGrid(self):
        self.rover.move('f')
        self.assertEqual(0, self.rover.x)
        self.assertEqual(99, self.rover.y)

    def testShouldMoveToAnotherEdgeOfTheGrid2(self):
        self.rover.move('lffrf')
        self.assertEqual(98, self.rover.x)
        self.assertEqual(99, self.rover.y)
