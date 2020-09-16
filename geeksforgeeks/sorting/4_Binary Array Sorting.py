'''
Given a binary array A[] of size N. The task is to arrange array in increasing order.
Note: The binary array contains only 0  and 1.

Input:
The first line of input contains an integer T, denoting the testcases. 
Every test case contains two lines, first line is N(size of array) and second line is space separated elements of array.

Output:
Space separated elements of sorted arrays. There should be a new line between output of every test case.

Your Task:
This is a function problem. You only need to complete the function binSort() that takes A and N as parameters and sorts the array. 
The printing is done automatically by the driver code.

Constraints:
1 < = T <= 100
1 <= N <= 106
0 <= A[i] <= 1

Example:
Input:
2
5
1 0 1 1 0
10
1 0 1 1 1 1 1 0 0 0
Output:
0 0 1 1 1
0 0 0 0 1 1 1 1 1 1

Explanation:
Testcase 1: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.
Testcase 2: After arranging the elements in increasing orde, elements will be 0 0 0 0 1 1 1 1 1 1.

hints:

1)
Make use of count variables to count number of ones and zeroes.

'''

def binSort(arr, n):
    
    j = -1
    
    for i in range(n):
        
        if(arr[i] < 1):
            j = j + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    return arr

arr = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
n = len(arr)
print(binSort(arr, n))
        