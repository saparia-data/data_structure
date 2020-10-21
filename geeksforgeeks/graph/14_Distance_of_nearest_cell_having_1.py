'''
Given a binary matrix. Find the distance of nearest 1 in the matrix for each cell.

You don't need to read input or print anything. Your task is to complete the function nearest() which takes the matrix (mat) 
and its dimensions (N and M) as inputs and returns a matrix of same dimensions 
where the value at index (i, j) in the resultant matrix signifies the minimum distance of 1 in the matrix from mat[i][j].
The distance is calculated as |i1 – i2| + |j1 – j2|, where i1, j1 are the row number 
and column number of the current cell and i2, j2 are the row number and column number of the nearest cell having value 1.

https://www.geeksforgeeks.org/nearest-1-0-binary-matrix/
https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/


'''
from _collections import deque


def nearest(g, n, m):
    
    vis = [[0 for j in range(m)] for i in range(n)]
    sol = [[5005 for i in range(m)] for j in range(n)]
    que = deque()
    
    for i in range(n):
        for j in range(m):
            if(g[i][j] == 1):
                vis[i][j] = 1
                sol[i][j] = 0
                que.append([i, j])
                
    while(len(que)>0):
        x = que[0][0]
        y = que[0][1]
        que.popleft()
        if(x>0 and (not vis[x-1][y])):
            sol[x-1][y] = min(sol[x-1][y], sol[x][y]+1)
            vis[x-1][y] = 1
            que.append([x-1, y])
        if(x<(n-1) and (not vis[x+1][y])):
            sol[x+1][y] = min(sol[x+1][y], sol[x][y]+1)
            vis[x+1][y] = 1
            que.append([x+1, y])
        if(y>0 and (not vis[x][y-1])):
            sol[x][y-1] = min(sol[x][y-1], sol[x][y]+1)
            vis[x][y-1] = 1
            que.append([x, y-1])
        if(y<(m-1) and (not vis[x][y+1])):
            sol[x][y+1] = min(sol[x][y+1], sol[x][y]+1)
            vis[x][y+1] = 1
            que.append([x, y+1])
    # print_sol(sol, n, m)
    return sol