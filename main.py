'''This module imports modules from directory folder in order to get the
check_capital function, the check_state function and the db_create function.
'''
import argparse
import sqlite3
import sys

from directory.capitals import check_capital
from directory.capitals import check_state
from directory.db_manager import db_create


def db_edit():
    ''' This function edit the content of note of a the chosen capital.'''
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('UPDATE capitals SET note_id= ? WHERE capital_id= ?',
                (args.note, args.city))
    conn.commit()
    conn.close()


def db_check():
    ''' This function shows the note of a given capital.
    It is useful to check if the note entry got updated or not.'''
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT capital_id, note_id FROM capitals WHERE capital_id= ?',
                (args.city, ))
    print (cur.fetchone())
    conn.close()


def parse_arguments():
    ''' Parse user inputs:
        -create: Erase existing database and populate new database if
        it is followed by True.
        -capital: Return capital given the STATE.
        -state: Return state given the CAPITAL.
        -city: Select the CAPITAL in the database.
        -note: Edit NOTE column of a CAPITAL in the database.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-create', type=bool,
                        help='Erase database and populate new if True')
    parser.add_argument('-capital', type=str,
                        help='State can be choosen from capitals.csv')
    parser.add_argument('-state', type=str,
                        help='Capital can be choosen from capitals.csv')
    parser.add_argument('-city', type=str,
                        help='Capital can be choosen from capitals.csv')
    parser.add_argument('-note', type=str,
                        help='The string must be inside apostrophes')
    args = parser.parse_args()
    return args

args = parse_arguments()

if __name__ == '__main__':
    args = parse_arguments()
    if args.create:
        db_create()
    if args.capital:
        capital_checker = check_capital(args.capital)
    if args.state:
        state_checker = check_state(args.state)
    if args.city:
        if args.note:
            db_edit()
            db_check()
        else:
            db_check()
