# Author Lauri Putkonen
#Read a file that has countries and populations (name can be "countries.txt").

import re

file = "countries.txt"
with open (file) as file_obj:
    lines = file_obj.readlines()

print(lines[0])

# Output:
#  China,1407271880


#Remove possible whitespaces.

stripped = []
for line in lines:
    line = line.strip()
    stripped.append(line)

#Search for the population of some given country.

country = "Finland"
for line in stripped:
    if re.search(country, line, re.IGNORECASE):
        print(line)
        print(line.partition(",")[2]) #population without country name

#OUTPUT:
#Finland,5508198
#5508198
#Åland Islands (Finland),30152
#30152

print()
#Print the country that has the biggest population.
highest = ""
index = 0
for line in stripped:
    if (line.partition(",")[2]) > highest:
        highest = line
    
print("The highest population: ", highest.partition(",")[0])
file_obj.close()

#OUTPUT:
#The highest population:  China

#Add more countries and populations to the file.

with open(file, "a") as file_append:
    file_append.write("Fakelandia, 50420\n")
    file_append.write("Mumbojambo, 2500\n")

file_append.close()
