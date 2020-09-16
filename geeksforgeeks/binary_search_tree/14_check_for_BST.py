'''
Given a binary tree. Check whether it is a BST or not.


https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

'''

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
        
INT_MAX = 4294967296
INT_MIN = -4294967296

# O(n) time complexity and O(n) space complexity
def isBST(node):
    return isBSTUtil(node,  INT_MIN, INT_MAX)

def isBSTUtil(node, mini, maxi):
    
    if(node is None):
        return True
    
    if(node.data < mini or node.data > maxi):
        return False
    
    return (isBSTUtil(node.left, mini, node.data - 1) and isBSTUtil(node.right, node.data + 1, maxi))

root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 

print(isBST(root))