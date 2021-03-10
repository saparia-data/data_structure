'''
The function is expected to check if the tree is symmetric, if so return true otherwise return false. 
For knowing symmetricity think of face and hand. Face is symmetric while palm is not.

Note: Symmetric trees are mirror image of itself.

Sample Input:

20

10 20 50 -1 60 -1 -1 30 70 -1 80 -1 90 -1 -1 40 100 -1 110 -1 -1 -1

Sample Output:

true


https://www.youtube.com/watch?v=ewEAjK83ZVM&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=39
https://www.youtube.com/watch?v=gn2ApElF2i0&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=40


'''

class Node:
    def __init__(self):
        self.data = None
        self.children = []
    
    
def create_generic_tree(arr):
    
    root = Node()
    
    st = [] # create empty stack
    
    for i in range(len(arr)):
        
        if(arr[i] == -1):
            st.pop()
        else:
            t = Node()
            t.data = arr[i]
            
            if(len(st) > 0):
                st[-1].children.append(t)
            else:
                root = t
                
            st.append(t)
            
    return root


def areMirror(root1, root2):
    
    if(len(root1.children) != len(root2.children)):
        return False
    
    for i in range(len(root1.children)):
        j = len(root1.children) - 1 - i
        c1 = root1.children[i]
        c2 = root2.children[j]
        if(areMirror(c1, c2) == False):
            return False
        
    return True

def isSymmetric(root):
    
    return areMirror(root, root) # symmetric trees are mirror image of itself


if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, -1, 90, -1, -1, 40, 100, -1, 110, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    
    print(isSymmetric(root))