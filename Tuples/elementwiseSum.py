tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# def tuple_elementwise_sum(t1, t2):
#     if len(t1) != len(t2):
#         raise ValueError("Input tuples must have the same length.")
#     result = tuple(a + b for a, b in zip(t1, t2))
#     return result

# Using map fuction and zip
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple) 