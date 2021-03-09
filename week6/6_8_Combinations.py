#Author Lauri Putkonen
#8. Calculates amount of combinations
# (try to use also an own factorial function here)


def factorial(num):
    result = 1
    for x in range(1, num+1):
        result *= x
    return result

array = [40, 50, 20, 60, 50, 90, 59, 20, 666]


print("There is {} combinations with {} different values".format(factorial(len(array)), len(array)))

#OUTPUT:
#There is 362880 combinations with 9 different values
