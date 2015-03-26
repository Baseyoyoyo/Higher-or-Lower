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

  def generateAnswers(self):
    count = 1
    answers = []

    while count <= self.quantity:
      answers.append(random.randrange(1, count * 20))

      count = count + 1

    return answers
  
  def validateAnswer(self, answer):
    return (self.previousAnswer() > self.currentAnswer() and answer == "l") or (self.currentAnswer() > self.previousAnswer() and answer == "h")

  def currentAnswer(self):
    return self.values[self.counter]

  def previousAnswer(self):
    return self.values[self.counter - 1]