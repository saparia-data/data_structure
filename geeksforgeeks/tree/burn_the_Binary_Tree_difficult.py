'''
https://stackoverflow.com/questions/52787803/given-a-node-how-long-will-it-take-to-burn-the-whole-binary-tree

https://www.geeksforgeeks.org/burn-the-binary-tree-starting-from-the-target-node/

If we take a closer look we will observe that the time taken to burn the whole tree is equal the longest diameter of the tree.

'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# returns a tuple (max = the longest path so far, dist = current path)
def _recurse(node, start):
    if node is None:
        return (None, 0)
    else:
        max_left, dist_left = _recurse(node.left, start)
        max_right, dist_right = _recurse(node.right, start)
        # this node is the starting node
        if node == start:
            return (0, 0)
        # the starting node is in left or right
        elif max_right is not None or max_left is not None:
            return (dist_right + dist_left + 1,
                    (dist_left if max_right is None else dist_right) + 1)
        # we haven't seen the starting node
        else:
            return (None, max(dist_left, dist_right) + 1)

def time_to_burn(root, start):
    return _recurse(root, start)

# Sample code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)
root.right.right = Node(50)
print ((time_to_burn(root, root.left.right)))