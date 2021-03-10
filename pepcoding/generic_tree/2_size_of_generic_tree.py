'''
https://www.youtube.com/watch?v=epQq3XWitxA&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=5

Sample Input:

12

10 20 -1 30 50 -1 60 -1 -1 40 -1 -1

Sample Output:
6

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

def size(root):
    
    s = 0
    
    for child in root.children:
        cs = size(child)
        s = s + cs
        
    s = s + 1
    return s


if __name__ == "__main__":
    
    arr = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    print(size(root))