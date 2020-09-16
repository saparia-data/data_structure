import queue

# method-1

def printLevelOrder1(root):
    
    res = []
    q = queue.Queue()
    
    if(root is None):
        return
    
    q.put(root)
    q.put(None)
    
    while(len(q) > 1):
        
        node = q.get()
        
        if(node == None):
            res.append("\n")
            q.put(None)
            continue
            
        q.put(node.data)
        
        if(node.left != None):
            q.put(node.left)
            
        if(node.right != None):
            q.put(node.right)
            
    return res

# method-2
def printLevelOrder2(root):
    
    q = queue.Queue()
    q.put(root)

    while(q.qsize()):
        curr_level_size = q.qsize()
        for i in range(curr_level_size):
            curr_node = q.get()
            print(curr_node.data,end=" ")

            if curr_node.left:
                q.put(curr_node.left)
            if curr_node.right:
                q.put(curr_node.right)
        print('\n',end=" ")
            
        