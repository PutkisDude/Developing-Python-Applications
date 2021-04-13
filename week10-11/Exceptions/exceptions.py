#Author Lauri Putkonen
# Use the file "countries.txt".
# Catch min 2 differenr exceptions when reading or writing to the file.

from datetime import datetime

try:
    file = open("countries.txt", "r")
#    file.write("error")

except FileNotFoundError:
    print("No such file")


except ValueError:
    print("You dont't have permission to  write to the file")

# 2.
# Catch min 2 different exception when user gives a year number.
# Give proper messages to the user.

class TooHighOrLow(Exception):
    pass
    
year_now = datetime.now().year

try:
    year = int(input("Give year: "))
    if year > year_now or year < 0:
        raise TooHighOrLow

except ValueError: #When value is something else than integer
    print("Write only whole numbers")

except TooHighOrLow: # When value is less than 0 or higher than current year
    print("Type value between 0 and current year")



