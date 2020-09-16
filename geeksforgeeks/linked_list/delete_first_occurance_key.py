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
        
    def deleteNode(self, key):
        temp = self.head
        
        if(self.head.data == key):
            self.head = temp.next
            temp = None
            
        # 1 2 3 4 5
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
            
        prev.next = temp.next
        temp = None
        
        if (temp == None):
            print("Key is not Present!!!")
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
            
            
if __name__ == '__main__':
    
    llist = SinglyLinkedList() 
    
    llist.insertAtFront(7) 
    llist.insertAtFront(1) 
    llist.insertAtFront(3) 
    llist.insertAtFront(2) 
      
    print("Created Linked List: ")
    llist.printList() 
    llist.deleteNode(7)  
    print ("\nLinked List after Deletion of 1:")
    llist.printList() 
    
    
                