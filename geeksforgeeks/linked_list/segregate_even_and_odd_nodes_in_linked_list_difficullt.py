'''
Given a Linked List of integers, write a function to modify the linked list such that all even numbers appear before all the odd numbers in the modified linked list. 
Also, keep the order of even and odd numbers same.

https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

'''
class Node: 
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
            
    def segregateEvenOdd(self):
      
        # Starting node of list having  
        # even values. 
        evenStart = None
          
        # Ending node of even values list. 
        evenEnd = None
          
        # Starting node of odd values list. 
        oddStart = None
          
        # Ending node of odd values list. 
        oddEnd = None
          
        # Node to traverse the list. 
        currNode = self.head 
          
        while(currNode != None): 
            val = currNode.data 
              
            # If current value is even, add 
            # it to even values list. 
            if(val % 2 == 0): 
                if(evenStart == None): 
                    evenStart = currNode 
                    evenEnd = evenStart 
                else: 
                    evenEnd.next = currNode 
                    evenEnd = evenEnd.next
              
            # If current value is odd, add  
            # it to odd values list. 
            else: 
                if(oddStart == None): 
                    oddStart = currNode 
                    oddEnd = oddStart 
                else: 
                    oddEnd.next = currNode 
                    oddEnd = oddEnd.next
                      
            # Move head pointer one step in  
            # forward direction 
            currNode = currNode.next 
          
        # If either odd list or even list is empty, 
        # no change is required as all elements  
        # are either even or odd. 
        if(oddStart == None or evenStart == None): 
            return
          
        # Add odd list after even list.      
        evenEnd.next = oddStart 
        oddEnd.next = None
          
        # Modify head pointer to  
        # starting of even list. 
        self.head = evenStart 
        
llist = LinkedList()
llist.push(11)
llist.push(10)
llist.push(9)
llist.push(6)
llist.push(4)
llist.push(1)
llist.push(0)
llist.printList()
llist.segregateEvenOdd()
print("Linked list after re-arranging")
llist.printList()