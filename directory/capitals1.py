import csv
file = 'capitals.csv'

list_of_capitals = {}
with open(file) as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    try:
        for row in reader:
            list_of_capitals[row[0]] = row[1]
    except IndexError:
        pass

print (list_of_capitals)

def check_capital(state_name):
    '''It returns the capital of the correspondent state if it
       is present in the list.'''

    if state_name in list_of_capitals:
        print ('The capital of {} is {}'.format(state_name,
                                                list_of_capitals[state_name]))
    else:
        print ('Sorry, {} does not seem to be an European state'
               .format(state_name))


def check_state(capital_name):
    '''It returns the state of the correspondent capital if it
    is present in the list.'''

    for (state, capital) in list_of_capitals.items():
        if capital == capital_name:
            print ('The European state whose capital is {} is {}'
                   .format(capital_name, state))
            return
    print ('Sorry, {} is not the capital of any European state'
           .format(capital_name))
