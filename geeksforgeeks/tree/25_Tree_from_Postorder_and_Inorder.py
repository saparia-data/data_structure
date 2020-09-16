'''
Given inorder and postorder traversals of a Binary Tree in the arrays in[] and post[] respectively. 
The task is to construct the binary tree from these traversals.
For example, if given inorder and postorder traversals are {4, 8, 2, 5, 1, 6, 3, 7} and {8, 4, 5, 2, 6, 7, 3, 1}  respectively, 
then your function should construct below tree.



          1
       /      \
     2        3
   /   \    /   \
  4     5   6    7
    \
      8

https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/

'''

class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
        
def search(arr, strt, end, value): 
    i = 0
    for i in range(strt, end + 1): 
        if (arr[i] == value):  
            break
    return i
        
def buildUtil(In, post, inStrt, inEnd, pIndex): 
      
    # Base case  
    if (inStrt > inEnd):  
        return None
  
    # Pick current node from Postorder traversal  
    # using postIndex and decrement postIndex  
    node = newNode(post[pIndex[0]])  
    pIndex[0] -= 1
  
    # If this node has no children  
    # then return  
    if (inStrt == inEnd):  
        return node  
  
    # Else find the index of this node  
    # in Inorder traversal  
    iIndex = search(In, inStrt, inEnd, node.data)  
  
    # Using index in Inorder traversal,  
    # construct left and right subtress  
    node.right = buildUtil(In, post, iIndex + 1,  
                                  inEnd, pIndex)  
    node.left = buildUtil(In, post, inStrt,  
                        iIndex - 1, pIndex)  
  
    return node

def buildTree(In, post, n): 
    pIndex = [n - 1]  
    root =  buildUtil(In, post, 0, n - 1, pIndex)
    return root 

def preOrder(node): 
    if(node is None):  
        return
    print(node.data,end = " ") 
    preOrder(node.left)  
    preOrder(node.right)
    
if __name__ == '__main__': 
    In = [4, 8, 2, 5, 1, 6, 3, 7] 
    post = [8, 4, 5, 2, 6, 7, 3, 1]  
    n = len(In) 
  
    root = buildTree(In, post, n)    
    preOrder(root)