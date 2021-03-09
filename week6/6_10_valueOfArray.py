#Author Lauri Putkonen
#10. Searches for a value from an array.

def valueOf(arr, index):
    value = arr[index]
    return value

array = ["this", "is", "the", "array", "value"]

print(valueOf(array, 2))
print(valueOf(array, 4))
    
#OUTPUT:
# the
# value
