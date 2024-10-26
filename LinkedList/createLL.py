class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
       
# Creating a linked list with a single element
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
            
# # Creating an empty linked list
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
sampleLL = LinkedList(15)
print(sampleLL)
print(sampleLL.head.value)
print(sampleLL.tail.value)
print(sampleLL.length)
