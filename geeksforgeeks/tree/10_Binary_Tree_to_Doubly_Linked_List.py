'''
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous 
and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, DLL would be 40<=>20<=>60<=>10<=>30.

hint:

-The idea is to do inorder traversal of the binary tree. While doing inorder traversal, keep track of the previously visited node in a variable say prev. 
-For every visited node, make it next of prev and previous of this node as prev.

'''

class Node:
        
    def __init__(self,data):    
        self.data = data;    
        self.left = None;    
        self.right = None; 
        
class BinaryTreeToDLL:
     
    def __init__(self):    
        #Represent the root of binary tree    
        self.root = None;    
        #Represent the head and tail of the doubly linked list    
        self.head = None;    
        self.tail = None;
        
    def convertbtToDLL(self, node):
        
        if(node is None):
            return
        
        self.convertbtToDLL(node.left)
        
        if(self.head is None):
            self.head = self.tail = node
            
        else:
            
            self.tail.right = node
            node.left = self.tail
            self.tail = node
            
        self.convertbtToDLL(node.right);
        
    def display(self):
        
        if(self.head is None):
            return "List is empty"
        
        else:
            curr = self.head
            while(curr):
                print(curr.data, end = " ")
                curr = curr.right
                
bt = BinaryTreeToDLL();    
#Add nodes to the binary tree    
bt.root = Node(1);    
bt.root.left = Node(2);    
bt.root.right = Node(3);    
bt.root.left.left = Node(4);    
bt.root.left.right = Node(5);    
bt.root.right.left = Node(6);    
bt.root.right.right = Node(7);    
     
#Converts the given binary tree to doubly linked list    
bt.convertbtToDLL(bt.root);    
     
#Displays the nodes present in the list    
bt.display();
            
            
        
        
        