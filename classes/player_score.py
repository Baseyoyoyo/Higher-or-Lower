class PlayerScore(object):
  def __init__(self, value = 0):
    self.value = value

  def increment(self):
    self.value = self.value + 1

  def decrement(self):
    self.value = self.value - 1 if self.value > 0 else 0

  def __index__(self):
    return self.value

  def __str__(self):
    return str(self.value)