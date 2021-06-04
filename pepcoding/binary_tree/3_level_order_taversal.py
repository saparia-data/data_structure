'''
The function is expected to print tree level by level, left to right.
Each level must be on a separate line and elements of same level should be separated by space


Sample Input:

19
50 25 12 n n 37 30 n n n 75 62 n 70 n n 87 n n

Sample Output:

50 
25 75 
12 37 62 87 
30 70 



https://www.youtube.com/watch?v=u0maCj0o_LY&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=10
https://www.youtube.com/watch?v=U7rLw0jXI0E&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=11


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
        


if __name__ == "__main__":
    
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    
    root = create_binary_tree(arr)
    print(root.data)
    print("##########################################################")
    
    levelOrderTraversal(root)