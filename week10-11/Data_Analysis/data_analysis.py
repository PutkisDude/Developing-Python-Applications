# Author Lauri Putkonen
# Read and code data analysis example from document
# DA_python_example.docx
# Show at least 1 chart that illustrates results.
# Bonus:
# Create you own data analysis example using pandas and numpy.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


data = pd.read_csv("electric_usage.csv")

# Different to previous month

df_consum = pd.DataFrame.diff(data["kWh"])
data["Different"] = df_consum

# print
print(data[["Vuosi", "Kuukausi", "kWh", "Different"]])




# Matplotlib Figure
time = []
for x in range(len(data["Vuosi"])):
               time.append(str(data["Vuosi"][x]) + " - " + str(data["Kuukausi"][x]))
               
plt.figure(figsize=(15,8))
plt.barh(time, data["kWh"])
plt.xlabel("Electricity consumption(kWh)")
plt.show()
