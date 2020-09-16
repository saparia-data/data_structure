'''
Given a Binary Tree with all unique values and two nodes value n1 and n2. The task is to find the lowest common ancestor of the given two nodes. 
We may assume that either both n1 and n2 are present in the tree or none of them is present. 

The tree is
          5
        /
      2
     /   \
   3     4
The lowest common ancestor of given nodes 3 and 4 is 2.

hints:

Following is simple O(n) algorithm to find LCA of n1 and n2.
1) Find path from root to n1 and store it in a vector or array.
2) Find path from root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.


iterative solution:
https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

https://www.youtube.com/watch?v=F-_1sbnPbWQ

'''
def lca(root, n1, n2):
    # base case
    if root is None:
        return None
        
    # If either n1 or n2 matches with root's key, report 
    #  the presence by returning root (Note that if a key is 
    #  ancestor of other, then the ancestor key becomes LCA 
    if root.data == n1 or root.data == n2:
        return root
        
    # Look for keys in left and right subtrees 
    left_lca = lca(root.left, n1, n2) 
    right_lca = lca(root.right, n1, n2)
    
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca:
        return root
        
    # Otherwise check if left subtree or right subtree is LCA 
    if left_lca is not None:
        return left_lca
    else:
        return right_lca