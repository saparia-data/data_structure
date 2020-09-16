'''
Given a binary tree with a value associated with each node, 
we need to choose a subset of these nodes such that sum of chosen nodes is maximum under a constraint that no two chosen node in subset 
should be directly connected that is, if we have taken a node in our sum then we can’t take its any children in consideration and vice versa.

     1
   /   \
  2     3
 /     / \
1     4   5

In above binary tree, sum of nodes 2, 4 and 5 = 11 is maximum
https://www.geeksforgeeks.org/maximum-sum-nodes-binary-tree-no-two-adjacent/

Try to solve this using dynamic programming

'''

def maxSumHelper(root) : 
    if (root == None):  
        sum = [0, 0]  
        return sum
    sum1 = maxSumHelper(root.left)  
    sum2 = maxSumHelper(root.right)  
    sum = [0, 0] 
    sum[0] = sum1[1] + sum2[1] + root.data  
    sum[1] = (max(sum1[0], sum1[1]) + 
              max(sum2[0], sum2[1]))
    return sum
  
def getMaxSum(root) : 
  
    res = maxSumHelper(root)  
    return max(res[0], res[1])