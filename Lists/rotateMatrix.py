matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(matrix):
    n = len(matrix)
    
    for i in range(n): # Iterate over the rows
        for j in range(i, n): # Iterate over columns starting from current 'i'
            # Swap the elements at positions from (i,j) and (j,i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()
        
print(matrix)        
rotate(matrix)
print(matrix)    