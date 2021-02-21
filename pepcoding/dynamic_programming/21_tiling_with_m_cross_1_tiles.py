'''
1. You are given a number n and a number m separated by line-break representing the length and breadth of a n * m floor.
2. You've an infinite supply of m * 1 tiles.
3. You are required to calculate and print the number of ways floor can be tiled using tiles.

Input Format:

A number n
A number m

Sample Input:

39
16

Sample Output:

61


https://www.youtube.com/watch?v=_c_R-uIi-zU&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=27


'''

def tiling(n, m):
    
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        
        if(i < m):
            dp[i] = 1
            
        elif(i == m):
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-m]
            
    return dp[n]


if __name__ == "__main__":
    
    n = 39
    m = 16
    print(tiling(n, m))