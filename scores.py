import sqlite3

db = sqlite3.connect("scores.db")

cursor = db.cursor()

scores = cursor.execute("""
  select name, score, recorded_at from scores order by score desc;
""").fetchall()

for score in scores:
  print "player " + score[0] + " achieved a score of " + str(score[1]) + " at " + str(score[2])
