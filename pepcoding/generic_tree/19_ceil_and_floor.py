'''
You are required to find the ceil and floor value of a given element.


Sample Input:

24

10 20 -50 -1 60 -1 -1 30 70 -1 -80 110 -1 -120 -1 -1 90 -1 -1 40 -100 -1 -1 -1

70

Sample Output:

CEIL = 90
FLOOR = 60



https://www.youtube.com/watch?v=m__4qg_G_gs&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=44
https://www.youtube.com/watch?v=I1rAT8hRnWI&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=45


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

def solution(root, data):
    
    global ceil
    global floor
    
    if(root.data > data):
        
        if(root.data < ceil):
            ceil = root.data
            
    if(root.data < data):
        
        if(root.data > floor):
            floor = root.data
            
    for child in root.children:
        solution(child, data)


if __name__ == "__main__":
    
    arr = [10, 20, -50, -1, 60, -1, -1, 30, 70, -1, -80, 110, -1, -120, -1, -1, 90, -1, -1, 40, -100, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    
    global ceil
    global floor
    
    ceil = sys.maxsize
    floor = -sys.maxsize - 1
    
    print(ceil, floor)
    
    data = 70
    solution(root, data)
    print(ceil, floor)