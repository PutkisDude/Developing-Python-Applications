#Author Lauri Putkonen
#9. Calculates the standard deviation.

import statistics

def devition(arr):
    return statistics.stdev(arr)

array = [52, 62, 13, 44, 5]
print("%.4f" % devition(array))

#OUTPUT: 24.9139
