'''
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
4. You are standing in top-left cell and are required to move to bottom-right cell.
5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom-right cell).
7. You are required to traverse through the matrix and print the cost of path which is least costly.


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

23



https://www.youtube.com/watch?v=D-0souJUBMU&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=6
https://www.youtube.com/watch?v=BzTIOsC0xWM&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=7


'''

def minCostInMaze(arr, n, m):
    
    dp = [[0 for i in range(m)] for j in range(n)]
    #print(dp)
    
    for i in range(len(arr) - 1, -1, -1):
        
        for j in range(len(arr[0]) - 1, -1, -1):
            
            if(i == len(dp) - 1 and j == len(dp[0]) - 1): # at last cell
                dp[i][j] = arr[i][j]
                
            elif(i == len(dp) - 1): # last row
                dp[i][j] = dp[i][j + 1] + arr[i][j]
                
            elif(j == len(dp[0]) - 1): # last column
                dp[i][j] = dp[i + 1][j] + arr[i][j]
                
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + arr[i][j]
                
                
    return dp[0][0]
                


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
    
    print(minCostInMaze(arr, n, m))