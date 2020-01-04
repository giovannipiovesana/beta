#This module populates a database named capitals
import sqlite3
import csv 
def db_create():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS capitals')
    cur.execute('''
    CREATE TABLE "capitals"(
    "capital_id" TEXT,
    "state_id" TEXT,
    "note_id" TEXT)''')
    
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
