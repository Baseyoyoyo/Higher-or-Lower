import sqlite3
import datetime

class ScoreBoard(object):
  def __init__(self, database = "scores.db"):
    self.db = sqlite3.connect(database)
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

  def highest(self, limit = 10):
    return self.__rows__(limit).fetchall()

  def recent(self, limit = 10):
    return self.__rows__(limit, "recorded_at").fetchall()

  def count(self):
    return self.cursor.execute("SELECT COUNT(*) FROM scores").fetchone()[0]

  def clear(self):
    self.cursor.execute("DELETE FROM scores")
    return self.db.commit()

  def __rows__(self, limit = 10, sort_field = "score"):
    return self.cursor.execute(
      "SELECT name, score, recorded_at FROM scores ORDER BY " + sort_field + " DESC LIMIT ?", 
      (limit,)
    )