def max_product(arr):
    max1, max2 = 0, 0
    
    for element in arr:
        
        if element > max1:
            max2 = max1
            max1 = element
            
        elif element > max2:
            max2 = element
        
    return max1 * max2


# # Using sort(reverse=True) for des order
# def max_product(arr):
#     arr.sort(reverse=True)
#     return arr[0] * arr[1]


arr = [1, 7, 3, 4, 9, 5]

print(max_product(arr))