class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self)->str:
        tempnode = self.head
        result = ''
        while tempnode is not None:
            result += str(tempnode.value)
            if tempnode.next is not None:
                result += ' -> '
            tempnode = tempnode.next
        return result
        
    def __iter__(self):
        node = self.head
        while node is None:
            print(node.value)
            node = node.next
    
    # Inserting at the end of SLL if elements are there in SLL.    
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
    
    # Inserting elements at begining of SLL with two condition    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, value, index):
        
        new_node = Node(value)
        
        if index < 0 or index > self.length:
            return False
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            
        else:    
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length += 1
        
    def traverse(self):
        if self.head is None:
            print("Empty SLL")
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index < 0 and index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail =None
        else:    
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
        
    
                
sampleLL = LinkedList()
sampleLL.append(25)
sampleLL.append(41)
sampleLL.append(58)
sampleLL.prepend(99)
sampleLL.insert(114, 1)
print(sampleLL.length)

# First node
print(sampleLL.head.value)
print(sampleLL.head.next.value)

# Last Node
print(sampleLL.tail.value)
print(sampleLL.tail.next)
print(sampleLL)

# Search
print(sampleLL.search(41))

# get operation returning a node itself as object
print(sampleLL.get(4))
print(sampleLL)
print(sampleLL.set(1,115))
print(sampleLL)
print(sampleLL.pop_first())
print(sampleLL)
print(sampleLL.pop())
print(sampleLL)