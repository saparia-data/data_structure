'''
Addition is one of the easiest operation to carry out. The same hold true for matrices. Two matrices can be added only if they have the same dimensions. 
The elements at similar positions get added.

You are given two matrices. The first matrix's dimensions are given by n1,m1. The second matrix's dimensions are given by n2,m2. 
You need to add both the matrices. If addition is not possible then print -1.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains four lines of input. 
The first line contains dimensions of the first array n1 and m1. The second line contains n1*m1 elements separated by spaces. The third line contains dimensions of the second array n2 and m2. The fourth line contains n2*m2 elements separated by spaces.

Output Format:
For each testcase, in a new line, print the sum of matrix if possible; else print -1.

Your Task:
This is a function problem. You only need to complete the function sumMatrix that taks n1, m1, n2, m2, matrix1, matrix2 as parameters 
and prints the sum of matrices. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= n1, m1, n2, m2 <= 30
0 <= arri <= 100

Examples:
Input:
1
2 3
1 2 3 4 5 6
2 3
1 3 3 2 3 3
Output:
2 5 6 6 8 9

Explanation:
Testcase 1: Adding each elements in first matrix to the elements with corresponding row and column (cell) of another matrix will result in the sum as 2 5 6 6 8 9.

Hints:

1) addition is simple. Just add two matrices.

def sumMatrix(n1, m1, n2, m2, arr1, arr2):

'''

def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    
    if(n1 != n2 or m1 != m2):
        print(-1, end = "")
        return
    
    ans = [[0 for i in range(m1)] for j in range(n1)]
    print(ans)
    
    for i in range(n1):
        for j in range(m1):
            ans[i][j] = arr1[i][j] + arr2[i][j]
            print(ans[i][j], end = " ")
    
arr1 = [[1,2,3],[4,5,6]]
arr2 = [[7,8,9],[10,11,12]]
n1,m1 = 2, 3
n2,m2 = 2, 3
sumMatrix(n1, m1, n2, m2, arr1, arr2)
    
    
    
    
    