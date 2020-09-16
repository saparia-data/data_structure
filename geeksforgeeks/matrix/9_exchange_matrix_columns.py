'''
You are given a matrix A of dimensions n1 x m1. 
You have to exchange A's first column with last column.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. 
Each testcase contains two lines of input. The first line contains dimensions of the matrix A, n1 and m1. 
The second line contains n1*m1 elements of matrix separated by spaces.

Output:
For each testcase, in a new line, print the resultant matrix.

User Task:
The task is to complete the function exchangeColumns() which is used to do required operation on matrix. 
The addition of newline is automatically done by the driver code.

Constraints:
1 <= T <= 100
1 <= n1, m1<= 30
0 <= arr[i] <= 100

Examples:
Input:
2
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
2 3
4 3 2 1 5 6
Output:
4 2 3 1 8 6 7 5 12 10 11 9 16 14 15 13
2 3 4 6 5 1

Explanation:
Testcases 1: Matrix is as follow:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

After exchanging first  column with last column, we have matrix as follows:
4 2 3 1
8 6 7 5
12 10 11 9
16 14 15 13
Testcase 2: Matrix is as follows:
4 3 2
1 5 6
After exchanging columns matrix will be:
2 3 4
6 5 1.

hints:

Use a temp variable and swap both the columns.

'''
#arr1 is matrix
#n1,m1 are dimension
def exchangeColumns(n1, m1, arr1):
    
    for i in range(m1):
        t = arr1[i][0]
        arr1[i][0] = arr1[i][m1 - 1]
        arr1[i][m1 - 1] = t
        
    for i in range(n1):
        for j in range(m1):
            print(arr1[i][j], end = " ")
        print("\n")
    
    
arr1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

n1, m1 = 3, 3

exchangeColumns(n1, m1, arr1)