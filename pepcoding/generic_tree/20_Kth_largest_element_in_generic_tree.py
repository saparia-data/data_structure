'''
You are given a number k. You are required to find and print the kth largest value in the tree.


Sample Input:

24

10 20 -50 -1 60 -1 -1 30 70 -1 -80 110 -1 -120 -1 -1 90 -1 -1 40 -100 -1 -1 -1

8

Sample Output:

10



https://www.youtube.com/watch?v=7Vi6GkgtWpg&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=46
https://www.youtube.com/watch?v=DmAGEAeYhJs&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=47


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

def ceilAndfloor(root, data):
    
    global ceil
    global floor
    
    if(root.data > data):
        
        if(root.data < ceil):
            ceil = root.data
            
    if(root.data < data):
        
        if(root.data > floor):
            floor = root.data
            
    for child in root.children:
        ceilAndfloor(child, data)
        
        
def kthLargest(node, k):
    
    global ceil
    global floor
    
    floor = -sys.maxsize - 1
    factor = sys.maxsize
    
    for i in range(k):
        ceilAndfloor(node, factor) # this will set floor as largest value as factor is +infinity
        factor = floor
        floor = -sys.maxsize - 1
        
    return factor

if __name__ == "__main__":
    
    arr = [10, 20, -50, -1, 60, -1, -1, 30, 70, -1, -80, 110, -1, -120, -1, -1, 90, -1, -1, 40, -100, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    
    global ceil
    global floor
    
    ceil = sys.maxsize
    floor = -sys.maxsize - 1
    
    #print(ceil, floor)
    
    k = 8
    print(kthLargest(root, k))