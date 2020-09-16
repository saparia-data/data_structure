def getSize(root):
    
    if(root is None):
        return 0
    else:
        return 1 + getSize(root.left) + getSize(root.right)