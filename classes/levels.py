import random

class Levels(object):
  def __init__(self, quantity = 20):
    self.quantity = quantity
    self.counter = 0
    self.values = self.generateAnswers()

  def __iter__(self):
    return self

  def next(self):
    if self.counter + 1 == self.quantity:
      raise StopIteration

    self.counter = self.counter + 1

    return self.currentAnswer()

  def rangeFor(self, index):
    return [1, index * 20]

  def generateNumber(self, count):
    range = self.rangeFor(count)

    return {
      "floor": range[0],
      "ceiling": range[1],
      "value": random.randrange(range[0], range[1], count)
    }

  def generateAnswers(self):
    count = 1
    numbers = []

    while count <= self.quantity:
      numbers.append(self.generateNumber(count))

      count = count + 1

    return numbers
  
  def validateAnswer(self, answer):
    current_answer = self.currentAnswer()["value"]
    previous_answer = self.previousAnswer()["value"]

    return (previous_answer > current_answer and answer == "l") or (current_answer > previous_answer and answer == "h")

  def currentAnswer(self):
    return self.values[self.counter]

  def previousAnswer(self):
    return self.values[self.counter - 1]