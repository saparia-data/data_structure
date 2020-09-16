'''
Given a Binary Search Tree and a range. Find all the numbers in the BST that lie in the given range.
Note: Element greater than or equal to root go to the right side.

 

Example 1:

Input:
       17
     /    \
    4     18
  /   \
 2     9 
l = 4, h = 24

Output: 4 9 17 18 

https://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/

simply do inorder traversal and check for range and if falls in range just print node data.

'''
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
def printNearNodesUtil(root,l,h,res):
    
    # base case
    if root is None:
        return 
    
    # recurse for left subtree
    printNearNodesUtil(root.left,l,h,res)
    
    # if data is in the range, print it
    if(root.data>=l and root.data<=h):
        res.append (root.data)
    
    # recurse for right
    printNearNodesUtil(root.right,l,h,res)
    
def printNearNodes (root, l, h):
    res = []
    printNearNodesUtil (root, l, h, res)
    return res

l = 10 ; h = 25 ; 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 

print(printNearNodes(root, l, h)) 