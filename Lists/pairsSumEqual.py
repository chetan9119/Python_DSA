def pair_sum(arr, sum):
    index = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                index.append(f"{arr[i]}+{arr[j]}")
    return index   
            
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))