my_list = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

# def first_second(my_list):
#     my_list.sort(reverse=True)
#     return tuple(my_list[:2])

def first_second(my_list):
    max1, max2 = 0, 0
    for i in my_list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i!=max1:
            max2 = i
    return max1,max2


print(first_second(my_list))