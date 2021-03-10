'''
Sample Input:

24

10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1

Sample Output:

10 20 30 40 50 60 70 80 90 100 110 120 .


https://www.youtube.com/watch?v=ZHdnMxqgQOM&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=12
https://www.youtube.com/watch?v=TUxo5YpKvxw&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=13


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

def levelOrderTraversals(root):
    
    q = []
    
    q.append(root)
    
    while(len(q) > 0):
        
        node = q.pop(0)
        print(node.data, end = " ")
        
        for child in node.children:
            q.append(child)
            
    print(".")


if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    root = create_generic_tree(arr)
    print(root.data)
    levelOrderTraversals(root)