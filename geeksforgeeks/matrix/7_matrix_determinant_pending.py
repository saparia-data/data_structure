'''
Given a square matrix mat of size N x N. The task is to find the determinant of this matrix.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer N denoting the size of the matrix. The next line contains the elements of the matrix in row-wise form.

Output:
Print the determinant of the matrix.

Your Task:
This is a function problem. You only need to complete the function determinantOfMatrix() 
that takes matrix and n as parameters and returns determinant.

Constraints:
1 <= T <= 40
1 <= N <= 7
-10 <= mat[i][j] <= 10

Example:
Input:
2
4
1 0 2 -1 3 0 0 5 2 1 4 -3 1 0 5 0
3
1 2 3 4 5 6 7 10 9
Output:
30
12

Explanation:
Testcase 1: Determinant of the given matrix is 30.
Testcase 2: Determinant of the given matrix is 12.

Hints:

For finding the determinant of the matrix most conventional way is cramer's rule. Cramer's rule states that:
Step 1:- Find the cofactor of the elements of any row or column.
Step 2:- Multiply the co-factor with their respective row/column elements.  
Step 3:- Add the results obtained in the step 2 seperately with alternate sign.

'''
def getDeterminant(a,n):