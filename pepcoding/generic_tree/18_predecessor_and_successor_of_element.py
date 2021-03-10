'''
You are required to find the preorder predecessor and successor of a given element.


Sample Input:

24

10 20 -50 -1 60 -1 -1 30 70 -1 -80 110 -1 -120 -1 -1 90 -1 -1 40 -100 -1 -1 -1

-120

Sample Output:

Predecessor = 110
Successor = 90


https://www.youtube.com/watch?v=vfNlLP-oOUg&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=42
https://www.youtube.com/watch?v=lXL9xs0G8Uo&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=43


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

def solution(root, data):
    
    global successor
    global predecessor
    global state
    
    if(state == 0):
        
        if(root.data == data):
            state = 1
        else:
            predecessor = root.data
            
    elif(state == 1):
        successor = root.data
        state = 2
        
    for child in root.children:
        solution(child, data)
        
    
    
    
    


if __name__ == "__main__":
    
    arr = [10, 20, -50, -1, 60, -1, -1, 30, 70, -1, -80, 110, -1, -120, -1, -1, 90, -1, -1, 40, -100, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    
    global successor
    global predecessor
    global state
    
    successor = None
    predecessor = None
    state = 0
    
    data = -120
    solution(root, data)
    print(predecessor, successor)