#Author Lauri Putkonen
#2. Returns the average of 4 floating point values.

#takes unlimited amount arguments
def average_of_four(*values):
    sum_of_values = sum(values)
    avg = sum_of_values / len(values)
    return round(avg, 2)

print(average_of_four(5, 3, 5.5, 6))

#OUTPUT: 4.88
