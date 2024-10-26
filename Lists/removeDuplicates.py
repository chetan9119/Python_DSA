def remove_duplicates(lst):
    unique_lst = []
    # using set as a checker
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))





# def remove_duplicates(arr):
#     arr_new = []
#     for i in arr:
#         if i not in arr_new:
#             arr_new.append(i)
#     return arr_new



