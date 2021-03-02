#AUTHOR LAURI PUTKONEN
# 6. Take a look at python.org site. Array methods are presented here:
# https://docs.python.org/3/tutorial/datastructures.html
# Give your own examples of using those metods.

array = ["this", "is", "array"]
print(array)

#OUPUT: ['this', 'is', 'array']

#############################################

#Append - add item to end of the list

array.append("example")

print(array)

#OUTPUT: ['this', 'is', 'array', 'example']

#############################################

#Extend - add values from another array to array

array2 = ["and", "this", "is", "extended"]
array.extend(array2)
             
print(array)

#Output: ['this', 'is', 'array', 'example', 'and', 'this', 'is', 'extended']


#############################################

#Insert - insert value to given position

array.insert(2, "the")
print(array)

#OUPUT: ['this', 'is', 'the', 'array', 'example', 'and', 'this', 'is', 'extended']

##############################################

# Remove - Removes item from array with selected value

array.remove("example")
print(array)

#OUPUT: ['this', 'is', 'the', 'array', 'and', 'this', 'is', 'extended']

##############################################

# Pop - Removes value from selected index or last item from list if there isn't parameters

array.pop(2)
array.pop()
print(array)

#OUTPUT: ['this', 'is', 'array', 'and', 'this', 'is']

#############################################

# Clear- Clear all data from array

array.clear()
print(array)

#OUTPUT: []

#############################################

# Index - Search value from array and return index of it.

array = ["This", "is", "array", "example", "array"]
print("Index:", array.index("array"))
print("Next index", array.index("array", 3))

#OUTPUT: Index: 2
#Next index 4
#############################################

# Count - Count amount of the value in array

print("\"Array\" string is", array.count("array"), "times in array")

#OUTPUT: "Array" string is 2 times in array

#############################################

# Sort - Change order of the values.

array.sort()
print(array) #Alphabetical order
array.sort(reverse=True) #Reversed order
print(array)

#OUTPUT: ['This', 'array', 'array', 'example', 'is']
# ['is', 'example', 'array', 'array', 'This']

#############################################

# Copy - Copy array to another

copy_array = array.copy()
print(copy_array)

#OUTPUT: ['is', 'example', 'array', 'array', 'This']
