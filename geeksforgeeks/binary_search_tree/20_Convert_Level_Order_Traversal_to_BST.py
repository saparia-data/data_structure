'''
Given an array of size N containing level order traversal of a BST. The task is to complete the function constructBst(), 
that construct the BST (Binary Search Tree) from its given level order traversal.

Input:
N = 9
BST[] = {7,4,12,3,6,8,1,5,10}
Output: 7 4 3 1 6 5 12 8 10
Explanation: After constructing BST, the preorder traversal of BST is 7 4 3 1 6 5 12 8 10.

The idea is to use the Recursion:-
We know that the first element will always be the root of tree and second element will be the left child 
and third element will be the right child (if fall in the range), and so on for all the remaining elements.

1) First pick the first element of the array and make it root.
2) Pick the second element, if it’s value is smaller than root node value make it left child,
3) Else make it right child
4) Now recursively call the step (2) and step (3) to make a BST from its level Order Traversal.

https://www.geeksforgeeks.org/construct-bst-given-level-order-traversal/

'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBst(a,n):
    if n>0:
        root=Node(a[0])
    else:
        return None
    for i in range(1,n):
        insert(root,a,n,i)
    return root

def insert(root,a,n,i):
    if root.data>a[i]:
        if root.left:
            insert(root.left,a,n,i)
        else:
            root.left=Node(a[i])
    if root.data<a[i]:
        if root.right:
            insert(root.right,a,n,i)
        else:
            root.right=Node(a[i])