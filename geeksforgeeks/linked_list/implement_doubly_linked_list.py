class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertAtFront(self, data):
        
        new_node = Node(data)
        
        new_node.next = self.head
        
        if(self.head is not None):
            self.head.prev = new_node
            
        self.head = new_node
        
    def insertAtMiddle(self, prev_node, data):
        if prev_node is None: 
            print("the given previous node cannot be NULL")
            return 
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        
        if(new_node.next is not None):
            new_node.next.prev = new_node
            
    def insertAtEnd(self, data):
        
        new_node = Node(data)
        
        new_node.next = None
        
        if(self.head is None):
            new_node.prev = None
            self.head = new_node
            return
        
        temp = self.head
        
        while(temp.next is not None):
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        
        return
    
    def printData(self):
        first = self.head
        print("Nodes in forward Direction")
        while(first):
            print(first.data, end=" ")
            last = first
            first = first.next
              
        print("\nNodes in reverse Direction")   
        while(last):
            print(last.data, end=" ")
            last = last.prev
            
if __name__ == '__main__':
    
    dlist = DoublyLinkedList()
    
    dlist.insertAtEnd(1)
    dlist.insertAtFront(2)
    dlist.insertAtFront(3)
    dlist.insertAtEnd(4)
    dlist.insertAtMiddle(dlist.head.next.next, 5)
    dlist.printData()
        
        
        
        
        