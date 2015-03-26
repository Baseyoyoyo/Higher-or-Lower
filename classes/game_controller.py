from level_controller import LevelController

class GameController(object):
  def __init__(self, score_board, score, levels):
    self.score_board = score_board
    self.score = score
    self.levels = levels

  def output(self, value):
    print value

  def welcomeMessage(self):
    self.output("Hello and welcome to my higher or lower number guessing game.")
  
  def getName(self):
    self.name = raw_input("Whats your name? ")

  def runLevels(self):
    for number in self.levels:
      level = LevelController(self, number)

      level.intro()
      level.getAnswer()
      level.outcome()

  def complete(self):
    self.score_board.add(self.name, self.score.value)
    self.output("Well done your score is " + str(self.score) + " Good Job")