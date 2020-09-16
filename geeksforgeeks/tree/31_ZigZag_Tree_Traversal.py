'''
Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

https://www.geeksforgeeks.org/zigzag-tree-traversal/

https://www.youtube.com/watch?v=YsLko6sSKh8

'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def spiralTreeTraversal(root):
    s1 = []
    s2 = []
    
    if(root is None):
        return
    
    s1.append(root)
    
    while(len(s1) or len(s2)):
        
        while(len(s1)):
            
            temp = s1.pop()
            print(temp.data, end = " ")
            
            if(temp.left is not None):
                s2.append(temp.left)
                
            if(temp.right is not None):
                s2.append(temp.right)
            
                
        while(len(s2)):
            
            temp = s2.pop()
            print(temp.data, end = " ")
            
            if(temp.right is not None):
                s1.append(temp.right)
                
            if(temp.left is not None):
                s1.append(temp.left)
            
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
spiralTreeTraversal(root)
