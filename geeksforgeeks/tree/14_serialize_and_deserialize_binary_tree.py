'''
Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array. 
Now your task is to complete the function serialize which stores the tree into an array A[ ] 
and deSerialize which deserializes the array to tree and returns it.

Note: The structure of tree must be maintained.


'''
# here we will use pre-order traversal for serialization and deserialization

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def serialize(root, arr):
    
    if(root is None):
        arr.append(-1)
        
    arr.append(root.data)
    serialize(root.left, arr)
    serialize(root.right, arr)
    
def deserializeUtil(arr):
    
    if(deserializeUtil.index == len(arr)):
        return None
    
    val = arr[deserializeUtil.index]
    deserializeUtil.index += 1
    
    if(val == -1):
        return None
    
    root = Node(val)
    root.left = deserializeUtil(arr)
    root.right = deserializeUtil(arr)
    
    return root
    
    
def deserialize(arr):
    deserializeUtil.index = 0
    root = deserializeUtil(arr)
    return root