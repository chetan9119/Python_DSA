import numpy as np

# 1. creating two dimentional array
print("Creating array practise :") 
twoDArray = np.array([[12,8,6,11],[4,9,12,14],[13,5,3,9],[10,5,14,8]])
print(twoDArray)

## Inserting elemnts into two D array for rows and columns
newTwoDArrayCol = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0) # row
newTwoDArrayRow = np.insert(twoDArray, 0, [[70,80,99,90]], axis=1) # columns
# print(newTwoDArrayCol)
# print(newTwoDArrayRow)
## using append method
# newTwoDArrayColApnd = np.append(twoDArray, [[33,44,55,66]], axis=0) # rows
# print(newTwoDArrayColApnd)


# 2. Accessing elements from two dimentional array
# print(len(twoDArray[0])) and print(len(twoDArray)) == 4
print("Access elements practise: ")
def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Incoorect Index")
    else:
        print(array[rowIndex][columnIndex])
# accessElements(twoDArray, 1,2)

# 3. Traversing two dimentional array
print("Traversing practise :")
def traverseArray(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            print(array[row][col])
# traverseArray(twoDArray) 

# 4. Searching through the element
print("Searching Element :")
# Using linear search
def searchTDArray(array, target): 
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == target:
                print(f"The targeted value {target} at index : ({row}, {col})")
    else:
        return "The element not found"
# print(searchTDArray(twoDArray, 5))
        
# 5. Searching through the element
print("Deleteing the col or row in two dimentional array :")

# for rows deletion
newTDArrayrow = np.delete(twoDArray, 0, axis=0)
print(newTDArrayrow)     

# for columns deletion        
newTDArraycol = np.delete(twoDArray, 2, axis=1)
print(newTDArraycol)       
        
        
        
        
        
        
        
        
        
        
        
        
        