'''
Given a Binary Tree and a positive integer k. The task is to count all distinct nodes that are distance k from a leaf node. 
A node is at k distance from a leaf if it is present k levels above the leaf and also, is a direct ancestor of this leaf node. 
If k is more than the height of Binary Tree, then nothing should be counted.



https://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/

https://www.youtube.com/watch?v=ZgT8NXIMF4g

https://www.techiedelight.com/find-all-nodes-at-given-distance-from-leaf-nodes-in-a-binary-tree/

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isLeaf(node):
    
    return node.left is None and node.right is None

def leafNodeDistanceUtil(root, path, s, k):
    
    if(root is None):
        return
    
    if(isLeaf(root) and len(path) >= k):
        s.add(path[-k])
        return
    
    path.append(root)
    
    leafNodeDistanceUtil(root.left, path, s, k)
    leafNodeDistanceUtil(root.right, path, s, k)
    
    path.remove(root)



def leafNodeDistance(root, k):
    
    path = []
    s = set()
    leafNodeDistanceUtil(root, path, s, k)
    
    for ele in s:
        print(ele.data)
        
root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
root.right.left = Node(6)  
root.right.right = Node(7)  
root.right.left.right = Node(8)

leafNodeDistance(root, 1)