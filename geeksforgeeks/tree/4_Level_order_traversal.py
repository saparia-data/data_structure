def levelOrderTraversal(root):
    
    if(root is None):
        return
    
    q = []
    
    res = []
     
    q.append(root)
     
    while(len(q)):
        
        node = q.pop()
        res.append(node.data)
        
        if(node.left != None):
            q.append(node.left)
            
        if(node.right != None):
            q.append(node.right)
    
    