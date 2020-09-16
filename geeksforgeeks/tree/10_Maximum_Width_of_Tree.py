'''
Given a Binary Tree, find the maximum width of it. Maximum width is defined as the maximum number of nodes in any level.
For example, maximum width of following tree is 4 as there are 4 nodes at 3rd level.

          1
       /     \
     2        3
   /    \    /    \
  4    5   6    7
    \
      8

'''

import queue 
def getMaxWidth(root):
    
    q = queue.Queue()
    
    q.put(root)
    max_width = 0
    
    while(q.empty() == False):
        
        curr_level_size = q.qsize()
        
        max_width = max(max_width, curr_level_size)
        
        for i in range(curr_level_size):
            
            curr_node = q.get()
            
            if(curr_node.left is not None):
                q.put(curr_node.left)
                
            if(curr_node.right is not None):
                q.put(curr_node.right)
                
    return max_width
            