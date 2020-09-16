'''
Given a BST and a key. Insert a new Node with value equal to that key into the BST. 

Example:

Input:
      2
   /    \
  1      3
K = 4

Output: 1 2 3 4

Explanation: After inserting the node 4
Inorder traversal will be 1 2 3 4.

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

'''
class Node: 
    def __init__(self,data): 
        self.left = None
        self.right = None
        self.data = data
        
def insert(root, k):
    
    if(root is None):
        root = Node(k)  
        
    else:
        
        if(root.data < k):
            if(root.right):
                insert(root.right, k)
            else:
                root.right = Node(k)
                
        else:
            if(root.left):
                insert(root.left, k)
            else:
                root.left = Node(k)
                
def inorder(root): 
    if(root): 
        inorder(root.left) 
        print(root.data, end = " ") 
        inorder(root.right)
        
root = Node(50)

insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

inorder(root)