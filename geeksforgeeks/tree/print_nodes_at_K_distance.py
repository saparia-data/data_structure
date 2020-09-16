'''
Nodes at distance k from the root are basically the nodes at (k+1)th level of the Binary Tree.

https://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/

'''
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def printKDistant(root, k):
    
    if(root is None):
        return
    
    if(k == 0):
        print(root.data)
        
    else:
        printKDistant(root.left, k - 1)
        printKDistant(root.right, k - 1)
        
# Driver program to test above function 
""" 
   Constructed binary tree is 
            1 
          /   \ 
        2      3 
      /  \    / 
    4     5  8  
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(8) 
  
printKDistant(root, 2)