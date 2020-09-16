def preOrderUtil(root, res):
    
    if(root is None):
        return
    
    res.append(root.data)
    preOrderUtil(root.left, res)
    preOrderUtil(root.right, res)
    
def preOrder(root):
    
    res = []
    preOrderUtil(root, res)
    return res
    
    
    