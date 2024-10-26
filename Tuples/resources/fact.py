def fact(n):
    a = n + fact(n-1)
    return a

result = fact(5)
print(result)