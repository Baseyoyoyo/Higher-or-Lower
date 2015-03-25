class PlayerScore(object):
  def __init__(self):
    self.value = 0

  def increment(self):
    self.value = self.value + 1

  def decrement(self):
    if self.value > 0:
      self.value = self.value - 1

  def __index__(self):
    return self.value

  def __str__(self):
    return str(self.value)