'''
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.

If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. 
For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.

'''
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0
        
        
def bottomView(root):
    
    if(root is None):
        return
    
    q = []
    m = {}
    hd = 0
    root.hd = hd
    q.append(root)
    while(len(q)):
        
        root = q[0]
        hd = root.hd
        
        m[hd] = root.data
            
        if(root.left):
            root.left.hd = hd - 1
            q.append(root.left)
            
        if(root.right):
            root.right.hd = hd + 1
            q.append(root.right)
            
        q.pop(0)
        
    for i in sorted(m):
        print(m[i], end = " ")
        
root =  Node(20); 
root.left =  Node(8); 
root.right =  Node(22); 
root.left.left =  Node(5); 
root.left.right =  Node(3); 
root.right.left =  Node(4); 
root.right.right =  Node(25); 
root.left.right.left =  Node(10); 
root.left.right.right =  Node(14); 
bottomView(root)