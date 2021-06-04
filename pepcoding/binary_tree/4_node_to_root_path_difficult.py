'''
The functions are expected to 
    - find -> return true or false depending on if the data is found in binary tree.
    - nodeToRoot -> returns the path from node (correspoding to data) to root in form of an arraylist (root being the last element)


Sample Input:

19
50 25 12 n n 37 30 n n n 75 62 n 70 n n 87 n n
30

Sample Output:

true
[30, 37, 25, 50]



https://www.youtube.com/watch?v=p_8c3QYbDJ8&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=17
https://www.youtube.com/watch?v=1Kyc-zQS7eQ&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=18


'''

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

def levelOrderTraversal(root):
    
    mq = []
    
    mq.append(root)
    
    while(len(mq) > 0):
        
        count = len(mq)
        
        for i in range(count):
            node = mq.pop(0)
            print(str(node.data) + " ", end = " ")
            
            if(node.left != None):
                mq.append(node.left)
                
            if(node.right != None):
                mq.append(node.right)
        
        print()    


def findNode(node, data):
    
    global path
    
    if(node == None):
        return False
    
    if(node.data == data):
        path.append(node.data)
        return True
    
    fil = findNode(node.left, data) # fil -> find in left
    
    if(fil):
        path.append(node.data)
        return True
    
    fir = findNode(node.right, data) # fil -> find in right
    
    if(fir):
        path.append(node.data)
        return True
    
    return False
    
    
    
    


if __name__ == "__main__":
    
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    
    root = create_binary_tree(arr)
    print(root.data)
    print("##########################################################")
    
    global path
    path = []
    
    data = 30
    print(findNode(root, data))
    print(path)