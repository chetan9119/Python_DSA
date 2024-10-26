import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# Linear search
def findNumber(arr, number):
    
    for i in range(len(arr)):
        
        if arr[i] == number:
            return i
    
    else:
        return -1
          
index = findNumber(myArray, 21)

print(index)