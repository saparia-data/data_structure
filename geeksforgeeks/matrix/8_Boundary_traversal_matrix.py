'''
You are given a matrix A of dimensions n1 x m1. 
The task is to perform boundary traversal on the matrix in clockwise manner.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. 
Each testcase two lines of input. The first line contains dimensions of the matrix A, n1 and m1. 
The second line contains n1*m1 elements separated by spaces.

Output:
For each testcase, in a new line, print the boundary traversal of the matrix A.

Your Task:
This is a function problem. You only need to complete the function boundaryTraversal() 
that takes n1, m1 and matrix as parameters and prints the boundary traversal. 
The newline is added automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= n1, m1<= 30
0 <= arri <= 100

Examples:
Input:
4
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4
12 11 10 9 8 7 6 5 4 3 2 1
1 4
1 2 3 4
4 1
1 2 3 4
Output:
1 2 3 4 8 12 16 15 14 13 9 5
12 11 10 9 5 1 2 3 4 8
1 2 3 4
1 2 3 4

Explanation:
Testcase1: The matrix is:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
The boundary traversal is 1 2 3 4 8 12 16 15 14 13 9 5
Testcase 2: Boundary Traversal will be 12 11 10 9 5 1 2 3 4 8.
Testcase 3: Boundary Traversal will be 1 2 3 4.
Testcase 4: Boundary Traversal will be 1 2 3 4.

hints:

Traverse the top boundary first then the right boundary then the bottom boundary 
then the left boundary and print the elements simultaneously.

'''

def BoundaryTraversal(a, n, m):
    """
    a: matrix
    n: no. of rows
    m: no. of columns
    """
    
    if(min(n,m) == 1):
        for row in a:
            print(*row, end = " ")
        return
            
    row_idx, col_idx = 0, 0
    
    #print first row
    while(col_idx < m):
        print(a[row_idx][col_idx], end = " ")
        col_idx += 1
        
        
    #print last column
    col_idx = m - 1
    row_idx += 1
    
    while(row_idx < n):
        print(a[row_idx][col_idx], end = " ")
        row_idx += 1
         
    #print last row
    row_idx = n - 1
    col_idx -= 1
    while(col_idx > -1):
        print(a[row_idx][col_idx], end = " ")
        col_idx -= 1
        
    #print first column
    row_idx -= 1
    col_idx = 0
    while(row_idx > 0):
        print(a[row_idx][col_idx], end = " ")
        row_idx -= 1
        
        
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
n, m = 3, 3        

BoundaryTraversal(a, n, m)