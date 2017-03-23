"""
This first exercise will cover `if` statements.
"""


# python 2 / 3 compatibility stuff here -- ignore these next 4 lines
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass


"""
The objective of this first assignment is to add an if/else block which does the following:

  - if `number` is less than 100, print out "<number goes here> is a small number"
  - otherwise, print "<number goes here> is a HUGE number!"
"""

number = input('Give me a number:')  # this will prompt the user to enter text in the command line and hit enter.
number = int(number)  # since `input(...)` returns whatever you type in as a string, we need to tell python to treat it as an integer.

print("I don't do anything fancy just yet, but your number is", number)
