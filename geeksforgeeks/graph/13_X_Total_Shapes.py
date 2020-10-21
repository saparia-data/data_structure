'''
Given N * M string array arr of O's and X's. The task is to find the number of 'X' total shapes.
'X' shape consists of one or more adjacent X's (diagonals not included).

Testcase 1: Given input is like:

OOOOXXO
OXOXOOX
XXXXOXO
OXXXOOO

So, X which are adjacent to each other vertically for horizontally (diagonals not included). 
So, there are 4 different groups in the given matrix.

'''

            
def markConnected(arr, visited, i, j, N, M):
    
    if(arr[i][j] == 'X' and visited[i][j] == False):
        visited[i][j] == True
        
    if(i + 1 < N):
        markConnected(arr, visited, i + 1, j, N, M)
        
    if(i - 1 >= 0):
        markConnected(arr, visited, i - 1, j, N, M)
        
    if(j + 1 < M):
        markConnected(arr, visited, i, j + 1, N, M)
        
    if(j - 1 >=0):
        markConnected(arr, visited, i, j - 1, N, M)
    
    
def getShapesCount(arr, N, M):
    count = 0
    visited = [[False for i in range(3)] for i in range(4) ]
    print(visited)
    
    for i in range(N):
        for j in range(M):
            
            if(arr[i][j] == 'X' and visited[i][j] == False):
                count += 1
                markConnected(arr, visited, i, j, N, M)
                
    return count
        