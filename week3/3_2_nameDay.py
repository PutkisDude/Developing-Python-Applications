#Author Lauri Putkonen
#User enters a weekday number and the program tells the name of the day.

import calendar

day = int(input("Number of the day: ")) -1

print(calendar.day_name[day])

# Could also make a list and print from it but there is inbuilt module in python to do same thing
# weekdays = ["Monday", "Tuedsday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day = int(input("Number of the day ")) -1
# print(weekdays[day])

#OUTPUT EXAMLE:

#Number of the day: 3
#Wednesday
