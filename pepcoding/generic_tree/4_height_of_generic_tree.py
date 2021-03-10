'''
Find height of generic tree.

Sample Input:

12

10 20 -1 30 50 -1 60 -1 -1 40 -1 -1

Sample Output:

2


https://www.youtube.com/watch?v=Vm5ubT7aPmI&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=8
https://www.youtube.com/watch?v=duRYlVs72js&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=9


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

def getHeight(root):
    
    h = -1
    
    for child in root.children:
        ch = getHeight(child)
        h = max(ch, h)
        
    h += 1
    
    return h


if __name__ == "__main__":
    
    arr = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    root = create_generic_tree(arr)
    print(root.data)
    print(getHeight(root))