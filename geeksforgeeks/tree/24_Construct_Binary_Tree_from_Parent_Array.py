'''
Given an array of size N that represents a Tree in such a way that array indexes are values in tree nodes 
and array values give the parent node of that particular index (or node). 
The value of the root node index would always be -1 as there is no parent for root. 
Construct the standard linked representation of Binary Tree from this array representation.

Input:
N = 7
Tree = -1 0 0 1 1 3 5
Output: 0 1 2 3 4 5 6
Explanation:For the array parent[] = {-1,
0, 0, 1, 1, 3, 5}; the tree generated
will have a sturcture like 
         0
       /   \
      1     2
     / \
    3   4
   /
  5
/
6

https://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/

'''

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None  
        
def createNode(parent, i, created, root): 
  
    # If this node is already created 
    if created[i] is not None: 
        return
  
    # Create a new node and set created[i] 
    created[i] = Node(i) 
  
    # If 'i' is root, change root pointer and return 
    if parent[i] == -1: 
        root[0] = created[i] # root[0] denotes root of the tree 
        return
  
    # If parent is not created, then create parent first 
    if created[parent[i]] is None: 
        createNode(parent, parent[i], created, root ) 
  
    # Find parent pointer 
    p = created[parent[i]] 
  
    # If this is first child of parent 
    if p.left is None: 
        p.left = created[i] 
    # If second child 
    else: 
        p.right = created[i]   
    


def createTree(parent):
    
    n = len(parent)
    
    root = [None]
    
    created = [None for i in range(n + 1)]
    
    for i in range(n):
        createNode(parent, i, created, root)
        
    return root[0]

def inorder(root): 
    if(root is not None): 
        inorder(root.left) 
        print(root.data, end = " ") 
        inorder(root.right)
        
parent = [-1, 0, 0, 1, 1, 3, 5] 
root = createTree(parent)
inorder(root) 

