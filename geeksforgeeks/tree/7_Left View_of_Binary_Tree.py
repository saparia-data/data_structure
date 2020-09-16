'''
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. 
The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   


'''
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
        
# Recursive Solution
def leftViewUtil(root, level):
    global max_level
    
    if(root is None):
        return
    
    if(max_level < level):
        print(root.data, end = " ")
        max_level = level
        
    leftViewUtil(root.left, level + 1)
    leftViewUtil(root.right, level + 1)
    

def leftView(root):
    global max_level
    
    max_level = 0
    leftViewUtil(root, 1)
    
    
# Iterative Solution
import queue
def leftViewUtilIterative(root):
    
    if(root is None):
        return
    
    q = queue.Queue()
    q.put(root)
    
    while(q.empty() == False):
        
        count = q.qsize()
        
        for i in range(count):
            
            curr = q.get()
            
            if(i == 0):
                print(curr.data, end = " ")
                
            if(curr.left is not None):
                q.put(curr.left)
                
            if(curr.right is not None):
                q.put(curr.right)
                
        
root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40)  
    
leftView(root)
print("\n")  
leftViewUtilIterative(root)
    