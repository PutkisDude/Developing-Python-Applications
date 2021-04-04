#Author Lauri Putkonen
#Open this place
#https://python-graph-gallery.com/
#Present min 5 different chart types using your own data.
#Add there chart figure and code.

import matplotlib.pyplot as plt

# My grades
grades = [3, 1, 4, 4, 5, 5, 5, 4, 5]

grade_values = (0, 1, 2, 3, 4, 5)
# Count amounts
grades_for_graph = []

for x in grade_values:
    grades_for_graph.append(grades.count(x))


fig, ax = plt.plot(grade_values, grades_for_graph, 1)

# plt.pie(grades_for_graph)
plt.show()
