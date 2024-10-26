# Creating a tuple...
newTuple0 = ('a',)
print(newTuple0)

newTuple1 = ('a','b','c','d','e')
print(newTuple1)

newTuple3 = tuple('abcde')
print(newTuple3)


# Accessing elements of tuples
print(newTuple1[0])

# Using slicing
print(newTuple1[1:4:2])

# Traversing through elements
for i in newTuple1:
    print(i)
    
# Traversing through indexes
for i in range(len(newTuple1)):
    print(newTuple1[i])    
    
# Search for an element
print(newTuple1.index("a"))

# Traversing through index() and passing the value to 'i'
for i in newTuple1:
    print(newTuple1.index(i))

def searchTuple(tup, element):
    for i in range(len(tup)):
        if tup[i] == element:
            return f"The element found at {i} index"
    else:
        return "Element doen't exists"   
print(searchTuple(newTuple1, 'c'))


# Tuple operations and executions
numTup = (1,4,3,2,5,1)
numTup2 = (1,2,6,9,8,7)

# Concatenate two tuples
print(numTup+numTup2)

# The multiply operator will repeat the value certain times as follows
print(numTup * 3)

# Element exists or not
print(1 in numTup)

# Method for counting elements
print(numTup.count(1))

# index() method
print(numTup.index(3))

# len() functions
print(len(numTup))
print(len(numTup2))

# max and min
print(max(numTup))
print(min(numTup2))


# Operations on List ( Lists VS Tuples)

list1 = [0,1,2,3,4,5,6]
print(list1)

# Re assign
list1[1] = 0
print(list1)

# deleting list
del list1[0]
print(list1)


# Fuctions common in both
myTuple = (0,1,2,3,4,5,6)
print("Here are the fuctions of tuples")
print(len(myTuple))
print(sum(myTuple))
print(max(myTuple))
print(min(myTuple))
print(any(myTuple))
print(all(myTuple))
print(sorted(myTuple))


# Methods used in tuples
myTpl = (0,1,2,3,4,5,6,0)
print(myTpl.count(0))
print(myTpl.index(4))

# Nested creation of using both inside each other
myList = [(1,2),(3,4),(5,6)]
myTup = ([1,2],[3,4],[5,6])

print(myList)
print(myTup)