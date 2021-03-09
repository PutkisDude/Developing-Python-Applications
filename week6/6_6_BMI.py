#Author Lauri Putkonen
#6. Returns the BMI.

def bmi(weight, height):
    height = height / 100
    bmi = weight / (height * height)
    return bmi

weight = float(input("Type your weight(kg) : "))
height = float(input("Type height (cm): "))

print("Your BMI is %.2f" % bmi(weight, height))

#OUTPUT:
# Type your weight(kg) : 90
# Type height (cm): 180
# Your BMI is 27.78
