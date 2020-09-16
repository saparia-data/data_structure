'''
Given a BST and a number X. The task it to find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

Example 1:

Input:
      5
    /   \
   1     7
    \
     2 
      \
       3
       
X = 3

Output: 3

Explanation: We find 3 in BST, so ceil
of 3 is 3.

https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/

'''
def ceil(root, inp): 
      
    # Base Case 
    if root == None: 
        return -1
      
    # We found equal key 
    if root.key == inp : 
        return root.key  
      
    # If root's key is smaller, ceil must be in right subtree 
    if root.key < inp: 
        return ceil(root.right, inp) 
      
    # Else, either left subtree or root has the ceil value 
    val = ceil(root.left, inp) 
    return val if val >= inp else root.key