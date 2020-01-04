# This module uses argparse to get an input from user in order to get the desired output running check_capital or check_state.
import argparse
import sqlite3
import sys

data ='directory/capitals.csv'

# This function parses the user inputs.
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-city', type=str,
                        help='The name of the capital')
    parser.add_argument('-been', type=str,
                        help='been')
    parser.add_argument('-check', type=str,
                        help='The name of the capital')
    args = parser.parse_args()
    return args

def db_edit():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()
    
    capital = args.city
    note = args.been

    cur.execute('UPDATE capitals SET note_id= ? WHERE capital_id= ?', (note, capital))
    conn.commit()
    
if __name__ == '__main__':
    print(args.city)
    #db_edit(args.city, args.been)
