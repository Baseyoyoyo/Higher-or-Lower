import random

GuessesTaken = 0

print ("Hello and welcome to my higher or lower number guessing game.")
print ("Whats your name?")
myName = input()

number = random.randint(1, 20)
number1 = random.randint(1, 20)
number2 = random.randint(1, 20)
number3 = random.randint(1, 20)
number4 = random.randint(1, 20)
number5 = random.randint(1, 20)
number6 = random.randint(1, 20)
number7 = random.randint(1, 20)
number8 = random.randint(1, 20)
number9 = random.randint(1, 20)
number10 = random.randint(1, 20)
number11 = random.randint(1, 20)
number12 = random.randint(1, 20)
number13 = random.randint(1, 20)
number14 = random.randint(1, 20)
number15 = random.randint(1, 20)
number16 = random.randint(1, 20)
number17 = random.randint(1, 20)
number18 = random.randint(1, 20)
number19 = random.randint(1, 20)
number20 = random.randint(1, 20)

print ("So, your names " + myName + " Hmmmmmmm")
print ("Ok " + myName + " here is your first number")
print ("")
print (number)
print ("")
print ("Also keep in mind that the numbers range from 1 to 20")
print ("")
print ("So will the next number be higher or lower?")
print ("")
print ("")
print ("Use h to guess Higher and use l to guess Lower.")

guess = input('Enter either h or l:    ')

if number > number1 and guess == "l":
    print ("Well done the number was " + number1 + " Now onto stage 2")
elif number > number1 and guess == "h":
    print ("Incorrect the number was " + number1 + "GAME OVER")
elif number < number1 and guess == "h":
    print ("Well done the number was " + number1 + " Now onto stage 2")
elif number < number1 and guess == "l":
    print ("Incorrect the number was " + number1 + " GAME OVER")