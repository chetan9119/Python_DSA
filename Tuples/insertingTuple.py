input_tuple = (2, 3, 4)
value_to_insert = 1

# Refined solution
def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

# def insert_value_front(input_tuple, value_to_insert):
#     temp_list = list(input_tuple)
#     temp_list.append(value_to_insert)
#     return tuple(sorted(temp_list))

output_tuple = insert_value_at_beginning(input_tuple, value_to_insert)
print(output_tuple)