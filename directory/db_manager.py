'''This module populates a database named capitals.sqlite with capitals.csv
through an iteration cycle. capital_id and state_id entries are filled with
the capitals and states found on the .csv.
'''
import argparse
import sqlite3
import sys
import csv


def db_create():
    '''This function creates a new table named capitals or rewrites it from
    scratch if it is already there with three entries: capital_id, state_id
    and note_id.'''
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS capitals')
    cur.execute('''
    CREATE TABLE "capitals"(
    "capital_id" TEXT,
    "state_id" TEXT,
    "note_id" TEXT)''')

    with open('data/capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print (row)
            capital_id = row[0]
            state_id = row[1]
            cur.execute('''INSERT INTO capitals(
            capital_id, state_id) VALUES (?, ?)''',
                        (capital_id, state_id))
            conn.commit()
