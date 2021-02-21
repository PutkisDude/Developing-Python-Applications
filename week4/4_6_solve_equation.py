#Author Lauri Putkonen
#Try to solve this equation (try find 1 of roots)
#3x^3 - 4x^2 + 9x +5 = 0
#Here ^ means exponent


x = -10000.0
increase = 999.0
result = 3 * x ** 3 - 4 * x ** 2 + 9 * x + 5

tries = 0

while result != 0:

    temp_x = x + increase
    result = 3 * temp_x ** 3 - 4 * temp_x ** 2 + 9 * temp_x + 5
    if result > 0:
        increase *= 0.1
    else:
        x = temp_x

    if result == 0.0:
        x = "{:.7f}".format(x)
        print("X =", x)
