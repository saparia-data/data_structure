'''
Given a Matrix containing 0s and 1s. Find the unit area of the largest region of 1s

Input : M[][5] = { 0 0 1 1 0
                   1 0 1 1 0
                   0 1 0 0 0
                   0 0 0 0 1 }
Output : 6 
In the following example, there are 
2 regions one with length 1 and the 
other as 6. So largest region: 6

Input : M[][5] = { 0 0 1 1 0
                   0 0 1 1 0
                   0 0 0 0 0
                   0 0 0 0 1 }
Output: 4 
In the following example, there are 
2 regions one with length 1 and the 
other as 4. So largest region: 4


https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/

'''

import collections

rr=[-1,-1,-1, 0, 0, 1, 1, 1]
cc=[-1, 0, 1,-1, 1,-1, 0, 1]

def is_valid(matrix, r, c):
    
    if(r < 0 and r >= len(matrix)):
        return False
    if(c < 0 and c >= len(matrix[r])):
        return False
    
    return True

def find_size(matrix, row, col):
    
    q = collections.deque([row, col])
    matrix[row][col] = 2
    ret = 1
    
    while(len(q)):
        
        r = q[0][0]
        c = q[0][1]
        q.popleft()
    
        for i in range(8):
            nextr = r + rr[i]
            nextc = c + cc[i]
            
            if(is_valid(matrix, nextr, nextc)):
                if(matrix[nextr][nextc] == 1):
                    matrix[nextr][nextc] = 2
                    ret += 1
                    q.append([nextr, nextc])
                    
    return ret

def find_max_area(matrix, r, c):
    
    ret = 1
    
    for i in range(r):
        for j in range(c):
            if(martix[i][j] == 1):
                maxArea = max(ret, find_max_area(matrix, i, j))
                
    return maxArea
                    
                    