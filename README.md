# Game.py
## Python based command line maths game


### What is the purpose of this command line maths game?

This command line game was originally created as part of a school project.
The purpose of the game is that the computer randomly generates a number and then 
asks the user to input either l or h to symbolise weather the next randomly produced
number will be either higher or lower than the previously number. The computer will 
then reveal the second number and tell the user if their guess was correct or incorrect.
if the guess was correct then the computer will move onto the next stage keeping track
of the players score. If the guess was incorrect then the their score will decrease by 1 point. On each level that they get correct the numbers will increase making 
the range larger and the chance of guessing incorrectly larger as well.
The score is now displayed on the screen after every turn taken so you can keep track of your score.
At the end of the game you can view previous players scores and compare them to your score.

### Whats New?

The `scores.py` file now automatically runs so at the end of the game it asks the user if they would like to view the High Scores.

### How To Run

Type into console `python -m game.py` and hit enter
the program should now automatically run.

### Tests

The core classes that form the game are tested with Python's unittest. Tests can be found in the [tests directory](tests/).

To easily run the tests, I've included a bash script. From the root of the project, use `./test` and the all tests will be run.