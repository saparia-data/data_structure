'''
Given a set of non-negative integers, and a value sum, determine number of subsets of the given set with sum equal to given sum

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: 1  
There is 1 subset (4, 5) with sum 9.

https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

'''

# Recursion solution. Complexity is O(2^n)
def isSubsetSum(set, n, sum):
 
    # Base Cases
    if(n == 0):
        if(sum == 0):
            return 1
        else:
            return 0
 
    # If last element is greater than
    # sum, then ignore it
    #if (set[n - 1] > sum):
     #  return isSubsetSum(set, n - 1, sum)
 
    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(
        set, n-1, sum) + isSubsetSum(
        set, n-1, sum-set[n-1])
        
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
print(isSubsetSum(set, n, sum))

# DP solution
def isSubsetSum_DP(arr, n, sum):
    
    dp = [[None for j in range(sum+1)] for i in range(n+1)]
    print(dp)
    
    for i in range(n+1):
        dp[i][0] = 1
        
    print(dp)
    
    for j in range(1,sum+1):
        dp[0][j] = 0
        
    print(dp)
    
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if(j < arr[i-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j - arr[i-1]]
                
    print(dp)
                
    return dp[n][sum]
        
    
arr = [3, 34, 4, 12, 5, 2]
sum1 = 9
n1 = len(arr)
print(isSubsetSum_DP(arr, n1, sum1))