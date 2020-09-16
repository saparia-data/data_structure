'''
Given a square matrix mat[][] of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. 
The first line of each test case consists of an integer N, where N is the size of the square matrix. 
The second line of each test case contains N x N space separated values of the matrix mat.

Output:
Corresponding to each test case, in a new line, print the rotated matrix. 

User Task:
The task is to complete the function rotateby90() which rotates the input matrix by 90 degree. 
You just need to rotate the matrix, printing the matrix will be automatically done the driver code.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 50
1 <= mat[][] <= 100

Example:
Input:
3
3
1 2 3 4 5 6 7 8 9
2
1 2 3 4
1
80
Output:
3 6 9 2 5 8 1 4 7
2 4 1 3
80

Explanation:
Testcase 1: Matrix is as below:
1 2 3
4 5 6
7 8 9

Rotating it by 90 degrees in anticlockwise directions will result as below matrix:
3 6 9
2 5 8
1 4 7
Testcase 2: Matrix is as below:
1 2
3 4
After rotating by 90 degree , matrix will be 
2 4
1 3
Testcase 3: Matrix is as below:
80
After rotating by 90 degree , matrix will be 
80

hints:

1)
A N x N matrix will have floor(N/2) square cycles. For example, a 4 X 4 matrix will have 2 cycles. 
The first cycle is formed by its 1st row, last column, last row and 1st column. 
The second cycle is formed by 2nd row, second-last column, second-last row and 2nd column.

The idea is for each square cycle, we swap the elements involved with the corresponding cell in the matrix in anti-clockwise direction 
i.e. from top to left, left to bottom, bottom to right and from right to top one at a time. We use nothing but a temporary variable to achieve this.

2)
First Cycle (Involves Red Elements)
 1  2  3 4 
 5  6  7  8 
 9 10 11 12 
 13 14 15 16 

 
Moving first group of four elements (First
elements of 1st row, last row, 1st column 
and last column) of first cycle in counter
clockwise. 
 4  2  3 16
 5  6  7 8 
 9 10 11 12 
 1 14  15 13 
 
Moving next group of four elements of 
first cycle in counter clockwise 
 4  8  3 16 
 5  6  7  15  
 2  10 11 12 
 1  14  9 13 

Moving final group of four elements of 
first cycle in counter clockwise 
 4  8 12 16 
 3  6  7 15 
 2 10 11 14 
 1  5  9 13 


Second Cycle (Involves Blue Elements)
 4  8 12 16 
 3  6 7  15 
 2  10 11 14 
 1  5  9 13 

Fixing second cycle
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
'''

def transpose(a, n):
    
    for i in range(n):
        for j in range(i, n):
            t = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = t
            
def reverseColumn(a, n):
    
    for i in range(n):
        j = 0
        k = n - 1
        while j < k:
            t = a[j][i]
            a[j][i] = a[k][i]
            a[k][i] = t
            j += 1
            k -= 1

def rotateby90(a, n):
    
    transpose(a, n)
    reverseColumn(a, n)
    
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("\n")
    
    
    
n = 4
a = [[1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16] ]

rotateby90(a, n)
    

    
    
    
    