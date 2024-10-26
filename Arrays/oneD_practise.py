# importing array from python core library
from array import *

# 1. Creating array and traversing it
print("Step - 1")
my_array = array('i', [1,2,3,4,5])
for element in my_array:
    print(element)  # TC - O(N)
    
    
# 2. Accessing elements through indexes
print("Step - 2")
for index in range(len(my_array)):
    print(my_array[index]) # TC -O(N)

# 3. Adding element to the array
print("Step - 3")
my_array.append(7) # It'll always append to end of the array
print(my_array)  

# 4. Inserting value in array  
print("Step - 4")
my_array.insert(5,6) # inserting at a given position of array
print(my_array)

# 5. Extend array 
print("Step - 5")
new_array = array('i', [8,9,10])
my_array.extend(new_array)
print(my_array)

# 6. Add item from list into array using fromlist()
print("Step - 6")
tempList = [11,12,13,14,15]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove elements from the array using remove()
print("Step - 7")
my_array.remove(13)
print(my_array)

# 8 Remove last element using pop()
print("Step - 8")
print(my_array.index(15))
#my_array.pop() # remove last element
my_array.pop(13) # remove element using index
print(my_array)

# 9. Fetch element using index
print("Step - 9")
print(my_array.index(10))

# 10. Reversing the array using reverse()
print("Step - 10")
my_array.reverse()
print(my_array)

# 11. Getting array buffer information thorough buffer_function()
print("Step - 11")
print(my_array.buffer_info())

# 12. count method
print("Step - 12")
my_array.append(14)
print(my_array.count(14))

# 13. Convert array into string
print("Step - 13")
string = my_array.tobytes()
print(string) 

# 14. Convert array to a python list
print("Step - 14")
print(my_array.tolist())

# 15. Convert string to array
print("Step - 15")
intsArray = array('i')
intsArray.frombytes(string)
print(intsArray)

# 16. Slicing of array
print("Step - 16")
print(my_array[::-1])