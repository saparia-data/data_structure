'''
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
4. You are standing in front of left wall and are supposed to dig to the right wall. You can start from 
   any row in the left wall.
5. You are allowed to move 1 cell right-up (d1), 1 cell right (d2) or 1 cell right-down(d3).
6. Each cell has a value that is the amount of gold available in the cell.
7. You are required to identify the maximum amount of gold that can be dug out from the mine.


Sample Input:

6
6

0 1 4 2 8 2
4 3 6 5 0 4
1 2 4 1 4 6
2 0 7 3 2 2
3 1 5 9 2 4
2 7 0 8 5 1

Sample Output:

33


https://www.youtube.com/watch?v=5KdvH15NJjc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=8
https://www.youtube.com/watch?v=hs0lilfJ7C0&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=9


'''

def pathWithMaxGold(arr, n, m):
    
    dp = [[0 for i in range(m)] for j in range(n)]
    #print(dp)
    
    for j in range(len(arr[0]) - 1, -1, -1): # start with last column last cell
        
        for i in range(len(arr) - 1, -1, -1):
            
            if(j == len(arr[0]) - 1): # if j is in last column
                dp[i][j] = arr[i][j]
                
            elif(i == 0): # if i is in first row
                dp[i][j] = arr[i][j] + max(dp[i][j + 1], dp[i + 1][j + 1])
                
            elif(i == len(arr) - 1):
                dp[i][j] = arr[i][j] + max(dp[i][j + 1], dp[i - 1][j + 1]);
                
            else:
                dp[i][j] = arr[i][j] + max(dp[i][j + 1], dp[i - 1][j + 1], dp[i + 1][j + 1])
                
    maxx = dp[0][0]
    
    for i in range(1, len(dp)):
        
        if(dp[i][0] > maxx):
            maxx = dp[i][0]
            
    return maxx




if __name__ == "__main__":
    
    n = 6
    m = 6
    
    arr = [
            [0 ,1 ,4 ,2 ,8 ,2],
            [4 ,3 ,6 ,5 ,0 ,4],
            [1 ,2 ,4 ,1 ,4 ,6],
            [2 ,0 ,7 ,3 ,2 ,2],
            [3 ,1 ,5 ,9 ,2 ,4],
            [2 ,7 ,0 ,8 ,5 ,1]
          ]
    
    print(pathWithMaxGold(arr, n, m))