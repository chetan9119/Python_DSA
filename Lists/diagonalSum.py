myList2D= [[1,2,3],[4,5,6],[7,8,9]]

def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
    return total
print(diagonal_sum(myList2D))

# def diagonal_sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if i == j:
#                 sum += arr[i][j]
#     return sum
# print(diagonal_sum(myList2D))