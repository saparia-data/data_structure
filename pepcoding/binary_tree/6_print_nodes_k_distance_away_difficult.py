'''
The function is expected to print all nodes which are k distance away in any direction from node with value equal to data.


Sample Input:

19
50 25 12 n n 37 30 n n n 75 62 n 70 n n 87 n n
37
2

Sample Output:

12
50


https://www.youtube.com/watch?v=cH8gtWOrTGY&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=26
https://www.youtube.com/watch?v=B89In5BctFA&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=26


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

def findNode(node, data):
    
    global path
    
    if(node == None):
        return False
    
    if(node.data == data):
        path.append(node)
        return True
    
    fil = findNode(node.left, data) # fil -> find in left
    
    if(fil):
        path.append(node)
        return True
    
    fir = findNode(node.right, data) # fil -> find in right
    
    if(fir):
        path.append(node)
        return True
    
    return False

def printKLevelDown(node, k, blocker):
    
    if(node == None or k < 0 or node.data == blocker):
        return
    
    if(k == 0):
        print(node.data)
        
    printKLevelDown(node.left, k-1, blocker)
    printKLevelDown(node.right, k-1, blocker)


def printKdistanceAway(root, data, k):
    global path
    path = []
    findNode(root, data)
    for i in range(len(path)):
        printKLevelDown(path[i], k-i, None if i == 0 else path[i-1].data)


        


if __name__ == "__main__":
    
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    
    root = create_binary_tree(arr)
    print(root.data)
    print("##########################################################")
    global path
    path = []
    k = 2
    data = 37
    printKdistanceAway(root, data, k)