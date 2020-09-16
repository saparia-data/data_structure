'''
Given a Binary Search Tree (with all values unique) and two node values. Find the Lowest Common Ancestors of the two nodes in the BST.

https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

'''

def lowestCommonAncestor(root, n1, n2):
    
    if(root is None):
        return None
    
    if(root.data > n1 and root.data > n2):
        return lowestCommonAncestor(root.left, n1, n2)
    
    elif(root.data < n1 and root.data < n2):
        return lowestCommonAncestor(root.right, n1, n2)
    
    return root