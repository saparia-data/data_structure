'''
Given a Linked List Representation of Complete Binary Tree. The task is to construct the Binary tree.
Note : The complete binary tree is represented as a linked list in a way where if root node is stored at position i, its left, 
and right children are stored at position 2*i+1, 2*i+2 respectively.
 
Given tree is 
                            1
                         /   \
                       2      3
                     /   \
                   4      5
Now, the level order traversal of the above tree is 1 2 3 4 5.
'''
class ListNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Conversion:
    
    def __init__(self, data = None):
        
        self.head = None
        self.root = None
        
    def push(self, new_data):
        
        node = ListNode(new_data)
        node.next = self.head
        self.head = node
        
    def convertList2Binary(self):
        
        q = []
        
        if(self.head is None):
            self.head = None
            self.root = None
            
        self.root = BinaryTreeNode(self.head.data)
        
        q.append(self.root)
        
        self.head = self.head.next
        
        while(self.head):
            
            parent = q.pop(0)
            
            leftChild = None
            rightChild = None
            
            leftChild = BinaryTreeNode(self.head.data)
            q.append(leftChild)
            self.head = self.head.next
            
            if(self.head):
                rightChild = BinaryTreeNode(self.head.data)
                q.append(rightChild)
                self.head = self.head.next
                
            parent.left = leftChild
            parent.right = rightChild
            
    def inOrderTraversal(self, root):
        
        if(root is None):
            return
        
        self.inOrderTraversal(root.left)
        print(root.data, end = " ")
        self.inOrderTraversal(root.right)
            
conv = Conversion() 
conv.push(36) 
conv.push(30) 
conv.push(25) 
conv.push(15) 
conv.push(12) 
conv.push(10)

conv.convertList2Binary()
conv.inOrderTraversal(conv.root)
            
        