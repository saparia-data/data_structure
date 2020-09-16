'''
Given a Binary Tree, you need to find the maximum value which you can get by subtracting the value of node B from the value of node A, 
where A and B are two nodes of the binary tree and A is an ancestor of B. 

Input:
S = 5 2 1
Output: 4
Explanation:
      5
    /    \
   2      1
The maximum difference we can get
is 4, which is bewteen 5 and 1.

https://www.geeksforgeeks.org/maximum-difference-between-node-and-its-ancestor-in-binary-tree/

'''
_MIN = -2147483648
_MAX = 2147483648

class Node:  
  
    # Constructor to create a new node  
    def __init__(self, key):  
        self.key = key 
        self.left = None
        self.right = None

def maxDiffUtil(t, res):
    
    if(t is None):
        return _MAX, res
    
    if(t.left is None and t.right is None):
        return t.key, res
    
    a, res = maxDiffUtil(t.left, res)
    b, res = maxDiffUtil(t.right, res)
    
    val = min(a, b)
    
    res = max(res, t.key - val)
    
    return min(val, t.key), res

def maxDiff(root):
    
    res = _MIN
    x, res = maxDiffUtil(root, res)
    return res


if __name__ == '__main__':

    """ Construct below tree
              6
            /   \
           /     \
          3       8
                /   \
               /     \
              2       4
            /   \
           /     \
          1       7
    """

    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.right.left = Node(2)
    root.right.right = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(7)

    print(maxDiff(root))