'''
https://www.youtube.com/watch?v=MRe3UsRadKw
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None 
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, data):
        temp = Node(data)
        temp.next  = self.head
        self.head = temp
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def reverse(self,item):
        if item.next == None:
            #print(item.data)
            #print(self.head.data)
            self.head = item
            return
        self.reverse(item.next)
        temp = item.next
        #print(temp.data)
        #print(item.data)
        temp.next = item
        item.next = None
            
mylist = LinkedList()
mylist.add(15)
mylist.add(20)
mylist.add(25)
mylist.add(30)
mylist.printList()
#print(mylist.head.data)
mylist.reverse(mylist.head)
        