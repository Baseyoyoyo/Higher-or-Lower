import random

class Levels(object):
  def __init__(self, quantity = 20):
    self.quantity = quantity
    self.counter = 0
    self.values = self.generateAnswers()

  def __iter__(self):
    return self

  def next(self):
    if self.counter >= self.quantity:
      raise StopIteration
      
    answer = self.values[self.counter]

    self.counter = self.counter + 1

    return answer

  def generateAnswers(self):
    count = 1
    answers = []

    while count <= self.quantity:
      answers.append(random.randrange(1, count*20))

      count = count + 1

    return answers

