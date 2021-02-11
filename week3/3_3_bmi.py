#Author Lauri Putkonen
#Program calculates BMI and gives also a textual description.
height = int(input("Height(cm): "))
weight = float(input("Weight(kg): "))

height /= 100

bmi = round((weight / (height * height)), 2)
print("")

if bmi < 18.5 :
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Your weight is normal")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
else :
    print("You are obese")

print("Your BMI is", bmi, "\n")
print("Underweight = <18.5\n"
      "Normal weight = 18.5 - 24.9\n"
      "Overweight = 25-29.9\n"
      "Obesity = 30 or higher\n"
      "PS. Don't take BMI too seriously!")

#I made this last week already with textual descriptions

#OUTPUT EXAMPLE:

#Height(cm): 180
#Weight(kg): 90

#You are overweight
#Your BMI is 27.78 

#Underweight = <18.5
#Normal weight = 18.5 - 24.9
#Overweight = 25-29.9
#Obesity = 30 or higher
#PS. Don't take BMI too seriously!
