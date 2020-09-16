'''
The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the spiral level order would be 10 30 20 40 60 

https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form-using-one-stack-and-one-queue/

https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/

'''

class Node:  
    def __init__(self, key):  
        self.key = key  
        self.left = self.right = None
        
# using one queue and one stack
def printSpiralUsingOneStack(root):
    
    if(root is None):
        return
    
    s = []
    q = []
    reverse = False
    q.append(root)
    
    while(len(q)):
        
        size = len(q)
        
        while(size > 0):
            p = q[0]
            q.pop(0)
            
            if(reverse):
                s.append(p.key)
            else:
                print(p.key, end = " ")
                
            if(p.left is not None):
                q.append(p.left)
                
            if(p.right is not None):
                q.append(p.right)
                
            size -= 1
            
        if(reverse):
            while(len(s)):
                print(s[-1], end = " ")
                s.pop()
                
        reverse = not reverse
        
#using two stacks
def printSpiralUsing2Stacks(root):
    
    if (root == None): 
        return # None check  
  
    # Create two stacks to store  
    # alternate levels  
    s1 = [] # For levels to be printed  
            # from right to left  
    s2 = [] # For levels to be printed  
            # from left to right  
  
    # append first level to first stack 's1'  
    s1.append(root)  
  
    # Keep printing while any of the  
    # stacks has some nodes  
    while not len(s1) == 0 or not len(s2) == 0: 
          
        # Print nodes of current level from s1  
        # and append nodes of next level to s2  
        while not len(s1) == 0: 
            temp = s1[-1]  
            s1.pop()  
            print(temp.key, end = " ")  
  
            # Note that is right is appended 
            # before left  
            if(temp.left):  
                s2.append(temp.left)  
            if(temp.right): 
                s2.append(temp.right) 
  
        # Print nodes of current level from s2  
        # and append nodes of next level to s1  
        while (not len(s2) == 0): 
            temp = s2[-1]  
            s2.pop()  
            print(temp.key, end = " ")  
  
            # Note that is left is appended 
            # before right  
            if (temp.right): 
                s1.append(temp.right)  
            if (temp.left):  
                s1.append(temp.left) 
        
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
printSpiralUsingOneStack(root) 
print("\n")
printSpiralUsing2Stacks(root)