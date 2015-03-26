# Simple CLI based game for guessing a number being higher or lower
# Requires Python > 3
# `python higher_or_lower.py`
import random
from classes.score_board import ScoreBoard
from classes.player_score import PlayerScore
from classes.levels import Levels

score_board = ScoreBoard()

print ("Hello and welcome to my higher or lower number guessing game.")

name = raw_input("Whats your name? ")

print ("So, your names " + name + " Hmmmmmmm")

score = PlayerScore()
count = 1
previousNumber = random.randrange(1, count*20)

levels = Levels(15)

for number in levels:
 
  print ("\nKeep in mind that the numbers range from 1 to " + str(count * 20))

  print ("\n\nYour number is " + str(previousNumber) + ". So will the next number be higher or lower?")

  guess = raw_input("\n\nEnter either h or l: ")

  if (previousNumber > number and guess == "l") or (number > previousNumber and guess == "h"):
    score.increment()

    print ("Well done the number was " + str(number) + " Your score at the end of the round is " + str(score))

  else:

    score.decrement()

    print ("Incorrect the number was " + str(number) + " Your score at the end of the round is " + str(score))

    
  previousNumber = number
  count = count + 1
  

score_board.add(name, score.value)
print ("Well done your score is " + str(score) + " Good Job")

execfile("scores.py")

