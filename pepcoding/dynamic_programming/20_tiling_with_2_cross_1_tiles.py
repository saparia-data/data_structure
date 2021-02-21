'''
1. You are given a number n representing the length of a floor space which is 2m wide. It's a 2 * n board.
2. You've an infinite supply of 2 * 1 tiles.
3. You are required to calculate and print the number of ways floor can be tiled using tiles.

Sample Input:

8

Sample Output:

34


https://www.youtube.com/watch?v=dVT9JeUMMDE&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=26


'''
def tiling(n):
    
    dp = [0] * (n+1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]


if __name__ == "__main__":
    
    n = 8
    print(tiling(n))