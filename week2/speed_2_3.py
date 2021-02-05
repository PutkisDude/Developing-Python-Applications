#Author Lauri Putkonen
speed = int(input("Give speed of car(km/h): "))
distance = int(input("Give distance(km): "))

time_in_hours = round((distance / speed), 2)
minutes = int(distance % speed)
hours = int(distance / speed)

print("Driving takes", time_in_hours, "in hours")
print("Driving takes ", hours, " hours ", minutes, " and minutes.")
