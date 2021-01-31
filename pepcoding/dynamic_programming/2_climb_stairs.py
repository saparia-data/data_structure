'''
1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. In one move, you are allowed to climb 1, 2 or 3 stairs.
4. You are required to print the number of different paths via which you can climb to the top.


Sample Input:
4

Sample Output:
7


https://www.youtube.com/watch?v=A6mOASLl2Dg&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=2


'''
# using memoization
def countPathsMemoization(n, qb):
    
    if(n == 0):
        return 1
    
    elif(n < 0):
        return 0
    
    if(qb[n] > 0):
        return qb[n]
    
    nm1 = countPathsMemoization(n-1, qb)
    nm2 = countPathsMemoization(n-2, qb)
    nm3 = countPathsMemoization(n-3, qb)
    cp = nm1 + nm2 + nm3
    qb[n] = cp
    
    return cp

# using Tabulation

def countPathsTabulation(n):
    
    dp = [0] * (n+1)
    
    dp[0] = 1
    
    for i in range(1, n+1):
        
        if(i == 1):
            dp[i] = dp[i - 1]
        elif(i == 2):
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            
    return dp[n]


if __name__ == "__main__":
    
    n = 4
    qb = [0] * (n+1)
    print(countPathsMemoization(n, qb))
    print(countPathsTabulation(n))