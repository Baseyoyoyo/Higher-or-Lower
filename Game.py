# Simple CLI based game for guessing a number being higher or lower
# Requires Python > 3
# `python higher_or_lower.py`
from classes.score_board import ScoreBoard
from classes.player_score import PlayerScore
from classes.levels import Levels
from classes.game_controller import GameController

score_board = ScoreBoard()
score = PlayerScore()
levels = Levels(15)

game = GameController(score_board, score, levels)

game.welcomeMessage()
game.getName()
game.runLevels()
game.complete()