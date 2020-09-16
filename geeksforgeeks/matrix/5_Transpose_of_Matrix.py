'''
Write a program to find transpose of a square matrix mat[][] of size N*N. Transpose of a matrix is obtained 
by changing rows to columns and columns to rows.

Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. 
Each test case contains an integer N, denoting the size of the square matrix. 
Then in the next line are N*N space separated values of the matrix.

Output:
For each test case output will be the space separated values of the transpose of the matrix

User Task:
The task is to complete the function transpose() which finds the transpose of the matrix. 
The printing is done by the driver code.

Constraints:
1 <= T <= 15
1 <= N <= 20
-103 <= mat[i][j] <= 103

Example:
Input:
2
4
1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4
2
1 2 -9 -2
Output:
1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4
1 -9 2 -2

Explanation:
Testcase 1: The matrix after rotation will be: 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4.
Testcase 2: The matrix after rotation will be: 1 -9 2 -2.

hint:
Swapping the elements at position i, j with element at j, i. 
But, for every row traversal, j should start 1 cell ahead of i.

'''

def transpose(mat,n):
    
    trans = [[0 for i in range(4)] for i in range(4)]
    
    for i in range(n):
        for j in range(n):
            trans[i][j] = mat[j][i]
            
    for i in range(n):
        for j in range(n):
            print(trans[i][j], end = " ")
        print("\n")
        
def transpose2(mat, n):
    
    for i in range(n):
        for j in range(i, n):
            t = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = t
            
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print("\n")
            
            
    
    
n = 4
mat = [ [1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3], 
    [4, 4, 4, 4]]

transpose(mat, n)
print("----------------------------")
transpose2(mat, n)