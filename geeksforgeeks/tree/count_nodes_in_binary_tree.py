#O(n) solution. This solution will work for any kind of tree i.e. for complete binary tree as well as incomplete binary tree
def countNodes(root):
    
    if(root is None):
        return
    
    return 1 + countNodes(root.left) + countNodes(root.right)

#O(Log n * Log n) solution. This solution will work only if tree is complete binary tree

def countNodesCompleteBT(root):
    
    lh = rh = 0, 0
    curr = root
    
    while(curr.left is not None):
        lh += 1
        curr = curr.left
        
    curr = root
    while(curr.right is not None):
        rh += 1
        curr = curr.right
        
    if(lh == rh):
        return pow(2, lh) - 1
    
    return 1 + countNodes(root.left) + countNodes(root.right)