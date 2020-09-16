class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAtMiddle(self, prev_node, data):
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if(self.head == None):
            self.head = new_node
            return
        
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        
    def printData(self):
        
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
        
if __name__=='__main__':
    
    llist = SinglyLinkedList()
    llist.insertAtEnd(6)
    llist.insertAtFront(7);
    llist.insertAtFront(1);
    llist.insertAtEnd(4)
    llist.insertAtMiddle(llist.head.next, 8) 
    llist.printData()
    
            
            