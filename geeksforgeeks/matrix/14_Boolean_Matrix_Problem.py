'''
Given a boolean matrix mat[r][c] of size r X c, modify it such that if a matrix cell mat[i][j] is 1 (or true) 
then make all the cells of ith row and jth column as 1.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is r and c, r is the number of rows and c is the number of columns.
The next r lines contain c elements having either 0 or 1 and separated by spaces.

Output:
Print the modified array.

Your Task:
This is a function problem. You only need to complete the function booleanMatrix that takes r, c, and matrix as parameters 
and prints the modified array. You need to append a newline to separate ouput of individual testcases.

Constraints:
1 ≤ T ≤ 100
1 ≤ r, c ≤ 1000
0 ≤ A[i][j] ≤ 1

Example:
Input:
3
2 2
1 0
0 0
2 3
0 0 0 
0 0 1
4 3
1 0 0
1 0 0
1 0 0
0 0 0
Output:
1 1
1 0
0 0 1 
1 1 1
1 1 1
1 1 1
1 0 0

Explanation:
Testcase1: Since only first element of matrix has 1 (at index 1,1) as value, so first row and first column are modified to 1.
Testcase 2: Since only the last element of matrix has 1 (at index 2,3) , so last row and last column is modified to 1.
Testcase 3: Since first element of 1st,2nd,3rd row of matrix has value 1 
so, 1st column and 1st,2nd,3rd row of matrix has been modified to 1.

hints:

1) Create two temporary arrays row[M] and col[N]. Initialize all values of row[] and col[] as 0.
2) Traverse the input matrix mat[M][N]. If you see an entry mat[i][j] as true, then mark row[i] and col[j] as true.
3) Traverse the input matrix mat[M][N] again. For each entry mat[i][j], check the values of row[i] and col[j]. 
If any of the two values (row[i] or col[j]) is true, then mark mat[i][j] as true.

'''
def booleanMatrix(R, C, mat):
    
    row = [0] * r
    col = [0] * c
    
    print(row)
    print(col)
    
    for i in range(R):
        for j in range(C):
            if(mat[i][j] == 1):
                row[i] = 1
                col[j] = 1
                
    for i in range(R):
        for j in range(C):
            if(row[i] == 1 or col[j] == 1):
                mat[i][j] = 1
                
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = " ")
        print("\n")
        
        
mat = [ [1, 0, 0, 1], 
        [0, 0, 1, 0], 
        [0, 0, 0, 0] ]

r, c = 3, 4
booleanMatrix(r, c, mat)