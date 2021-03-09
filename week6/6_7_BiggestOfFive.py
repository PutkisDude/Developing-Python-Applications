#AUTHOR Lauri Putkonen
#7. Function returns the biggest of 5 integers.

def theBiggest(*nums):
    array = nums
    return max(array)

print(theBiggest(3, 4, 5, 6, 8))

#OUTPUT: 8

# I use same answer than in task 5, since it takes unlimited amount arguments
