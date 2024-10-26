def sum_product(input_tuple):
    sums = 0
    prod = 1
    for num in range(len(input_tuple)):
        sums += input_tuple[num]
        prod *= input_tuple[num]
    return sums,prod

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result) 