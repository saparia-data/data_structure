'''
1. You are given a number n, the size of a chess board.
2. You are required to place n number of queens in the n * n cells of board such that no queen can 
   kill another.
3. print all safe configurations of n-queens

Sample Input:

4

Sample Output:

0-1, 1-3, 2-0, 3-2, .
0-2, 1-0, 2-3, 3-1, .

https://www.youtube.com/watch?v=yvt0emtFiIE&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=3

'''
def displayBoard(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end = " ")
        print()

def nQueen(board, row, cols, ndiag, rdiag, asf):
    
    if(row == len(board)):
        print(asf)
        #displayBoard(board)
        return
    
    for col in range(len(board[0])):
        
        if(cols[col] == False and ndiag[row+col] == False and rdiag[row-col+len(board)-1] == False):
            board[row][col] = True # we can place queen here
            cols[col] = True
            ndiag[row+col] = True 
            rdiag[row-col+len(board)-1] = True
            nQueen(board, row+1, cols, ndiag, rdiag, asf + str(row) + "-" + str(col) + ",")
            board[row][col] = False
            cols[col] = False
            ndiag[row+col] = False
            rdiag[row-col+len(board)-1] = False
            

# here we are giving input for 4 cross 4 board
board = [[False for j in range(4)] for i in range(4)]
cols = [False] * len(board)
ndiag = [False] * (2 * len(board)-1)
rdiag = [False] * (2 * len(board)-1)  

nQueen(board, 0, cols, ndiag, rdiag, "")
            