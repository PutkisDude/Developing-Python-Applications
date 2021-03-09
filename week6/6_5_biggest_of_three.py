#AUTHOR Lauri Putkonen
#5. Returns the biggest of 3 integers.

def theBiggest(*nums):
    array = nums
    return max(array)

print(theBiggest(3, 4, 5, 6, 8))

#OUTPUT: 8
