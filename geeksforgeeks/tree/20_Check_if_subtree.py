'''
Given two binary trees with head reference as T and S having at most N nodes. The task is to check if S is present as subtree in T.
A subtree of a tree T1 is a tree T2 consisting of a node in T1 and all of its descendants in T1.

Example:

S:          10
           /   \
          4     6
                /
              30
 
T:                  26
                   /   \
                  10   3
                /   \   \
               4     6   3
                    /
                  30

In above example S is subtree of T.

Please note that subtree has to be having same leaves non leaves.

   10
  /
20

For example, above tree is not subtree of

         10
       /   \
    20     50
   /  \
30   40

But a subtree of

         30
       /   \
    10     50
   /  
20 

'''

def getInorder(root):
    inOrder = ""
    
    if(root is None):
        inOrder = inOrder + "$"
        return
    
    getInorder(root.left)
    inOrder = inOrder + str(root.data)
    getInorder(root.right)
    
    return inOrder

def getPreorder(root):
    preOrder = ""    
    if(root is None):
        preOrder = preOrder + "$"
        return
    
    preOrder = preOrder + str(root.data)
    getPreorder(root.left)
    getPreorder(root.right)

# check if T2 is sub tree of T1    
def isSubTree(T1, T2):
    
    if(T2 is None):
        return True
    
    if(T1 is None):
        return False
    
    inT1 = getInorder(T1)
    preT1 = getPreorder(T1)
    
    inT2 = getInorder(T2)
    preT2 = getPreorder(T2)
    
    if(preT2 not in preT1):
        return False
    
    if(inT2 not in inT1):
        return False
    
    return True