def getMaximum(root):
    
    if(root is None):
        return -99999999
    
    else:
        return max(root.data, max(getMaximum(root.left)), getMaximum(root.right))