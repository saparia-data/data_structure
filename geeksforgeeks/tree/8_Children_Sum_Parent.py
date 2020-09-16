'''
Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.

Tree is like:
            10
           /    
        10       

Here, every node is sum of its left and right child.
'''

def isSumProperty(root):
    
    if(root is None):
        return True
    
    if(root.left is None and root.right is None):
        return True
    
    summ = 0
    
    if(root.left is not None):
        summ += root.left.data
        
    if(root.right is not None):
        summ += root.right.data
        
    return (root.data == summ and isSumProperty(root.left) and isSumProperty(root.right))