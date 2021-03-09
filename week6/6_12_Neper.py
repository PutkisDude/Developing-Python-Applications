#Author Lauri Putkonen
# 12. Calculates an approximation of Neper's value (e).

import math

def neper(loopcount):
    neper = 0
    for i in range(loopcount):
        neper += 1/math.factorial(i)
    return neper


print(neper(333))

#Output: 2.7182818284590455
