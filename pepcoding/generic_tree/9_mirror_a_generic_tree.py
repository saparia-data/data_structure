'''
The function is expected to create a mirror image of the tree.


Sample Input:

24

10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1

Sample Output:

10 -> 20, 30, 40, .
20 -> 50, 60, .
50 -> .
60 -> .
30 -> 70, 80, 90, .
70 -> .
80 -> 110, 120, .
110 -> .
120 -> .
90 -> .
40 -> 100, .
100 -> .
10 -> 40, 30, 20, .
40 -> 100, .
100 -> .
30 -> 90, 80, 70, .
90 -> .
80 -> 120, 110, .
120 -> .
110 -> .
70 -> .
20 -> 60, 50, .
60 -> .
50 -> .


https://www.youtube.com/watch?v=CjtGTcG-fUU&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=20
https://www.youtube.com/watch?v=PDjTi3WGSNA&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=21


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


def display(root):
    
    val = str(root.data) + " -> "
    
    for node in root.children:
        val += str(node.data) + ", "
        
    val += "."
    print(val)
    
    for child in root.children:
        display(child)

def mirror(root):
    
    for child in root.children:
        mirror(child)
        
    root.children.reverse()
    
    
    


if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    root = create_generic_tree(arr)
    print(root.data)
    display(root)
    mirror(root)
    display(root)