'''
Given a Binary search tree and a value X,  the task is to complete the function which will return the floor of x.

Note: Floor(X) is an element that is either equal to X or immediately smaller to X. If no such element exits return -1.

Input:
       8
     /  \
    5    9
   / \    \
  2   6   10

X = 3

Output: 2

Explanation: Floor of 3 in the given BST
is 2

https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/

'''
# recursive solution O(h) extra space and O(n) time complexity
def floorBST(root, x):
    
    if(root is None):
        return None
    
    if(root == x):
        return root.data
    
    if(root.data > x):
        return floorBST(root.left, x)
    
    return max(root.data, floorBST(root.right, x))

# iterative solution with O(1) extra space and O(n) time complexity

def floorIterative(root, x):
    
    while(root is not None):
        
        if(root.data == x):
            res = root.data
            
        elif(root.data > x):
            root = root.left
            
        else:
            res = root.data
            root = root.right
            
    return res