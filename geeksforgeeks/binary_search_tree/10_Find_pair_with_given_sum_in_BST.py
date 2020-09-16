'''
Given a BST and a number X. The task is to check if any pair exists in BST or not whose sum is equal to X.

Example 1:

Input:
      8
    /   \
   5     9
  / \
 1   3
X = 4

Output: 1

Explanation: For the given input, there
exist a pair whose sum is, i.e, (3,1).

https://www.youtube.com/watch?v=ouuGHu9Sjhg

Method-1
-Do inorder traversal and store in an array
-traverse array from front and end and check addition is there or not. Check two pointer approach in an array
-Complexity is O(n) and space complexity is O(n)

'''
class Node: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None
        
def search(node, comp):
    
    if(node is None):
        return None
    
    if(node.data == comp):
        return True
    
    elif(node.data < comp):
        return search(node.right, comp)
    
    else:
        return search(node.left, comp)

# O(n2) solution    
def travelAndPrint(root, node, target):
    
    if(node is None):
        return None
    
    travelAndPrint(root, node.left, target)
    
    comp = target - node.data
    
    if(node.data < comp):
        if(search(root, comp)):
            print(node.data, comp)
    
    travelAndPrint(root, node.right, target)
    
# O(n) solution    
def findPair(root,x):
    '''
    :param root: given root of the bst
    :param x: given value.
    :return: boolean.
    
    hash = set() # hash to be used. is declared and cleared after ever test case
    '''
    global hash
    if root is None:
        return False
    if findPair(root.left,x): # traverse the left subtree
        return True
    if (x-root.key) in hash: # if its pair with current node
        return True
    hash.add(root.key)

    return findPair(root.right,x) # traverse right subtree
    
    
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 

travelAndPrint(root, root, 30)