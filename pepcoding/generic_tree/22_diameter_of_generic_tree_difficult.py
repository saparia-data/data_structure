'''
You are required to find and print the diameter of tree.
The diameter is defined as maximum number of edges between any two nodes in the tree.


Sample Input:

20

10 20 -50 -1 60 -1 -1 30 -70 -1 80 -1 90 -1 -1 40 -100 -1 -1 -1

Sample Output:

4


https://www.youtube.com/watch?v=_LVi8UWDCh8&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=50
https://www.youtube.com/watch?v=GIA2cZgOdwg&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=50



'''

import sys

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


def calaulateDiamater(root):
    
    global dia # diameter
    
    dch = -1 # deepest child height
    sdch = -1 # second deepest child height
    
    for child in root.children:
        
        ch = calaulateDiamater(child)
        
        if(ch >= dch):
            sdch = dch
            dch = ch
        elif(ch >= sdch):
            sdch = ch
            
    if(dch + sdch + 2 > dia):
        dia = dch + sdch + 2
        
    dch += 1
    return dch
            
        


if __name__ == "__main__":
    
    arr = [10, 20, -50, -1, 60, -1, -1, 30, -70, -1, 80, -1, 90, -1, -1, 40, -100, -1, -1, -1]
    
    global dia # diameter

    dia = 0
    root = create_generic_tree(arr)
    print(root.data)
    
    calaulateDiamater(root)
    print(dia)