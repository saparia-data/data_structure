'''

Sample Input:

24

10 20 50 -1 60 -1 -1 30 70 -1 80 110 -1 120 -1 -1 90 -1 -1 40 100 -1 -1 -1

Sample Output:

10 
20 30 40 
50 60 70 80 90 100 
110 120

https://www.youtube.com/watch?v=t4ts_6m4z68&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=15
https://www.youtube.com/watch?v=amG7xun8k4w&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=16

For more approaches:
https://www.youtube.com/watch?v=NuASXwfaFaY&list=PL-Jc9J83PIiEmjuIVDrwR9h5i9TT2CEU_&index=19


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

def levelOrderLinewiseTraversals(root):
    
    mq = [] # main queue
    cq = [] # child queue
    
    mq.append(root)
    
    while(len(mq) > 0):
        node = mq.pop(0)
        print(str(node.data), end = " ")
    
        for child in node.children:
            cq.append(child)
            
        if(len(mq) == 0):
            mq = cq
            cq = []
            print()
            

def levelOrderLinewiseTraversals2(root):
    
    mq = []
    mq.append(root)
    mq.append(None)
    
    while(len(mq) > 0):
        
        node = mq.pop(0)
        
        if(node != None):
            
            print(str(node.data), end = " ")
            
            for child in node.children:
                mq.append(child)
                
        else:
            
            if(len(mq) > 0):
                mq.append(None)
                print()
        
       
        
        


if __name__ == "__main__":
    
    arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    root = create_generic_tree(arr)
    print(root.data)
    #levelOrderLinewiseTraversals(root)
    levelOrderLinewiseTraversals2(root)