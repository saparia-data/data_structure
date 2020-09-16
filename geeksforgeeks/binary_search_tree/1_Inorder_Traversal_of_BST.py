'''
Inorder traversal means traversing through the tree in a Left, Node, Right manner. We first traverse left, then print the current node, 
and then traverse right. This is done recursively for each node.
You are given an array arr of size sizeOfArray. 
You need to create a BST using elements of the array. The BST is to be created using the elements in the order of their arrival.

Example:

Input:
       5
    /    \
   2      7
    \       \
    3        8
    
Output: 2 3 5 7 8


'''
def inOrder(root):
    if(root is None):
        return
    
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)