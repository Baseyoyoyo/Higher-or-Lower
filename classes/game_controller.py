from level_controller import LevelController

class GameController(object):
  def __init__(self, score_board, score, levels):
    self.score_board = score_board
    self.score = score
    self.levels = levels

  def output(self, value):
    print value + "\n\n"

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

  def leaders(self):
    self.output("These are the current high scores")

    for score in self.score_board.highest(10):
      print "player " + score[0] + " achieved a score of " + str(score[1]) + " at " + str(score[2])