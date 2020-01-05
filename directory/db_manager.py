'''This module populates a database named capitals.sqlite.
'''
import argparse
import sqlite3
import sys
import csv

'''This function creates a table named capitals or rewrites it from 
scratch if it is already there with three entries: capital_id, state_id
and notes_id.
'''
def db_create():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS capitals')
    cur.execute('''
    CREATE TABLE "capitals"(
    "capital_id" TEXT,
    "state_id" TEXT,
    "note_id" TEXT)''')

'''This iteration cycle populates the database with capital_id and 
state_id entries from the capital.csv file.
'''
    with open('directory/capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print (row)
            capital_id = row[0]
            state_id = row[1]
            cur.execute('''INSERT INTO capitals(
            capital_id, state_id) VALUES (?, ?)''',
                        (capital_id, state_id))
            conn.commit()
