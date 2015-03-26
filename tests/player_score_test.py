import unittest

from classes.player_score import PlayerScore

class PlayerScoreTest(unittest.TestCase):
  def testValue(self):
    score = PlayerScore(5)
    self.assertEqual(score.value, 5)

  def testIncrement(self):
    score = PlayerScore()
    score.increment()

    self.assertEqual(score.value, 1)

  def testDecrementWithZeroValue(self):
    score = PlayerScore()
    score.decrement()

    self.assertEqual(score.value, 0)

  def testDecrementWithPositiveValue(self):
    score = PlayerScore(5)
    score.decrement()

    self.assertEqual(score.value, 4)