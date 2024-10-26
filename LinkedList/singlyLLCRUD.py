class Node:  
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class SinglyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def inser_SLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
                
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    def traverse_SLL(self):
        if self.head is None:
            print("The Single Linked Lists doesn't exists")
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
            
    def search_SLL(self, element):
        if self.node is None:
            print("The SLL doesn't exists")
        else:
            node = self.head
            while self.head is not None:
                if node.value == element:
                    return node.value
                else:
                    return "Element doesn't exists"
                
    def delete_SLL(self, location):
        if self.head is None:
            return "The SLL doesn't exists"
        else:
            self.head = None
            self.tail = None