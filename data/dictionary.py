import csv
filename = 'data/capitals.csv'

reader = csv.reader(open(filename, 'r'))
list_of_capitals = {}
for row in reader:
    key, value = row
    list_of_capitals[key] = value

list_of_capitals
