'''
Given a binary tree and an integer X. Your task is to complete the function countSubtreesWithSumX() 
that returns the count of the number of subtress having total node's data sum equal to the value X.

Example: For the tree given below:            

              5
            /    \
        -10      3
        /  \    /  \
      9     8  -4  7

Subtree with sum 7:
             -10
            /   \
          9      8

and one node 7.


'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
            
def util(root, x, count):
    
    if(root is None):
        return 0
    
    lt = util(root.left, x, count)
    rt = util(root.right, x, count)
    
    summ = lt + rt + root.data
    
    if(summ == x):
        count[0] += 1
        
    return summ


def countSubtreesWithSumX(root ,x):
    
    if(root is None):
        return 0
    
    
    count = [0]
    
    lt = util(root.left, x, count)
    rt = util(root.right, x, count)
    
    sum_of_current = lt + rt + root.data
    
    if(sum_of_current == x):
        count[0] += 1
        
    return count[0]

root = Node(5)  
root.left = Node(-10)  
root.right = Node(3)  
root.left.left = Node(9)  
root.left.right = Node(8)  
root.right.left = Node(-4)  
root.right.right = Node(7)  

print(countSubtreesWithSumX(root, 7))