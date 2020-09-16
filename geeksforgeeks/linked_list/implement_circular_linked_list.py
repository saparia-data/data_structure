class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertAtFront(self, data):
        new_node = Node(data)
        
        if(self.head == None):
            self.head = self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
            
    
    def insertAtMiddle(self, prev_node, data):
        new_node = Node(data)
        
        prev_node.next = new_node
        new_node.next = prev_node.next
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        new_node.next = self.tail.next
        self.tail = new_node
        
    def printData(self):
        
        temp = self.head
        
        while(True):
            print(temp.data)
            temp = temp.next
            if(temp.next != self.head):
                break
        
if __name__ == '__main__':
    
    clist = CircularLinkedList()
    clist.insertAtFront(1);
    clist.insertAtFront(2);
    clist.printData()
        
            