class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def reverse(self):
        prev = None
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
llist = LinkedList() 
llist.push(20)
llist.push(4)
llist.push(15) 
llist.push(35)
llist.push(45)
#llist.printList()
llist.reverse()
llist.printList()