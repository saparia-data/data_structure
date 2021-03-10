'''
The function is expected to visit every node in "levelorder fashion" but in a zig-zag manner 
i.e. 1st level should be visited from left to right, 2nd level should be visited from right to left and so on. 
All nodes on same level should be separated by a space. Different levels should be on separate lines.

Sample Input:

24

10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1

Sample Output:

10 
40 30 20 
50 60 70 80 90 100 
120 110


https://www.youtube.com/watch?v=Yde0l3q-qJs&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=17
https://www.youtube.com/watch?v=eDdPZ05y4Os&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=18


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

def levelOrderLinewiseZigzagTraversals(root):
    
    ms = [] # main stack
    cs = [] # child stack
    level = 1
    ms.append(root)
    
    while(len(ms) > 0):
        
        node = ms.pop()
        print(str(node.data), end = " ")
        
        if(level % 2 == 1):
            
            for i in range(len(node.children)):
                child = node.children[i]
                cs.append(child)
        else:
            
            for i in range(len(node.children) - 1, -1, -1):
                child = node.children[i]
                cs.append(child)
                
        if(len(ms) == 0):
            ms = cs
            cs = []
            level += 1
            print()
            
        
       
        
        


if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    root = create_generic_tree(arr)
    print(root.data)
    levelOrderLinewiseZigzagTraversals(root)