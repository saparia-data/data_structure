'''
Given a matrix mat[][] of size N x N. The task is to print the elements of the matrix in the snake pattern.


Input:
First line consists of an integer T denoting the number of test cases. First line of each test case consists of N, 
denoting number of elements(N x N) in Matrix. Second line of every test case consists of N x N spaced integers denoting elements of Matrix elements.

Output:
For each testcase, in a new line, print the matrix in snake pattern.

Your Task:
This is a function problem. You only need to complete the function print that takes a matrix and n as parameters and prints the matrix. 
The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= mat[i][j] <= 100

Example:
Input:
2
3
45 48 54 21 89 87 70 78 15
2
1 2 3 4
Output:
45 48 54 87 89 21 70 78 15 
1 2 4 3

Explanation:
Testcase 1: Matrix is as below:
45 48 54
21 89 87
70 78 15

Printing it in snake pattern will lead to the output as 45 48 54 87 89 21 70 78 15.
Testcase 2: Matrix is as below:
1 2 
3 4
Printing it in snake pattern will give output as 1 2 4 3.

hint:
1. Just print in alternating left and right.

'''

def printS(mat):
    
    n = 4
    
    for i in range(n):
        
        if(i % 2 == 0):
            for j in range(4):
                print(mat[i][j], end = " ")
        
        else:
            for j in range(n - 1, -1, -1):
                print(mat[i][j], end = " ")
    
    
    
    
mat = [[ 10, 20, 30, 40 ], 
       [ 15, 25, 35, 45 ], 
       [ 27, 29, 37, 48 ], 
       [ 32, 33, 39, 50 ]]

printS(mat)