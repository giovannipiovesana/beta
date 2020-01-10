def load_csv(filename):

    '''loads file passed as filename (path of the file) and
    returns a dictionary. intended for loading csv files'''

    list_of_capitals = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        try:
            for row in reader:
                list_of_capitals[row[0]] = row[1]
        except IndexError:
            pass

    return list_of_capitals
