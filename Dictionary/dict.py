# creating dictionary using HASH tables
my_dict = dict()
print(my_dict)

eng_span = {
    "one":"uno",
    "two":"dos",
    "three":"tres"
}

eng_span_bydict = dict(one='uno',two='dos',three='tres')

print(eng_span)
print(eng_span_bydict)


# creating dict and tuples
eng_dict_list = [('one','uno'),('two','dos'),('three','tres')]
tupToDict = dict(eng_span_bydict)
print(tupToDict)


new_dict = {"name":"Chetan","age":31}
print(new_dict)
new_dict["age"] = 32
print(new_dict)

# Adding new element in dictionary
new_dict["Company"] = "Google"
print(new_dict)


# traversing element
def traverse_dict(dict):
    for key in dict:
        print(key, dict[key])

traverse_dict(new_dict)


# Search element
myDict = {'name':'Chetan', 'age':31, 'Company':'google'}

def search_dict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    else:
        return f"{value} doesn't exist"
        
print(search_dict(myDict, 31))
        

# Deleting elements
emp_dict = {'name':'Chetan','age':31, 'address':'Bhopal', 'education':'Bechlors'}


cp_dict = emp_dict.copy()
print(cp_dict)

# Using del 
del emp_dict['age']
print(emp_dict)

# Using pop(key, defaultValue)
removed_element = emp_dict.pop('address', None)
# Using popitem() last item from the dictionary
removed_element = emp_dict.popitem()
print(removed_element)
print(emp_dict)

# clear dict delete all the value from dict
emp_dict.clear()
print(emp_dict)

# using fromkeys method
randonDict = {}.fromkeys([1,2,3,4,5], "chetan")
print(randonDict)

# using get()
print(randonDict.get(5, "Answer"))

# if key isn't available in dictionary then returning the default value
print(randonDict.get(6, "Answer"))


# items() - It'll give the key, Value pair in tuple (key, Value) 
print(randonDict.items())

# keys()
print(randonDict.keys())

# values()
print(randonDict.values())

# setdefault
randonDict.setdefault(6, "New")
print(randonDict)

# update
randAdd = {"this": "add"}
randonDict.update(randAdd)
print(randonDict)



# Check dictionary
check_dict = {
    9:'Nine',
    6:'Six',
    10:'Ten',
    7:'Seven',
    4:'four'
}
for key in check_dict:
    print(key, check_dict[key])

print(10 in check_dict)
print('Six' in check_dict.values())
print('Two' not in check_dict.values())
print(len(check_dict))
print(all(check_dict))
print(any(check_dict))
print(sorted(check_dict))