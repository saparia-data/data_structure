'''
Given a binary tree, connect the nodes that are at same level. You'll be given an addition nextRight pointer for the same.

Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
       10                       10 ------> NULL
      / \                       /      \
     3   5       =>            3 ------> 5 --------> NULL
    / \     \               /  \           \
   4   1   2               4 --> 1 ----->  2 -------> NULL
   
Input:
S = 10 20 30 40 60
Output:
10 20 30 40 60
40 20 60 10 30
Explanation:The connected tree is
         10 ----------> NULL
       /     \
     20 ------> 30 -------> NULL
  /    \
 40 ----> 60 ----------> NULL


'''

class newnode: 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = self.nextRight = None
        
def connect(root):
    
    if(root is None):
        return
    
    q = []
    
    q.append(root)
    
    while(len(q)):
        
        curr_level_size = len(q)
        
        for i in range(curr_level_size):
            
            curr_node = q[0]
            
            if(i != curr_level_size - 1):
                curr_node.nextRight = q[1]
                
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
                
            q.pop(0)
            
root = newnode(10)  
root.left = newnode(20)  
root.right = newnode(30)  
root.left.left = newnode(40)
root.left.right = newnode(60)

connect(root)

if(root.nextRight):
    print(root.nextRight.data)
else:
    print(None)
    
if(root.left.nextRight):
    print(root.left.nextRight.data)
else:
    print(None)