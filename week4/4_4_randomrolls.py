#Author Lauri Putkonen
#Program throws dice 100 times and tells amounts of different values (1, 2, 3, 4,
#5, and 6).

from random import randint

rolls = [0, 0, 0, 0, 0, 0]

for i in range(1, 101):
    roll = randint(0,5)
    rolls[roll] += 1

print("Amount of values between 1 and 6:")
print(rolls)

