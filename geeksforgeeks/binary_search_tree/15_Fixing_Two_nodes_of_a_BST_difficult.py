'''
Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST by swapping them back. Do not change the structure of the tree.

Note: It is guaranteed than the given input will form BST, except for 2 nodes that will be wrong.

Input Tree:
         10
        /  \
       5    8
      / \
     2   20

In the above tree, nodes 20 and 8 must be swapped to fix the tree.  
Following is the output tree
         10
        /  \
       5    20
      / \
     2   8
     
https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/


'''

class Node: 
    def __init__(self,data): 
        self.left = None
        self.right = None
        self.data = data
        
def correctBSTUtil(root):
    
    global first
    global prev
    global last
    global middle
    
    if(root is not None):
        
        correctBSTUtil(root.left)
        
        if(prev is not None and root.data < prev.data):
            if(first is None):
                first = prev
                middle = root
                
            else:
                last = root
                
        prev = root
        
        correctBSTUtil(root.right)
        
def correctBST(root):
    global first
    global prev
    global last
    global middle
    
    first = None
    middle = None
    last = None
    prev = Node(float('-inf'))
    
    correctBSTUtil(root)
    
    if(first is not None and last is not None):
        temp = first.data
        first.data = last.data
        last.data = temp
        
    elif(first is not None and middle is not None):
        temp = first.data
        first.data = middle.data
        middle.data = temp
        
def inOrderTraversal(root):
    if(root is None):
        return
    
    inOrderTraversal(root.left)
    print(root.data, end = " ")
    inOrderTraversal(root.right)
    
root = Node(6); 
root.left = Node(10); 
root.right = Node(2); 
root.left.left = Node(1); 
root.left.right = Node(3); 
root.right.right = Node(12); 
root.right.left = Node(7); 

inOrderTraversal(root)
correctBST(root)
print("\n")
inOrderTraversal(root)
    