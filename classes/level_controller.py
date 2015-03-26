class LevelController(object):
    def __init__(self, game, number):
      self.game = game
      self.number = number

    def intro(self):
      self.game.output("Keep in mind that the numbers range from 1 to " + str(self.game.levels.counter * 20))
      self.game.output("Your number is " + str(self.game.levels.previousAnswer()) + ". So will the next number be higher or lower?")

    def getAnswer(self):
      self.answer = raw_input("Enter either h or l: ")

    def success(self):
      self.game.score.increment()
      self.game.output("Well done the number was " + str(self.number) + " Your score at the end of the round is " + str(self.game.score))

    def fail(self):
      self.game.score.decrement()
      self.game.output("Incorrect the number was " + str(self.number) + " Your score at the end of the round is " + str(self.game.score)) 
    
    def outcome(self):
      self.success() if (self.game.levels.validateAnswer(self.answer)) else self.fail()
