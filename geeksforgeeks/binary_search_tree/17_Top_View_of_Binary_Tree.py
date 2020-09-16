'''
Given below is a binary tree. The task is to print the top view of binary tree. 
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Print from leftmost node to rightmost node.

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100

Output: 40 20 10 30 100


https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/

'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0
        
        
def topview(root):
    
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
        
        if(hd not in m):
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
        
        