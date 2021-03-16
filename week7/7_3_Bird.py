#AUTHOR Lauri Putkonen
# 3. Bird has features name and amount of eggs.
# Amount of eggs has to be between 1 and 10.
# Migratory has special features: there is attribute named country that is the
# destination country and month when the migration mainly occurs.

# Country name has to begin with a cap and its length has to be between
# 5 to 20. Month has to be between 1 and 12.

import calendar


class Bird:
    def __init__(self, name, eggs):
        if eggs < 1 or eggs > 10:
            raise ValueError("Bad value")
        else:
            self.name = name
            self.eggs = eggs
            print(self.name, "has", eggs, "egg(s).")

    def migratory(self, country, month):

        if month < 1 or month > 12:
            raise ValueError("Month's value can only be 1-12")
        elif len(country) < 5 or len(country) > 20:
            raise ValueError("Country name is too short or long")
        else:
            self.country = country.capitalize()
            self.month = calendar.month_name[month]
            self.flying()


    def flying(self):
        print(self.name, "is flying to", self.country, "in", self.month)
              

seagull = Bird("Steven Seagull", 5)
seagull.migratory("finland", 12)

print()

flappy = Bird("Flap", 10)
flappy.migratory("USA", 3) 

#OUTPUT:

# Steven Seagull has 5 egg(s).
# Steven Seagull is flying to Finland in December

# Flap has 10 egg(s).
# Traceback (most recent call last): .... ValueError: Country name is too short or long

#########################################################################################

#I reverse engineered this file to .dot file with pyreverse and turned it to .png with graphviz for bonus task.

#Terminal commands for it on Ubuntu:
# Sudo apt install pylint graphviz
# pyreverse ./7_3_Bird.py
# dot -Tpng classes.dot > bird.png

##########

# I found multiple UML tools for python with fast google search but I didn't have much time to try them.
# I tried only dia2code:
# sudo apt install dia2code to terminal
# I made testUML.dia with it
# dia2code -t python testUML.dia to terminal to make code from UML .dia file 

#########3

# Pylint can use to detect errors and check if code is standard based too.

# pylint 7_3_Bird.py -- OUTPUT:

#************* Module 7_3_Bird
#7_3_Bird.py:36:0: C0303: Trailing whitespace (trailing-whitespace)
#7_3_Bird.py:44:26: C0303: Trailing whitespace (trailing-whitespace)
#7_3_Bird.py:56:0: C0301: Line too long (112/100) (line-too-long)
#7_3_Bird.py:64:0: C0305: Trailing newlines (trailing-newlines)
#7_3_Bird.py:1:0: C0103: Module name "7_3_Bird" doesn't conform to snake_case naming style (invalid-name)
#7_3_Bird.py:1:0: C0114: Missing module docstring (missing-module-docstring)
#7_3_Bird.py:13:0: C0115: Missing class docstring (missing-class-docstring)
#7_3_Bird.py:15:8: R1720: Unnecessary "else" after "raise" (no-else-raise)
#7_3_Bird.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
#7_3_Bird.py:24:8: R1720: Unnecessary "elif" after "raise" (no-else-raise)
#7_3_Bird.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
#7_3_Bird.py:29:12: W0201: Attribute 'country' defined outside __init__ (attribute-defined-outside-init)
#7_3_Bird.py:30:12: W0201: Attribute 'month' defined outside __init__ (attribute-defined-outside-init)
#7_3_Bird.py:38:0: C0103: Constant name "seagull" doesn't conform to UPPER_CASE naming style (invalid-name)
#7_3_Bird.py:43:0: C0103: Constant name "flappy" doesn't conform to UPPER_CASE naming style (invalid-name)

#------------------------------------------------------------------
#Your code has been rated at 3.48/10 (previous run: 4.35/10, -0.87)

