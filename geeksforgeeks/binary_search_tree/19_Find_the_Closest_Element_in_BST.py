'''
Given a BST and an integer. Find the least absolute difference between any node value of the BST and the given integer.

Input:
        10
      /   \
     2    11
   /  \ 
  1    5
      /  \
     3    6
      \
       4
       
K = 13
Output: 2
Explanation: K=13. The node that has
value nearest to K is 11. so the answer
is 2


Input:

      8
    /   \
   1     9
    \     \
     4    10
    /
   3
   
K = 9
Output: 0
Explanation: K=9. The node that has
value nearest to K is 9. so the answer
is 0.


'''

def minDiff(root, k):
    
    if(root is None):
        return 9999999999
    
    if(root.data == k):
        return 0
    
    if (root.data > k):
        return min( abs(root.data-k) , minDiff(root.left,k) )
    
    return min( abs(root.data-k) , minDiff(root.right,k) )