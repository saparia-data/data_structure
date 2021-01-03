'''
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a. The numbers can be 1 or 0 only.
4. You are standing in the top-left corner and have to reach the bottom-right corner. 
5. Only four moves are allowed 't' (1-step up), 'l' (1-step left), 'd' (1-step down) 'r' (1-step right). 
   You can only move to cells which have 0 value in them. You can't move out of the boundaries 
   or in the cells which have value 1 in them (1 means obstacle).
   
   
Sample Input:

8
8
0 1 0 0 0 0 0 0
0 1 0 1 1 1 1 0
0 1 0 1 0 0 0 0
0 1 0 1 0 1 1 1
0 0 0 0 0 0 0 0
0 1 0 1 1 1 1 0
0 1 0 1 1 1 1 0
0 1 0 0 0 0 0 0

Sample Output:

ddddrrttttrrrrrddlllddrrrddd
ddddrrdddrrrrr
ddddrrrrrrrddd


https://www.youtube.com/watch?v=R1URUB6_y2k&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=47

'''

def floodFill(maze, row, col, psf, visited):
    
    if(row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) 
       or maze[row][col] == 1 or visited[row][col] == True):
        
        return
    
    elif(row == len(maze) - 1 and col == len(maze[0]) - 1):
        print(psf)
        return
    
    visited[row][col] = True
    floodFill(maze, row - 1, col, psf + "t", visited)
    floodFill(maze, row, col - 1, psf + "l", visited)
    floodFill(maze, row + 1, col, psf + "d", visited)
    floodFill(maze, row, col + 1, psf + "r", visited)
    visited[row][col] = False
    
    
maze = [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0]
       ]

visited = [[False for i in range(8)] for i in range(8)]

floodFill(maze, 0, 0, "", visited)
        