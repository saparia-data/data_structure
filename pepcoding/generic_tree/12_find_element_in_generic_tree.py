'''
The function is expected to find the given data in the tree, if found it should return true or return false.


Sample Input:

24

10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1

120

Sample Output:

true


https://www.youtube.com/watch?v=H65rNN3TJkE&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=27
https://www.youtube.com/watch?v=dWri78Z4khs&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=28


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


def findData(node, data):
    
    if(node.data == data):
        return True
    
    for child in node.children:
        fic = findData(child, data)
        
        if(fic):
            return True
        
    return False


if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    data = 110
    print(findData(root, data))