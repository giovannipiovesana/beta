def load_csv():

    '''loads file passed as filename (path of the file) and
    returns a dictionary. intended for loading csv files'''

    list_of_capitals = {}
    with open('directory/capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            for row in reader:
                list_of_capitals[row[0]] = row[1]
        except IndexError:
            pass

    return list_of_capitals
