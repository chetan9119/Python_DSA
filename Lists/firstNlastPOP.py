myList = [1, 2, 3,7 ,5,6,8,9,4]

def middle(arr):
    return arr[1:-1]

# def middle(arr):
#     arr.pop(0)
#     arr.pop(len(arr)-1)
#     return arr
        
print(middle(myList))