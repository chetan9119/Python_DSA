# Accessing and Travesring the list
shoppingList = ['Milk','Cheese','Butter'] 

# Accesing element
print(shoppingList[2])

# Exists or not check
print('Milk' in shoppingList) # boolean check
print('Bread' in shoppingList) # boolean check

# Reversing list
print(shoppingList[-1]) # reverse value

## traverse
# for elements in shoppingList:
#     print(elements)

# Traversing and creating    
for index in range(len(shoppingList)):
    shoppingList[index] += " NEWS"
    print(shoppingList[index]) 


# # Calculating average
# total = []    
# while True:    
#     value = input("Enter No. :")
#     if value == 'done': break
#     total.append(int(value))
#     average = sum(total)/len(total)
# print(average)


# String and lists
a = "chetan,kumar,parashar"
b = a.split(",")
print(b)

print(" ".join(b))

# append and sort() / sorted()
a = [2,1,9,3,4]

a += [10]
print(a)

b = a[:]

#a.sort()
c= a.sort()
#c = sorted(a)
print(a)
print(b)
print(c)

# List comprehension
item = [1,2,3,4,5,6]
new_cube = [i*i*i for i in item]
print(new_cube)

# List comprehension using condition
nums = [-1,10,-20,2,-90,60,45,20]
new_list = [i for i in nums if i > 0]
print(new_list)

# Check consonants from string
sentence = "This is Chetan Parshar, I am an aspiring Software programmer"

def check_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
cons_list = [i for i in sentence if check_consonant(i)]

print(cons_list)

# Putting fuction in list comprehension
prev_list = [-1,10,-20,2,-90,60,45,20]

def check_num(number):
    return number if number > 0 else 'negative'

new_num_list = [check_num(i) for i in prev_list]
print(new_num_list)


cp_list = [1,2,3,4,5]
cp_list1 = cp_list # This is assigment operator
cp_list2 = cp_list[:] # This is copy operator

cp_list1[0] = 99
cp_list2[1] = 999

print(cp_list)
print(cp_list1)
print(cp_list2)