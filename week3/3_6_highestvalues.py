#Author Lauri Putkonen
#Variables a, b and c have different values. Create a program that finds the
#biggest one.
#Show 3 different ways to solve the problem.

a = 4
b = 2
c = 0
print("variables a, b, c with values {}, {}, {}".format(a,b,c))

# simple MAX function with variables

print("max function:")

highest = max(a, b, c)
print(highest)

print()

# Sorted List
print("list -> sort -> print last index from list:")
list = [a, b, c]
list.sort()
print(list[len(list) -1])

print()
# dictionary with max function
print("Dictionary with keys and max function:")
dict = {}
for var in ["a", "b", "c"]:
    dict[var] = eval(var)

print("Highest value is in variable", max(dict, key=dict.get), "and value is", max(dict.values()))

print()

# NESTED IF ELSE
print("Bad and messy nested if else:")

if a == b == c:
    print("All variables are equals with value %d" % a)
elif a >= b and a >= c:
    if a > b and a > c:
        print("Variable a has highest value(%d)" % a)
    elif a > c:
        print("a({}) and b({}) are equals".format(a, b))
    elif a == c and a > b:
        print("a({}) and c({}) are equals".format(a, c))
elif b >= c:
    if b > a and b > c:
        print("Variable b has highest value(%d)" % b)
    elif b > a:
        print("b({}) and c({}) are equals".format(b, c))
else:
    print("Variable c has highest value(%d)" % c)



#EXAMPLE OUTPUT

#variables a, b, c with values 4, 2, 0
#max function:
#4
#
#list -> sort -> print last index from list:
#4
#
#Dictionary with keys and max function:
#Highest value is in variable a and value is 4
#
#Bad and messy nested if else:
#Variable a has highest value(4)
