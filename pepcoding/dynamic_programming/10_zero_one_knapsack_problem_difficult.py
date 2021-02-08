'''
1. You are given a number n, representing the count of items.
2. You are given n numbers, representing the values of n items.
3. You are given n numbers, representing the weights of n items.
3. You are given a number "cap", which is the capacity of a bag you've.
4. You are required to calculate and print the maximum value that can be created in the bag without 
   overflowing it's capacity.

Note -> Each item can be taken 0 or 1 number of times. You are not allowed to put the same item 
        again and again.
        

Sample Input:

5

15 14 10 45 30
2 5 1 3 4

7

Sample Output:

75


https://www.youtube.com/watch?v=bUSaenttI24&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=16


'''

def zeroOneKnapsack(n, wts, vals, capacity):
    
    dp = [[0 for i in range(capacity+1)] for j in range(n+1)]
    #print(dp)
    
    for i in range(1, len(dp)):
        
        for j in range(1, len(dp[0])):
            
            if(j >= wts[i - 1]):
                
                rCap = j - wts[i - 1] # remaining capacity
                
                if(dp[i - 1][rCap] + vals[i - 1] > dp[i - 1][j]):
                    dp[i][j] = dp[i - 1][rCap] + vals[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
            else:
                dp[i][j] = dp[i - 1][j]
                
    #print(dp)
    return dp[n][capacity]



if __name__ == "__main__":
    
    n = 5
    vals = [15, 14, 10, 45, 30]
    wts = [2, 5, 1, 3, 4]
    capacity = 7
    
    print(zeroOneKnapsack(n, wts, vals, capacity))