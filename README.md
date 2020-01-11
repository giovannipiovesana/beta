# My Europe's travel diary

## Project overview

This project is diary a that a traveler can use to note their journey in the european capitals.

## Europe's Capitals and States feature
The european continent has a lot of states, many of which is difficult to remember exactly the capital. This is why the ```main.py``` module comes in handy. It has a command which helps the user remember the capital of a given the state or viceversa. Two argparse command -state and -capital give back the user 

Exaple commands: 
* INPUT: $ python main.py -state Berlin 
* OUTPUT: 'The European state whose capital is Berlin is Germany'

* INPUT: $ python main.py -capital Italy
* OUTPUT: 'The capital of Italy is Rome'

* N.B: All the 'Capital' and 'State' commands must be written with the first letter in uppercase and the rest lowercase, otherwise the code returns an error like this:
*-Sorry, germany does not seem to be an European state.
*-Sorry, berlin is not the capital of any European state.


## Capital notebook functionality
The program contains also a database which can be used by the user as a travel notebook. It 
*Week_3* Adds the ```capitals.csv``` file that makes ```main.py``` module work. It returns to the user the name of the state given the capital or viceversa. 
* An example of output can be: "The European state whose capital is 'Capital' is 'State'." 


## Valid States/Capitals

All the valid inputs the user can choose can be found in _.csv_ file located in: ```Week_3/capitals.csv```.

## Week_4
*Week_4* is composed by three modules that performs the following tasks (before using the following commands it's mandatory to _cd_ to the folder *Week_4*!):

* ```db_create.py```: this module populates a database with a table named capitals composed by three columns (_capital_id_, _state_id_, _note_id_). _capital_id_ and _state_id_ are taken from the _capital.csv_ file. _note_id_ is a empty row by default.
* Command: $ python db_create.py

* ```db_edit.py```: this module edit the content of _note_id_ entry. After inputting the name of the capital (written with the first letter in uppercase and the rest lowercase), the user can insert a word which will override the _note_id_ entry of the Capital.
* Example command:  $ python db_edit.py Berlin Been

* ```db_check.py```: this module checks the content of the row of the capital selected (written with the first letter in uppercase and the rest lowercase).
* Example command: $ python db_check.py Berlin

## Tests
*Tests* folder has the module ```test_capitals.py``` used to tests the module ```capital.py``` from *directory* folder with 3 different inputs.

* Command: $ python -m unittest -v -b Week_5/test_capitals.py

## Contributors

* Mattioli Luca
* Piovesana Giovanni Andrea
* Donadio Davide
* Zamperin Alberto

## License

MIT License

