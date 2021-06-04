'''
You are required to complete the body of size, sum, max and height function. The functions are expected to
    -size - return the number of nodes in BinaryTree
    -sum - return the sum of nodes in BinaryTree
    -max - return the highest node in BinaryTree
    -height - return the height of tree in terms of edges

Sample Input:

19
50 25 12 n n 37 30 n n n 75 62 n 70 n n 87 n n

Sample Output:

9
448
87
3


https://www.youtube.com/watch?v=I3D3p1TG1uE&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=5
https://www.youtube.com/watch?v=Y7fg3QS6u6w&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=6



'''

import sys

class Node:
    def __init__(self, data, left, right): 
        self.data = data  
        self.left = left
        self.right = right
        
class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state
        
def create_binary_tree(arr):
    
    st = []
    
    #create root node and root pair
    root = Node(arr[0], None, None)
    root_pair = Pair(root, 1)
    
    st.append(root_pair)
    
    idx = 0
    while(len(st) > 0):
        
        top = st[-1]
        
        if(top.state == 1):
            idx += 1 # increment index
            if(arr[idx] != None):
                left_node = Node(arr[idx], None, None) # create left node bcz state is 1
                top.node.left = left_node # assign left node to left of top node
                left_pair = Pair(left_node, 1) # create pair for left_node with initial state as 1
                st.append(left_pair) # push left_pair in stack
            else:
                top.node.left = None
                
            top.state += 1 # increment state for top pair
        
        elif(top.state == 2):
            idx += 1 # increment index
            if(arr[idx] != None):
                right_node = Node(arr[idx], None, None) # create right node bcz state is 2
                top.node.right = right_node # assign right node to right of top node
                right_pair = Pair(right_node, 1) # create pair for right_node with initial state as 1
                st.append(right_pair) # push right_pair in stack
            else:
                top.node.right = None
                
            top.state += 1 # increment state for top pair
        else: 
            st.pop(-1) # if state is 3 pop
            
    return root

    
def getSize(root):
    
    if(root == None):
        return 0
        
    ls = getSize(root.left)
    rs = getSize(root.right)
    ts = ls + rs + 1
    return ts
    
    
def getSum(root):
    
    if(root == None):
        return 0
    
    lsm = getSum(root.left)
    rsm = getSum(root.right)
    tsm = lsm + rsm + root.data
    return tsm
    

def getMax(root):
    
    if(root == None):
        return -(sys.maxsize-1)
    
    lm = getMax(root.left)
    rm = getMax(root.right)
    tm = max(root.data, lm, rm)
    return tm
    
    
def getHeight(root): # get height in terms of edges
    
    if(root == None):
        return -1 # -1 if height in terms of edges else return 0
    
    lh = getHeight(root.left)
    rh = getHeight(root.right)
    th = max(lh, rh) + 1
    return th
    
    
    
if __name__ == "__main__":
    
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    
    root = create_binary_tree(arr)
    print(root.data)
    print("##########################################################")
    print(getSize(root))
    print(getSum(root))
    print(getMax(root))
    print(getHeight(root))