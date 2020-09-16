'''
Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      / \
  4     5   6    7
    \
     8

Below is the given tree

            10
         /     \
     20         30
   /      \      
40      60

Right View is: 10 30 60.

'''

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        
def rightViewUtil(root, level):
    global max_level
    
    if(root is None):
        return
    
    if(max_level < level):
        print(root.data)
        max_level = level
        
        
    rightViewUtil(root.right, level + 1)
    rightViewUtil(root.left, level + 1)
        
        
def rightView(root):
    global max_level
    max_level = 0
    rightViewUtil(root, 1)
    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
  
rightView(root)