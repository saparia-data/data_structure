'''
create binary tree:
https://www.youtube.com/watch?v=XV1ADVV6FbQ&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=3

display binary tree:
https://www.youtube.com/watch?v=sYU6AnSJyjo&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=4


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


def display_binary_tree(root):
    
    if(root == None):
        return
    
    val = ""
    val += str(root.left.data) if root.left is not None else "."
    val += " <- " + str(root.data) + " -> "
    val += str(root.right.data) if root.right is not None else "."
    
    print(val)
    
    display_binary_tree(root.left)
    display_binary_tree(root.right)
    
    
    
if __name__ == "__main__":
    
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    
    root = create_binary_tree(arr)
    print(root.data)
    
    display_binary_tree(root)
    