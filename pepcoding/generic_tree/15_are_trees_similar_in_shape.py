'''
The function is expected to check if the two trees passed to it are similar in shape or not.


Sample Input:

24
10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1

24
1 2 5 -1 6 -1 -1 3 7 -1 8 11 -1 12 -1 -1 9 -1 -1 4 10 -1 -1 -1

Sample Output:

true


https://www.youtube.com/watch?v=rumfdyFR-_A&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=35
https://www.youtube.com/watch?v=y_PIhsd9vt0&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=36


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

def areSimilar(root_1, root_2):
    
    if(len(root_1.children) != len(root_2.children)):
        return False
    
    for i in range(len(root_1.children)):
        
        c1 = root_1.children[i]
        c2 = root_2.children[i]
        
        if(areSimilar(c1, c2) == False):
            return False
        
    return True


if __name__ == "__main__":
    
    arr1 = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    arr2 = [1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8, 11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1, -1]
    
    root_1 = create_generic_tree(arr1)
    root_2 = create_generic_tree(arr2)
    print(root_1.data)
    print(root_2.data)
    
    print(areSimilar(root_1, root_2))