import sqlite3


db = sqlite3.connect("scores.db")

cursor = db.cursor()

print ("If you wish to see the top scores from the past 10 days then please enter recent if you would like to see the all time high scores then please enter all.")

choice = raw_input ("")

sort_field = "recorded_at" if choice == "recent" else "score"

scores = cursor.execute(
  "SELECT name, score, recorded_at FROM scores ORDER BY " + sort_field + " DESC LIMIT ?", 
  (10,)
)

for score in scores.fetchall():
  print "player " + score[0] + " achieved a score of " + str(score[1]) + " at " + str(score[2])
