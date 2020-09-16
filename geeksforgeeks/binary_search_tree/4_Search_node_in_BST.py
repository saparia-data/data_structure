'''
Given a Binary Search Tree (BST), you need to find if a particular node(data) is present in the BST or not. 
Note: The BST does not insert duplicates.

Example 1:

Input:
         2
          \
          81
        /    \
      42      87
    /   \       \
   45   66      90
   
x = 87

Output: 1

Explanation: As 87 is present in the
given nodes , so the output will be 1.

'''

def search(node, data):
    
    if(node is None):
        return None
    
    if(node.data == data):
        return True
    
    elif(node.data < data):
        return search(node.right, data)
    
    else:
        return search(node.left, data)