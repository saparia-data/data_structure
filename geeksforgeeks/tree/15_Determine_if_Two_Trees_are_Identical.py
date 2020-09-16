'''
Given two binary trees, the task is to find if both of them are identical or not. 

'''

def areIdentical(root1, root2):
    
    if(root1 is None and root2 is None):
        return 1
    if(root1 is not None and root2 is not None):
        return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)