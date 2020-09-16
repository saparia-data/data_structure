'''
Given a Binary Search Tree (BST) and a node value. Delete the node with the given value from the BST. 
If no node with value x exists, then do not make any change. 

Input:
            1
             \
              2
                \
                 8 
               /    \
              5      11
            /  \    /  \
           4    7  9   12
           
X = 9
Output: 1 2 4 5 7 8 11 12

Explanation: In the given input tree after
deleting 9 will be

             1
              \
               2
                 \
                  8
                 /   \
                5     11
               /  \     \
              4    7     12

https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

'''

def minValueNode(node):
    
    current = node
    
    while(current.left):
        current = current.left
        
    return current

def deleteNode(root, key):
    
    if(root is None):
        return root
    
    if(key < root.key):
        root.left = deleteNode(root.left, key)
        
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        
    else:
        
        if(root.left is None):
            temp = root.right
            root = None
            return temp
        
        if(root.right is None):
            temp = root.left
            root = None
            return temp
        
        temp = minValueNode(root.right)
        
        root.key = temp.key
        
        root.right = deleteNode(root.right, temp.key)
        
    return root
    