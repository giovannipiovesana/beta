# This module uses argparse to get an input from user in order to get the desired output running check_capital or check_state.
import argparse
import csv
from Week_2.capitals import check_capital
from Week_2.capitals import check_state

data ='Week_3/capitals.csv'

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
    args = parser.parse_args()
    return args

# This function runs the check_capital and check_state function with the user input.
if __name__ == '__main__':
    states, capitals = parse_allowed_input()
    args = parse_arguments(states, capitals)
    if args.state:
        capital_checker = check_capital(args.state)
    else: 
        state_checker = check_state(args.capital)
