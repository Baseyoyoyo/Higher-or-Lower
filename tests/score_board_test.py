import unittest
import datetime
from classes.score_board import ScoreBoard

class DateTimeStub(object):
  def now(self):
    return "test_date_time"

class ScoreBoardTest(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(ScoreBoardTest, self).__init__(*args, **kwargs)
    
    self.score_board = ScoreBoard("testdatabase.py")

  def seedScores(self):
    self.score_board.clear()

    dummy_scores = [
      ("player1", 5, datetime.datetime.now() - datetime.timedelta(days=3)),
      ("player2", 6, datetime.datetime.now()),
      ("player3", 3, datetime.datetime.now() - datetime.timedelta(days=2))
    ]

    self.score_board.cursor.executemany(
      "INSERT INTO scores(name, score, recorded_at) VALUES(?,?,?)",
      dummy_scores
    )

    self.score_board.db.commit()

  def testRecorderAt(self):
    self.assertEqual(type(self.score_board.recordedAt()), datetime.datetime)

  def testCount(self):
    self.seedScores()

    self.assertEqual(self.score_board.count(), 3)

  def testClear(self):
    self.seedScores()

    self.score_board.clear()

    self.assertEqual(self.score_board.count(), 0)

  def testAdd(self):
    self.seedScores()

    self.score_board.add("player4", 15)

    self.assertEqual(self.score_board.count(), 4)

  def testHighest(self):
    self.seedScores()

    scores = self.score_board.highest()

    self.assertEqual(scores[0][0], "player2")
    self.assertEqual(scores[2][0], "player3")

  def testRecent(self):
    self.seedScores()

    scores = self.score_board.recent()

    self.assertEqual(scores[0][0], "player2")
    self.assertEqual(scores[2][0], "player1")