'''
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block 
i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. 
A rat starts from source and has to reach destination. The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is dead end and non-zero number means the block can be used in the path from source to destination. 
The non-zero value of mat[i][j] indicates number of maximum jumps rat can make from cell mat[i][j].

In this variation, Rat is allowed to jump multiple steps at a time instead of 1.

rat in maze --> https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

https://www.geeksforgeeks.org/rat-in-a-maze-with-multiple-steps-jump-allowed/

'''
N = 4

def printSolution(sol): 
    for i in range(N): 
        for j in range(N): 
            print(sol[i][j], end = " ") 
        print()  
          

def isSafe(maze, x, y): 
      
    # if (x, y outside maze) return false  
    if (x >= 0 and x < N and y >= 0 and 
         y < N and maze[x][y] != 0): 
        return True
    return False

def solveMaze(maze): 
    sol = [[0, 0, 0, 0], 
           [0, 0, 0, 0], 
           [0, 0, 0, 0], 
           [0, 0, 0, 0]] 
    if (solveMazeUtil(maze, 0, 0, sol) == False): 
        print("Solution doesn't exist") 
        return False
    printSolution(sol) 
    return True

def solveMazeUtil(maze, x, y, sol): 
      
    # if (x, y is goal) return True  
    if (x == N - 1 and y == N - 1) : 
        sol[x][y] = 1
        return True
          
    # Check if maze[x][y] is valid  
    if (isSafe(maze, x, y) == True): 
          
        # mark x, y as part of solution path  
        sol[x][y] = 1
          

        for i in range(1, N): 
            if (i <= maze[x][y]): 
                  

                if (solveMazeUtil(maze, x + i,  
                                  y, sol) == True):  
                    return True
                      

                if (solveMazeUtil(maze, x,  
                                  y + i, sol) == True): 
                    return True
                
        sol[x][y] = 0
        return False
    
    return False
  
# Driver Code 
maze = [[2, 1, 0, 0], 
        [3, 0, 0, 1], 
        [0, 1, 0, 1], 
        [0, 0, 0, 1]] 
solveMaze(maze)