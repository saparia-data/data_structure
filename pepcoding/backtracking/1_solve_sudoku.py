'''
1. You are give a partially filled 9*9 2-D array(arr) which represents an incomplete sudoku state.
2. You are required to assign the digits from 1 to 9 to the empty cells following some rules.

Rule 1 -> Digits from 1-9 must occur exactly once in each row.
Rule 2 -> Digits from 1-9 must occur exactly once in each column.
Rule 3 -> Digits from 1-9 must occur exactly once in each 3x3 sub-array of the given 2D array.

Sample Input:

3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0

Sample Output:

3 1 6 5 7 8 4 9 2 
5 2 9 1 3 4 7 6 8 
4 8 7 6 2 9 5 3 1 
2 6 3 4 1 5 9 8 7 
9 7 4 8 6 3 1 2 5 
8 5 1 7 9 2 6 4 3 
1 3 8 9 4 7 2 5 6 
6 9 2 3 5 1 8 7 4 
7 4 5 2 8 6 3 1 9 

https://www.youtube.com/watch?v=uyetDh-DyDg&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=1&t=1s

'''

def isValid(board, x, y, val):
    
    n = len(board)
    
    #check for row from 0 to 8
    for i in range(n): 
        if(board[i][y] == val):
            return False
        
    #check for column from 0 to 8
    for j in range(n):
        if(board[x][j] == val):
            return False
    
        
    smi = x//3 * 3 # formula to get starting row of sub matrix
    smj = y//3 * 3 # formula to get starting col of sub matrix
    
    # check for sub matrix
    for i in range(3):
        for j in range(3):
            if(board[i+smi][j+smj] == val):
                return False
            
    return True
        

def solveSudoku(board, i, j):
    
    if(i == len(board)):
        displayBoard(board)
        return
    
    ni = 0  # next i
    nj = 0  # next j
    
    if(j == len(board[0]) - 1):
        ni = i + 1
        nj = 0
    else:
        ni = i
        nj = j + 1
    
    if(board[i][j] != 0):
        solveSudoku(board, ni, nj)
        
    else:
        for po in range(1, 10):
            if(isValid(board, i, j, po)):
                board[i][j] = po # possible option
                solveSudoku(board, ni, nj)
                board[i][j] = 0
    
def displayBoard(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end = " ")
        print()


        
grid =[
        [3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ] 

solveSudoku(grid, 0, 0)