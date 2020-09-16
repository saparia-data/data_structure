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
        
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        
        if(self.head is not None):
            while(fast_ptr is not None and fast_ptr.next is not None):
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            print(slow_ptr.data)
    
llist1 = LinkedList()
llist1.push(1) 
llist1.push(2) 
llist1.push(3) 
llist1.push(4) 
llist1.push(5)
llist1.push(6)
#llist1.printList()  
llist1.printMiddle()      
        
        