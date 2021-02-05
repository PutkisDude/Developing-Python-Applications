#author Lauri Putkonen
print("This program converts seconds to hours, minutes and seconds")
seconds = int(input("Type seconds: "))

hours = int(seconds / 3600)
minutes = int(seconds % 3600 / 60)
seconds_left = seconds % 3600 % 60

print("Hours", hours, "minutes", minutes, "seconds", seconds_left)
