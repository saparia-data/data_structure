'''
Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.
For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.


              1
            /   \
          2      3
        /  \
      4     5
     /
    7

https://www.geeksforgeeks.org/print-ancestors-of-a-given-node-in-binary-tree/

https://www.youtube.com/watch?v=qjD-CmuC0MQ

'''

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
        
def printAncestors(root, target):
    
    if(root is None):
        return False
    
    if(root.data == target):
        return True
    
    if(printAncestors(root.left, target) or printAncestors(root.right, target)):
        print(root.data)
        return True
    
    return False

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(7) 
  
printAncestors(root, 7) 
