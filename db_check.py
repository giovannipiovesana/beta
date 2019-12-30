# This module shows the row of a given capital. (Useful to check if the note got updated or not)
import sqlite3
import sys
capital = sys.argv[1]

conn = sqlite3.connect('capitals.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM capitals WHERE capital_id= ?', (capital,))
print (cur.fetchone())
