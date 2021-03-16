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
