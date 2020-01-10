def load_csv():

    '''loads file passed as filename (path of the file) and
    returns a dictionary. intended for loading csv files'''

    list_of_capitals = {}
    with open('directory/capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print (row)
            capital_id = row[0]
            state_id = row[1]) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        try:
            for row in reader:
                list_of_capitals[row[0]] = row[1]
        except IndexError:
            pass

    return list_of_capitals

print (list_of_capitals)
