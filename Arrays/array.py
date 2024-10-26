import numpy as np
new_array = np.array([1,2,3,4,5])
print(new_array)

import array
my_array = array.array('i', [1,2,3,4])
my_array.insert(4,5)
print("Successfully inserted element '5' at position/Index 4")

# Array traversal
def traverseArray(array):
    for element in array:
        print(f'Traversal Function Output: {element}')
# Using traversal function       
traverseArray(my_array)

# Access elements using index
def accessElement(array, index):
    if index >= len(array):
        print("Invalid Index")
    else:
        print(f'Access Element Function Output: {array[index]}')
# Using access function
accessElement(my_array, 4) # Expected output is '5'


# Using linear search algo to find the element
def linear_search(array, target):
    # if target not in array:
    #     print("Targeted value doesn't exists in array")
    for index in range(len(array)):
        if array[index] == target:
            return f"Targeted value is at index: {index}" 
    return -1    
print(linear_search(my_array, 5))


# Removing element
my_array.remove(5)
print("Element '5' is removed from the array !")
print(my_array)