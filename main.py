# This module uses argparse to get an input from user in order to get the desired output running check_capital or check_state.
import argparse
import csv
from directory.capitals import check_capital
from directory.capitals import check_state
import sqlite3
import sys

data ='directory/capitals.csv'

# This function creates two sets from the csv file in order to whitelist user inputs
def parse_allowed_input(datafile=data):
    states = set()
    capitals = set()
    with open(datafile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            states.add(row[0])
            capitals.add(row[1])
    return states, capitals

# This function parses the user inputs.
def parse_arguments(states, capitals):
    parser = argparse.ArgumentParser()
    parser.add_argument('-capital', type=str,
                        help='The name of the state', choices=states)
    parser.add_argument('-state', type=str,
                        help='The name of the capital', choices=capitals)
    parser.add_argument('-city', type=str,
                        help='The name of the capital', choices=capitals)
    parser.add_argument('-been', type=str,
                        help='The name of the capital')
    parser.add_argument('-check', type=str,
                        help='The name of the capital', choices=capitals)
    args = parser.parse_args()
    return args

def db_edit():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()
    
    capital = args.capital
    note = args.been

    cur.execute('UPDATE capitals SET note_id= ? WHERE capital_id= ?', (note, capital))
    conn.commit()

def db_check():
    capitale = args.check
    conn = sqlite3.connect('capitals.sqlite')
  
    cur = conn.cursor()
    cur.execute('SELECT * FROM capitals WHERE capital_id= ?', (capitale,))
    print (cur.fetchone())
    
if __name__ == '__main__':
    states, capitals = parse_allowed_input()
    args = parse_arguments(states, capitals)
    if args.capital and args.been:
        db_edit(args.capital, args.been)
        
    #if args.state:
     #   capital_checker = check_capital(args.state)
   # else: 
    #    state_checker = check_state(args.capital)'''
