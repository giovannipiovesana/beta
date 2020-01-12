# My Europe's travel diary

## Project overview

This project is a diary that travelers can use to note their journey in the european capitals.

## Europe's Capitals and States feature
The european continent has a lot of states, many of which is difficult to remember exactly the capital. This is why the ```main.py``` module comes in handy. It has a command which helps the user remember the capital given the state or viceversa. 

Two argparse command are used: *-state* followed by the state the user wants to know the capital and *-capital* followed by the capital the user wants to know the state.

Exaple commands: 
* INPUT: '''
$ python main.py -state Berlin 
'''
* OUTPUT: The European state whose capital is Berlin is Germany

* INPUT: $ python main.py -capital Italy
* OUTPUT: The capital of Italy is Rome

## Capitals and States input rules
All the 'Capital' and 'State' commands must be written with the first letter in uppercase and the rest lowercase, otherwise the code returns an error like this:
* OUTPUT: Sorry, germany does not seem to be an European state.
* OUTPPUT: Sorry, berlin is not the capital of any European state.

If a state or capital is composed by two separated words like Vatican City, the command must be written inside apostrophes, otherwise the name is not recognized.

Example of a right command:
* INPUT: $ python main.py -state 'Vatican City'
* OUTPUT: The European state whose capital is Vatican City is Vatican City

Example of a wrong command:
* INPUT: $ python main.py -state Vatican City
* OUTPUT: usage: main.py [-h] [-create CREATE] [-capital CAPITAL] [-state STATE]
                [-city CITY] [-note NOTE]
main.py: error: unrecognized arguments: City

## Capital notebook creation
The ```main.py``` module has a database feature used by the user as a travel notebook. The database can be erased or created (if not existing previously) with the following command:
* INPUT: $ python main.py -create True
* OUTPUT: The output the program should give back is the file ```capitals.csv``` printed row by row.

The table of the database is named capitals composed by three columns (_capital_id_, _state_id_, _note_id_). _capital_id_ and _state_id_ are taken from the _capital.csv_ file. _note_id_ is a empty row by default.

## Capital notebook editing
During the trip to a capital, the user can edit the content of _note_id_ entry of a _capital_id_ with a note (string) about that capital with two argparse commands: -city and -note. The commands are used as shown below:
* INPUT: $ python main.py -city Berlin -note 'Berlin has a nice weather'
* OUTPUT: ('Berlin', 'Berlin has a nice weather')

After inputting the name of the capital (same rules shown in _Capitals and States input rules_ apply), the user can insert a string which will override the _note_id_ entry of that capital everytime. The string after the command -note must be written inside apostrophes, otherwise the entry is not registered.

## Capital notebook checking
The user can easly check the note of a capital written before with the following example command:

* INPUT: $ python main.py -city Berlin
* OUTPUT: ('Berlin', 'Berlin has a nice weather')

Same rules shown in _Capitals and States input rules_ apply.

## Valid States/Capitals

All the valid inputs the user can choose can be found in _.csv_ file located in: ```data/capitals.csv```.

## Tests
*Tests* folder has the module ```test_capitals.py``` used to tests the module ```capital.py``` from *directory* folder with 3 different inputs.

* INPUT: $ python -m unittest -v -b tests/test_capitals.py
* OUTPUT:
test_cornercase (tests.test_capitals.TestTrue) ... ok
test_empty (tests.test_capitals.TestTrue) ... ok
test_invalid (tests.test_capitals.TestTrue) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

## Contributors

* Mattioli Luca
* Piovesana Giovanni Andrea
* Donadio Davide
* Zamperin Alberto

## License

MIT License

