'''
The function is expected to check if the two trees passed to it are mirror images of each other in shape 
(data not to be checked, just the shape of tree).

Sample Input:

12
10 20 -1 30 50 -1 60 -1 -1 40 -1 -1

12
100 200 -1 300 500 -1 600 -1 -1 400 -1 -1

Sample Output:

true


https://www.youtube.com/watch?v=GfEQs3qhMws&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=37
https://www.youtube.com/watch?v=v2MqQoma9uc&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=38


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


def areMirror(root1, root2):
    
    if(len(root1.children) != len(root2.children)):
        return False
    
    for i in range(len(root1.children)):
        j = len(root1.children) - 1 - i
        c1 = root1.children[i]
        c2 = root2.children[j]
        if(areMirror(c1, c2) == False):
            return False
        
    return True


if __name__ == "__main__":
    
    arr1 = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    arr2 = [100, 200, -1, 300, 500, -1, 600, -1, -1, 400, -1, -1]
    
    root1 = create_generic_tree(arr1)
    root2 =  create_generic_tree(arr2)
    print(root1.data)
    print(root2.data)
    
    print(areMirror(root1, root2))
    