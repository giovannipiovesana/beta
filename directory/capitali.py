import csv
filename = 'directory/capitals.csv'

def load_csv(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        list_of_capitals = dict(reader)
    return list_of_capitals
