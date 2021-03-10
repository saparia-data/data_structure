'''
While traversing the function must print following content in different situations.
   2.1. When the control reaches the node for the first time -> "Node Pre" node.data.
   2.2. Before the control leaves for a child node from a node -> "Edge Pre" node.data--child.data.
   2.3. After the control comes back to a node from a child -> "Edge Post" node.data--child.data.
   2.4. When the control is about to leave node, after the children have been visited -> "Node Post" node.data.
   
   
Sample Input:

12

10 20 -1 30 50 -1 60 -1 -1 40 -1 -1

Sample Output:

Node Pre 10
Edge Pre 10--20
Node Pre 20
Node Post 20
Edge Post 10--20
Edge Pre 10--30
Node Pre 30
Edge Pre 30--50
Node Pre 50
Node Post 50
Edge Post 30--50
Edge Pre 30--60
Node Pre 60
Node Post 60
Edge Post 30--60
Node Post 30
Edge Post 10--30
Edge Pre 10--40
Node Pre 40
Node Post 40
Edge Post 10--40
Node Post 10



https://www.youtube.com/watch?v=kL6tIGhVW1k&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=10
https://www.youtube.com/watch?v=YnufWAWOfI8&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=11



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

def traversals(root):
    
    print("Node Pre " + str(root.data))
    
    for child in root.children:
        print("Edge Pre " + str(root.data) + "--" + str(child.data))
        traversals(child)
        print("Edge Post " + str(root.data) + "--"  + str(child.data))
        
    print("Node Post " + str(root.data))


if __name__ == "__main__":
    
    arr = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    root = create_generic_tree(arr)
    print(root.data)
    traversals(root)