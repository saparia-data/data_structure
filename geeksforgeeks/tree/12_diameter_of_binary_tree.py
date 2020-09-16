'''
Given a Binary Tree, find diameter of it.
The diameter of a tree is the number of nodes on the longest path between two leaves in the tree

The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
               
The diameter is of 4 length.

https://stackoverflow.com/questions/52787803/given-a-node-how-long-will-it-take-to-burn-the-whole-binary-tree

'''
# naive solution with O(n2) solution
def height(root):
    
    if(root is None):
        return 0
    
    return (1 + max(height(root.left), height(root.right)))

def longestDiameter(root):
    
    if(root is None):
        return 0
    
    d1 = 1 + height(root.left) + height(root.right)
    d2 = longestDiameter(root.left)
    d3 = longestDiameter(root.right)
    
    return max(d1, max(d2, d3))

# Better solution with O(n) complexity and O(h) extra space
dia = 0
def diameter(root):
    
    global dia
    
    if(root is None):
        return 0
    
    lh = diameter(root.left)
    rh = diameter(root.right)
    
    res = max(dia, 1+ lh + rh)
    
    return 1 + max(lh, rh) 

def diameterUtil(root):
    global dia
    dia = 0
    diameter(root)
    return dia