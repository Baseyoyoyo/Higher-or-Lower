# Simple CLI based game for guessing a number being higher or lower
# Requires Python > 3
# `python higher_or_lower.py`

import random

print ("Test")

print ("Hello and welcome to my higher or lower number guessing game.")

myName = raw_input("Whats your name? ")

print ("So, your names " + myName + " Hmmmmmmm")

score = 0
count = 1
previousNumber = random.randrange(1, count*20)


while 1:
 
  print ("\nKeep in mind that the numbers range from 1 to " + str(count * 20))

  print ("\n\nYour number is " + str(previousNumber) + ". So will the next number be higher or lower?")

  number = random.randrange(1, count*20)

  guess = raw_input("\n\nEnter either h or l: ")

  if (previousNumber > number and guess == "l") or (number > previousNumber and guess == "h"):
    score = score + 1

    print ("Well done the number was " + str(number) + " Your score at the end of the round is " + str(score))

  else:

    if score > 0:
      score = score - 1

    print ("Incorrect the number was " + str(number) + " Your score at the end of the round is " + str(score))

    
  previousNumber = number
  count = count + 1
  

print ("Well done your score is " + str(score) + " Good Job")