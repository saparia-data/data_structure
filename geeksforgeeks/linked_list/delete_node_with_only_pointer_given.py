'''
Given only a pointer to a node to be deleted in a singly linked list

https://www.geeksforgeeks.org/in-a-linked-list-given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/
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
            
    def deleteNode(self, node_ptr):
        temp = node_ptr.next
        node_ptr.data = temp.data
        node_ptr.next = temp.next
        
        '''
        node_ptr.data = node_ptr.next.data
        node_ptr.next = node_ptr.next.next
        '''
        
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.printList()
print("Linked list after removing a node")
llist.deleteNode(llist.head.next.next)
llist.printList()