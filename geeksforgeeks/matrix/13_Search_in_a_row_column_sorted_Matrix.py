'''
Given a matrix mat[] of size n x m, where every row and column is sorted in increasing order, and a number x is given. 
The task is to find whether element x is present in the matrix or not.
Expected Time Complexity : O(m + n)

Input:
The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of three lines. 
First line of each test case consist of two space separated integers N and M, 
denoting the number of element in a row and column respectively. 
Second line of each test case consists of N*M space separated integers denoting the elements in the matrix in row major order. 
Third line of each test case contains a single integer x, the element to be searched.

Output:
Corresponding to each test case, print in a new line, 1 if the element x is present in the matrix, otherwise simply print 0.

Your Task:
This is a function problem. You only need to complete the function search that takes n,m, and x as parameters 
and returns either 0 or 1.

Constraints:
1 <= T <= 200
1 <= N, M <= 1000
1 <= mat[][] <= 105
1 <= X <= 1000

Example:
Input:
2
3 3
3 30 38 44 52 54 57 60 69
62
1 6
18 21 27 38 55 67
55
Output:
0
1

Explanation:
Testcase 1: 62 is not present in the matrix, so output is 0.
Testcase 2: 55 is present in the matrix at 5th cell.

hints:

Use Divide and Conquer technique to find the element.

Let x = element we're trying to search for in the matrix.
Let e = current element we're processing in the array.

1) Start with top right element.
2) Loop: compare this element e with x
    i) if e = x, then return position of e, since we found x in the given matrix.
    ii) if e > x then move left to check elements smaller than e (if out of bound of matrix, then return false)
    iii) if e < x then move below to check elements greater than e (if out of bound of matrix, then return false)
3) repeat the i), ii) and iii) until you find the element or return false



'''
#mat is matrix
#n1 is rows
#m1 is cols
#x is element to search
def search(n1, m1, mat, x):
    
    i = 0
    j = n1 - 1
    
    while(i < m1 and j >= 0):
        
        if(mat[i][j] == x):
            print(i,j)
            return 1
            
        if(mat[i][j] > x):
            j -= 1
            
        else:
            i += 1
    
    return 0
    
    
    
    
mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 

n1, m1 = 4, 4
search(n1, m1, mat, 29)