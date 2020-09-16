'''
Given a square matrix mat[][] of size N*N, print the sum of upper and lower triangular elements. 
Upper Triangle consists of elements on the diagonal and above it. Lower triangle consists of elements on the diagonal and below it. 

Input Format:
The first line consists of an integer T i.e number of test cases. 
The first line of each test case consists of an integer N denoting the size of the matrix. 
The next line contains N*N spaced separated integers.

Output Format:
For each testcase, in a new line, print the required output.

Your Task:
This is a function problem. You only need to complete the function sumTriangles that takes n and matrix as parameters 
and prints the sum of upper and lower triangles. The newline is automatically appended by the driver code.

Constraints: 
1 <= T <= 100
1 <= N <= 100
1 <= mat[i][j] <= 100

Example:
Input:
1
3
6 5 4 1 2 5 7 9 7
Output:
29 32

Explanation:
Testcase1: The given matrix is

6 5 4
1 2 5
7 9 7

The elements of upper triangle are
6 5 4
   2 5
      7

Sum of these elements is 6+5+4+2+5+7=29

The elements of lower triangle are
6
1 2
7 9 7

Sum of these elements is 6+1+2+7+9+7= 32.

Hints:

1) The diagonal will contribute to both the sums

def sumTriangles(n, mat):

'''

def sumTriangles(n, mat):
    
    upper_sum = 0
    lower_sum = 0
    
    for i in range(n):
        for j in range(n):
            if(i == j):
                upper_sum += mat[i][j]
                lower_sum += mat[i][j]
            elif(i < j):
                upper_sum += mat[i][j]
            elif( j < i):
                lower_sum += mat[i][j]
                
    return upper_sum, lower_sum

mat = [[ 6, 5, 4 ], [ 1, 2, 5 ], [ 7, 9, 7 ]]

n = 3

upper, lower = sumTriangles(n, mat)
print(upper, lower)


