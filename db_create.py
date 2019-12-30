#This module populates a database named capitals
import sqlite3
import csv 

conn = sqlite3.connect('capitals.sqlite')
cur = conn.cursor()

#this function creates a table or rewrites it from scratch it it's already there
cur.execute('DROP TABLE capitals')
cur.execute('''
CREATE TABLE "capitals"(
"capital_id" TEXT,
"state_id" TEXT,
"note_id" TEXT)''')

#This function uses the csv file to populate the database with capital_id and state_id entries
with open('directory/capitals.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        capital_id=row[0]
        state_id=row[1]
        cur.execute('''INSERT INTO capitals(
        capital_id, state_id) VALUES (?,?)''',
                    (capital_id, state_id))
        conn.commit()
        
conn.close()
