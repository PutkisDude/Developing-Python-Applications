#Author Lauri Putkonen
# 4. Fill 2 arrays with some values and calculate the sum array.

array1 = [42, 49, 20, 40, 50, 23, 59]
array2 = [49, 15, 20, 30, 50, 90, 32, 68]
sum = 0

######################################################
# With 2 arrays

for x in array1:
    sum += x

for x in array2:
    sum += x
    
print("with 2 arrays", sum)

#Output: with 2 arrays 637

print()
#######################################################

# Sum indexes from both arrays to 3rd array and check that it won't go out of bounds
array3 = []
len1 = len(array1)
len2 = len(array2)


if len1 >= len2:
    for x in range(len2):
        array3.append(array1[x] + array2[x])
    for x in range(len2, len1):
        array3.append(array1[x])
else: 
    for x in range(len1):
        array3.append(array1[x] + array2[x])
    for x in range(len1, len2):
        array3.append(array2[x])

print("3rd array:", array3)

#OUPUT: 3rd array: [91, 64, 40, 70, 100, 113, 91, 68]

# Sum from 3rd array and print it

sum_array3 = 0
for x in array3:
    sum_array3 += x

print("3rd array:", sum_array3)

#OUTPUT: 3rd array: 637

print()
######################################################

# 2d array and sum from it

sum2 = 0
twodimensional_array = [[42, 49, 20, 40, 50, 23, 59], [49, 15, 20, 30, 50, 90, 32, 68]]

for x in range(len(twodimensional_array)):
    for j in range(len(twodimensional_array[x])):
        sum2 += twodimensional_array[x][j]

print("2d array:", sum2)


#OUTPUT: 2d array: 637
