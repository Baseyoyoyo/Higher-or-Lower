import sqlite3
import datetime

class ScoreBoard(object):
  def __init__(self):
    self.db = sqlite3.connect("scores.db")
    self.cursor = self.db.cursor()

    self.ensureTable()

  def ensureTable(self):
    self.cursor.execute("CREATE TABLE IF NOT EXISTS scores(id INTEGER PRIMARY KEY, name TEXT, score INTEGER, recorded_at DATETIME)")

  def recordedAt(self):
    return datetime.datetime.now() 
  
  def add(self, name, score):
    self.cursor.execute(
      "INSERT INTO scores(name, score, recorded_at) VALUES(?,?,?)", 
      (name, score, self.recordedAt())
    )

    self.db.commit()

score = ScoreBoard()
score.add("Harvey", 3)
