# This module uses argparse to get an input from user in order to get the desired output running check_capital or check_state.
import argparse
import sqlite3
import sys

import csv
from directory.capitals import check_capital
from directory.capitals import check_state

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

def db_edit():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('UPDATE capitals SET note_id= ? WHERE capital_id= ?', (args.been, args.city))
    conn.commit()
    conn.close()
    
def db_check():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT * FROM capitals WHERE capital_id= ?', (args.city,))
    print (cur.fetchone())
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', type=str,
                        help='erase existing and populate new db')
    parser.add_argument('--capital', type=str,
                        help='The name of the state')
    parser.add_argument('--state', type=str,
                        help='The name of the capital')
    parser.add_argument('--city', type=str,
                        help='The name of the capital')
    parser.add_argument('--been', type=str,
                        help='been')
    args = parser.parse_args()
    
    if args.create:
        db_create()
    if args.state:
        capital_checker = check_capital(args.state)
    if args.capital:
        state_checker = check_state(args.capital)
    if args.city:
        if args.been:
            db_edit()
        else:
            db_check()
     else: print ('ERROR BRO')
