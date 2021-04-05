#Author Lauri Putkonen
#Open this place
#https://python-graph-gallery.com/
#Present min 5 different chart types using your own data.
#Add there chart figure and code.

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import random

# My grades
grades = [3, 1, 4, 4, 5, 5, 5, 4, 5]

grade_values = (0, 1, 2, 3, 4, 5)
# Count amounts
grade_amount = []

# Count amount of each grades
for x in grade_values:
    grade_amount.append(grades.count(x))

# Another tuplet for grades
another = (1,0,2,2,5,2)

# Plot chart

plt.figure(0)
plt.style.use("seaborn-darkgrid")
plt.plot(grade_values, another, label="Another grade tuplet", marker=".")
plt.plot(grade_values, grade_amount, label="My grades", marker=".")
plt.title("School grades")
plt.xlabel("Grades")
plt.ylabel("Amount of the grade")
plt.savefig("grade_fig.png") 

plt.legend()

# Bar figure
plt.figure(1).gca().yaxis.set_major_locator(MaxNLocator(integer=True))

plt.bar(grade_values, grade_amount)
plt.style.use("seaborn-talk")
plt.title("My Grades")
plt.savefig("grade_bar.png") 


# Pie figure
plt.figure(2)
plt.pie(grade_amount, labels=grade_values)
plt.title("The pie chart")
plt.savefig("grade_pie.png") 


# Scatter
arr = [random.random() for i in range(10)]
arr2 = [random.random() for i in range(10)]

plt.figure(3)
plt.subplot(1,2, 1)

plt.title("The scatter plot")
plt.scatter(arr, arr2, marker="+")


# Fill
plt.subplot(1,2,2)
plt.title("Fill")
plt.fill(arr, arr2)
plt.savefig("scatter_fill.png") 

plt.show()

print(plt.style.available)
