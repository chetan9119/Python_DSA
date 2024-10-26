arr = [11,22,345,76,99]

sum = 0
for index, value in enumerate(arr):
    print(f"The index is {index} and value is {value}")
    print(arr[index])
    sum += arr[index]

print(sum)