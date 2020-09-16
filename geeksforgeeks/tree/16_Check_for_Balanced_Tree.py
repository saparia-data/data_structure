'''
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5

The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
The max difference in height of left subtree and right subtree is 1. Hence balanced.

https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

'''
class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
def height(root):
    
    if(root is None):
        return 0
    
    return 1 + max(height(root.left), height(root.right))

# O(n2) time complexity
def isBalanced(root):
    
    if(root is None):
        return True
    
    lh = height(root.left)
    rh = height(root.right)
    
    if(abs(lh - rh) <= 1 and isBalanced(root.left) is True and isBalanced(root.right) is True):
        return True
    
    return False

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(8)

print(isBalanced(root))