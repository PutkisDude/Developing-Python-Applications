#Author Lauri Putkonen
#Program calculates the exponential value (base and exponent are given
# invariable). Base can be a real number, exponent is a whole number. Use a loop.


base = 5
exponent = 8
x = base

for i in range(1, exponent):
    x = base * x

print("{}^{} = {}".format(base, exponent, x))

#OUTPUT: 5^8 = 390625

