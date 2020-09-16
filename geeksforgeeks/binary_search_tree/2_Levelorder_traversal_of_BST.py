'''
Levelorder traversal means traversing through the tree level by level, from left to right.
You are given an array arr of size sizeOfArray. You need to create a BST using elements of the array. 
The BST is to be created using the elements in the order of their arrival.

Example:

Input:
      5
    /   \
   2     7
   \      \
    3      8
    
Output: 5 2 7 3 8


'''
def levelOrder(root):
    
    if(root is None):
        return
    
    q = []
    
    q.append(root)
    
    while(len(q)):
        
        temp = q[0]
        q.remove(q[0])
        print(temp.data, end = " ")
        
        if(temp.left is not None):
            q.append(temp.left)
            
        if(temp.right is not None):
            q.append(temp.right)