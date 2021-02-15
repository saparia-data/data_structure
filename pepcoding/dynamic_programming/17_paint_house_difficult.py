'''
1. You are given a number n, representing the number of houses.
2. In the next n rows, you are given 3 space separated numbers representing the cost of painting nth house with red or blue or green color.
3. You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.

Input Format:

A number n

n1red n1blue n1green
n2red n2blue n2green
.. n number of elements


Sample Input:

4

1 5 7
5 8 4
3 2 9
1 2 4

Sample Output:

8


https://www.youtube.com/watch?v=kh48JLieeW8&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=23


'''

def paintHouse(arr, n):
    
    dp = [[0 for j in range(len(arr[0]))] for i in range(n)]
    #print(dp)
    
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][2]
    
    for i in range(1, n):
        
        dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        
    #print(dp)
        
    finalAns = min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
    return finalAns


if __name__ == "__main__":
    
    n = 4
    arr = [
            [1, 5, 7],
            [5, 8, 4],
            [3, 2, 9],
            [1, 2, 4]
          ]
    
    print(paintHouse(arr, n))