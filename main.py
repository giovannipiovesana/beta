# This module uses argparse to get an input from user in order to get the desired output running check_capital or check_state.
import argparse
import sqlite3
import sys

from directory.capitals import check_capital
from directory.capitals import check_state
from directory.db_manager import db_create


def db_edit():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('UPDATE capitals SET note_id= ? WHERE capital_id= ?',
                (args.note, args.city))
    conn.commit()
    conn.close()


def db_check():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT capital_id, note_id FROM capitals
                WHERE capital_id= ?', (args.city, ))
    print cur.fetchone()
    conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', type=bool,
                        help='erase existing and populate new db')
    parser.add_argument('--capital', type=str,
                        help='The name of the capital')
    parser.add_argument('--state', type=str,
                        help='The name of the state')
    parser.add_argument('--city', type=str,
                        help='The name of the capital')
    parser.add_argument('--note', type=str, help='Add some travel notes'
                        )
    args = parser.parse_args()

    if args.create:
        db_create()
    if args.state:
        capital_checker = check_capital(args.state)
    if args.capital:
        state_checker = check_state(args.capital)
    if args.city:
        if args.note:
            db_edit()
            db_check()
        else:
            db_check()
