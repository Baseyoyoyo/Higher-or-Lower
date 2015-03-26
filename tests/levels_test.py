import unittest

from classes.levels import Levels

class LevelsTest(unittest.TestCase):
  def testQuantity(self):
    levels = Levels(15)

    self.assertEqual(levels.quantity, 15)

  def testRangeFor(self):
    levels = Levels(3)

    range = levels.rangeFor(2)
    self.assertEqual(range[1], 40)

  def testGenerateNumberRange(self):
    levels = Levels(3)

    number = levels.generateNumber(5)

    self.assertEqual(type(number["floor"]), int)
    self.assertEqual(type(number["ceiling"]), int)

  def testGenerateNumberValue(self):
    levels = Levels(3)

    number = levels.generateNumber(5)

    self.assertEqual(type(number["value"]), int)

    self.assertGreater(number["value"], 0)
    self.assertLess(number["value"], 100)

  def testGenerateAnswers(self):
    levels = Levels(10)

    answers = levels.generateAnswers()

    self.assertEqual(len(answers), 10)

  def testValidateAnswer(self):
    levels = Levels(5)

    levels.currentAnswer = lambda: { "value": 10 }
    levels.previousAnswer = lambda: { "value": 11 }

    self.assertTrue(levels.validateAnswer("l"))
    self.assertFalse(levels.validateAnswer("h"))
