'''
Given a Matrix consisting of 0s and 1s. Find the number of islands of connected 1s present in the matrix. 
Note: A 1 is said to be connected if it has another 1 around it (either of the 8 directions).

https://www.youtube.com/watch?v=__98uL6wst8

'''

def isValid(x,y,n,m):
    
    if(x < n and y < m and x >= 0 and y >= 0):
        return True
    
    return False

def findIslands(a,n,m):
    
    # initialize no of islands
    islands = 0  
    
    # stack to maintain current connected islands
    stack = []
    
    # direction constants for 8 direction moves
    dirs = [-1,0,1]
    
    for i in range(n):
        
        for j in range(m):
            
            # not visited cell
            if(a[i][j] == 1):
                
                # new island found
                islands += 1
                
                # put cell in the stack
                stack.append([i, j])
                
                # till stack is not empty
                while(len(stack)):
                    index = stack.pop()
                    ind_x = index[0]
                    ind_y = index[1]
                    
                    # mark as visited
                    a[ind_x][ind_y] = -1
                    
                    for x_dir in dirs:
                        
                        for y_dir in dirs:
                            
                            if(isValid(ind_x + x_dir, ind_y + y_dir, n, m) and a[ind_x + x_dir][ind_y + y_dir, n, m] == 1):
                                stack.append([ind_x + x_dir, ind_y + y_dir])
                                
    return islands
                            
                    
                