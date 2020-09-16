'''
https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

'''

def inOrderUtil(root, res):
    
    if(root is None):
        return
    
    inOrderUtil(root.left, res)
    res.append(root.data)
    inOrderUtil(root.right, res)
    
    
def inorder(root):
    
    res = []
    inOrderUtil(root, res)
    return res    