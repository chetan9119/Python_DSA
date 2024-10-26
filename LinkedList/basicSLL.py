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
          node.next
    
# initializing nodes and singly linked lists        
singlelinkdlst = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)

# Assigning head to node1 and next of head to node2 and tail to node2
singlelinkdlst.head = node1
singlelinkdlst.head.next = node2
singlelinkdlst.tail = node2