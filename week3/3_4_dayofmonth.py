#Author Lauri Putkonen
#User gives a month number and our program tells the number of days in that month

import calendar
import datetime
now = datetime.datetime.now()
month = int(input("Number of the month: "))
print("Amount of days in the month", calendar.monthrange(now.year, month)[1])

# datetime-module gives current year for calendar and calendar gives days in month
# works with leap year too

#OUTPUT EXAMPLE:

# Number of the month: 2
# Amount of days in the month 28
