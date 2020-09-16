def postOrderUtil(root, res):
    
    if(root is None):
        return
    
    postOrderUtil(root.left, res)
    postOrderUtil(root.right, res)
    res.append (root.data)

def postOrder(root):
    
    res = []
    postOrderUtil(root, res)
    return res