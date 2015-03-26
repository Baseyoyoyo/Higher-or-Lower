import unittest

from classes.levels import Levels

class LevelsTest(unittest.TestCase):
  def testQuantity(self):
    levels = Levels(15)

    self.assertEqual(levels.quantity, 15)

  def testRangeFor(self):
    levels = Levels(3)

    range = levels.rangeFor(1)
    self.assertEqual(range[1], 20)

    range = levels.rangeFor(5)
    self.assertEqual(range[1], 100)