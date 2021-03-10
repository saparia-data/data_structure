'''
1) https://www.youtube.com/watch?v=9Oi3WamOCPo&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=2&t=331s
2) https://www.youtube.com/watch?v=3xovYxKCgBQ&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=3

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
                
    
    
    
if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    display(root)