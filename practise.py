# Removing consonants
sen = "My name is Chetan"

# to remove consonants and make a new list
def is_consonant(sen):
    vowels = 'aeiou'
    return sen.isalpha() and sen.lower() not in vowels

new = ''.join(i for i in sen if is_consonant(i))
print(new)


# Equality of lists
l1 = [3,1,2]
l2 = [1,3,2]
def check_equal(l1,l2):
    if len(l1) == len(l2):
        if sorted(l1) == sorted(l2):
            return 'Same'
    else:
        return "the number of elements aren't same in both lists"  
print(check_equal(l1,l2))

# Rotating matrix
mat = [[1,2,3],[4,5,6],[7,8,9]]


def rotate_matrix(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
    for row in arr:
        row.reverse()

print(mat)            
rotate_matrix(mat)
print(mat)