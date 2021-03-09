#Author Lauri Putkonen
#4. Returns the factorial.

def factorial(num):
    result = 1
    for x in range(1, num+1):
        result *= x
    return result

print(factorial(6))

#OUTPUT: 720
