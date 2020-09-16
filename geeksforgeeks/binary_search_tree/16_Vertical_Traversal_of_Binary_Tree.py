'''
Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Input:
       1
    /    \
   2      3
 /   \      \
4     5      6

Output: 4 2 1 5 3 6

https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/

https://stackoverflow.com/questions/36244380/enumerate-for-dictionary-in-python

'''

class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
        
def getVerticalOrder(root, hd, m):
    
    if(root is None):
        return
    
    try: 
        m[hd].append(root.key) 
    except: 
        m[hd] = [root.key]
        
    getVerticalOrder(root.left, hd-1, m)
    getVerticalOrder(root.right, hd+1, m)
    
def printVerticalOrder(root):
    
    m = dict()
    hd = 0
    
    getVerticalOrder(root, hd, m)
    
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end = " ")
            
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 
printVerticalOrder(root)