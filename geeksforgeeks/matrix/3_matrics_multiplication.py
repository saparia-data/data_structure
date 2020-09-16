'''
When dealing with matrices, you may, sooner or later, run into the elusive task of matrix multiplication. 
Here, we will try to multiply two matrices and hope to understand the process.

Two matrices A[][] and B[][] can only be multiplied if A's column size is equal to B's row size. 
The resultant matrix will have dimensions equal to A's row size and B's column size.
You are given two matrices A and B. A is of dimension n1 x m1; and B is of dimension n2 x m2. 
You have to multiply A with B and print the resultant matrix. If multiplication is not possible then print -1.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. 
Each testcase contains four lines of input. The first line contains dimensions of the first array n1 and m1. 
The second line contains n1 * m1 elements separated by spaces. The third line contains dimensions of the second array n2 and m2. 
The fourth line contains n2 * m2 elements separated by spaces.

Output:
For each testcase, in a new line, print the resultant matrix if possible; else print -1.

Your Task:
This is a function problem. You only need to complete the function multiplyMatrix that takes n1,m2,n2,m2,matrix1,matrix2 as parameters 
and prints the multiplied matrix. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= n1, m1, n2, m2 <= 30
0 <= arri <= 100

Examples:
Input:
2
3 2
4 8 0 2 1 6
2 2
5 2 9 4
1 1
2
1 1
3
Output:
92 40 18 8 59 26
6

Explanation:
Testcase 1: Matrices are of size 3 x 2 and 2 x 2 which results in 3 x 2 matrix with elements as 92, 40, 18, 8, 59, 26.
Testcase 2: Matrices are of size 1 x 1 and 1 x 1 which results in 1 x 1 matrix having element 6.

Hints:
1)
if columns of matrix 1 is not equal to rows of matrix 2 then multiplication is not possible
If we multiply a 2 x 3 matrix with a 3 x 1 matrix, the product matrix is 2 x 1

https://www.youtube.com/watch?v=DmHfB7o6vKc

'''
def multiplyMatrix(n1, m1, n2, m2, arr1, arr2): 
    
    R = [[0, 0, 0, 0],  
        [0, 0, 0, 0],  
        [0, 0, 0, 0], 
        [0, 0, 0, 0]]
    
    for i in range(n1):
        for j in range(n2):
            for k in range(n1):
                R[i][j] += arr1[i][k] * arr2[k][j]
                
    for i in range(n1):  
        for j in range(n2): 
            print(R[i][j],end=" ") 
        print("\n")
    
arr1 = [[1, 1, 1, 1],  
    [2, 2, 2, 2],  
    [3, 3, 3, 3], 
    [4, 4, 4, 4]] 


arr2 = [[1, 1, 1, 1],  
    [2, 2, 2, 2],  
    [3, 3, 3, 3], 
    [4, 4, 4, 4]]

n1, m1, n2, m2 = 4,4,4,4

multiplyMatrix(n1, m1, n2, m2, arr1, arr2)
