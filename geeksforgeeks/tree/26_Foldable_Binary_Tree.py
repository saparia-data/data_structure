'''
Given a binary tree, find out if the tree can be folded or not.

-A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. 
-An empty tree is considered as foldable.

Consider the below tree: It is foldable

       10
     /    \
    7      15
     \    /
      9  11
      

'''

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        
def foldableUtil(root1, root2):
    
    if(root1 is None and root2 is None):
        return True
    
    if(root1 is None or root2 is None):
        return False
    
    return foldableUtil(root1.left, root2.right) and foldableUtil(root1.right, root2.left)

def foldable(root):
    
    if(root is None):
        return True
    
    result = foldableUtil(root.left, root.right)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.left = Node(4)

print(foldable(root))