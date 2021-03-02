#AUTHOR LAURI PUTKONEN
# 1. Array contains 30 random values. Calculate the sum and average.

import random
import numpy as np

random_array = []
sum = 0
for x in range(30):
    random_array.append(random.randint(1,100))
    sum += random_array[x]

print("sum is", sum)
print("avg: %.2f" % (sum / len(random_array)))

#Same with Numpy
print("numpy sum:", np.sum(random_array))
print("numpy avg: %.2f" % np.average(random_array))


print()
#OUTPUT:
#sum is 1162
#avg: 38.73


##################################################################


# 2. Find the maximun of an array.

print("max value is", max(random_array))
print()

#OUTPUT: max value is 94

##################################################################

# 3. Search a value from an array.

search_value = 59
if search_value in random_array:
    print("Array index of value", search_value, "is",random_array.index(search_value))
else:
    print("Value",search_value, "is not in array")

# .index search only first value, with numpy can search multiple indexes with same value
arr = np.array(random_array)
print(np.argwhere(arr == 59))

#OUTPUT:
#Array index of value '59' is 10
#OR Value 59 is not in array

