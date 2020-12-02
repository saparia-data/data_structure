'''
Given an integer N denoting the Length of a line segment. You need to cut the line segment 
in such a way that the cut length of a line segment each time is either x , y or z. Here x, y, and z are integers.
After performing all the cut operations, your total number of cut segments must be maximum.

Example 1:
Input:
N = 4
x = 2, y = 1, z = 1
Output: 4
Explanation:Total length is 4, and the cut
lengths are 2, 1 and 1.  We can make
maximum 4 segments each of length 1.

Example 2:
Input:
N = 5
x = 5, y = 3, z = 2
Output: 2
Explanation: Here total length is 5, and
the cut lengths are 5, 3 and 2. We can
make two segments of lengths 3 and 2.


'''
def maximizeTheCuts(n, p, q, r): 
  
    dp = [-1]*(n + 1)  
  
    dp[0] = 0
  
    for i in range(n+1) : 
  
        if (dp[i] == -1): 
            continue
 
        if (i + p <= n): 
            dp[i + p] = (max(dp[i + p], dp[i] + 1)) 
  
       
        if (i + q <= n): 
            dp[i + q] = (max(dp[i + q], dp[i] + 1)) 
  
        
        if (i + r <= n): 
            dp[i + r] = (max(dp[i + r], dp[i] + 1)) 
  
    if(dp[n] == -1):
        return 0
    
    return dp[n]

n = 5
p = 5
q = 3
r = 2
print(maximizeTheCuts(n, p, q, r)) 