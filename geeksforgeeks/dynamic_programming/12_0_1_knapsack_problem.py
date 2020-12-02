'''
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] 
such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item, or don't pick it (0-1 property).

Example 1:
Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3

Example 2:
Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0


'''

def knapSack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(W+1):
        dp[0][i] = 0
        
    for i in range(n+1):
        dp[i][0] = 0

    # Build table K[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if(wt[i - 1] > w):
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                

    return dp[n][W]

values = [1,2,3]
weight = [4,5,1]
n = len(values)
print(knapSack(4, weight, values, n))