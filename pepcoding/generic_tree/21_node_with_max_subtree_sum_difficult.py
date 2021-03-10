'''
You are required to find and print the node which has the subtree with largest sum. 
Also print the sum of the concerned subtree separated from node's value by an '@'.


Sample Input:

20

10 20 -50 -1 60 -1 -1 30 -70 -1 80 -1 90 -1 -1 40 -100 -1 -1 -1

Sample Output:

30@130



https://www.youtube.com/watch?v=TKqOZ3tp1D8&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=48
https://www.youtube.com/watch?v=tDx3PPwgSxs&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=48


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

def maxSumSubTree(root):
    
    global max_sum_node
    global max_sum
    
    summ = 0
    
    for child in root.children:
        csum = maxSumSubTree(child)
        summ = summ + csum
        
    summ = summ + root.data
    
    if(summ > max_sum):
        max_sum = summ
        max_sum_node = root.data
        
    return summ

if __name__ == "__main__":
    
    arr = [10, 20, -50, -1, 60, -1, -1, 30, -70, -1, 80, -1, 90, -1, -1, 40, -100, -1, -1, -1]
    
    root = create_generic_tree(arr)
    print(root.data)
    
    global max_sum_node
    global max_sum
    
    max_sum_node = 0
    max_sum = -sys.maxsize - 1
    
    maxSumSubTree(root)
    print(str(max_sum_node) + "@" + str(max_sum))