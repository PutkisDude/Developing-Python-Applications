#Author Lauri Putkonen
# task 4.8
# Program calculates the factorial of n (given in a variable)

factorial = 1
n = 10

if(n == 0):
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial *= i

print("{}!".format(n), "=", factorial)

#OUPUT: 10! = 3628800
