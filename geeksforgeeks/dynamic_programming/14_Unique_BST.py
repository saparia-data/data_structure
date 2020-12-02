'''
Given an integer. Find how many structurally unique binary search trees are there that stores the values from 1 to that integer (inclusive). 

Example 1:
Input:
N = 2
Output: 2
Explanation:for N = 2, there are 2 unique
BSTs
     1               2  
      \            /
       2         1


Example 2:
Input:
N = 3
Output: 5
Explanation: for N = 3, there are 5
possible BSTs
  1           3     3       2     1
    \        /     /      /  \     \
     3      2     1      1    3     2
    /      /       \                 \
   2      1         2                 3

https://www.geeksforgeeks.org/number-of-unique-bst-with-a-given-key-dynamic-programming/

'''

def numTrees(n):  
  
    # DP to store the number of unique 
    # BST with key i  
    dp = [0] * (n + 1)  
  
    # Base case  
    dp[0] = 1
    #dp[1] = 1
  
    # fill the dp table in top-down  
    # approach.  
    for i in range(1, n + 1):  
        for j in range(i):  
    
            dp[i] = dp[i] + (dp[j] * dp[i - j - 1])  
            #if( dp[i] >= 1000000007 ):
                #dp[i] = dp[i] % 1000000007
    return dp[n]

n = 4
print(numTrees(n))