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

### Whats New?

The user can now choose to view the recent scores or the top high scores by just opening `scores.py`

The scores now descend from the largest amount of points downwards to smallest amount of points.

If the guess was incorrect then the their score will decrease by 1 point rather than ending the game all together.

### How To Run

Type into console `python higher_or_lower.py` and hit enter
the program should now automatically run.