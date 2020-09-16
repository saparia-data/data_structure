'''
Given a Binary Search Tree. The task is to find the minimum element in this given BST.

Example 1:

Input:
           5
         /    \
        4      6
       /        \
      3          7
     /
    1
    
Output: 1


'''

def minValue(root):
    
    if(root is None):
        return -1
    
    temp = root
    
    while(temp.left):
        temp = temp.left
        
    return temp.data