'''
Given a binary sorted non-increasing array arr of size N. You need to print the count of 1's in the binary array.

Input:
The input line contains T, denotes the number of test cases. Each input contains two lines. 
The first line contains N(size of binary array). 
The second line contains N elements of binary array separated by space.

Output:
For each test case in new line, print the count 1's in binary array.

User Task:
The task is to complete the function countOne() which return count of 1s in the input array.

Constraint:
1 <= T <= 100
1 <= N <= 5*106
0 <= arr[i] <= 1

Example:
Input:
2
8
1 1 1 1 1 0 0 0
8
1 1 0 0 0 0 0 0

Output:
5
2

Explanation:
Testcase 1: Number of 1's in given binary array : 1 1 1 1 1 0 0 0 is 5.

Hints:

1) Use binary search
2)
-You need to find the upperbound index of 1, ie., the last index at which 1 is present. 
So that, number of 1s can be deducted by subtracting this index with 0.
-Take two pointers as low and high at 0th and (n-1)th index initially and a middle at (low+high/2).
-Check for middle element, if it is 1, it means we need to check for the index afterwards mid.
-Go for the window afterward mid by jumping low to mid+1.
-If mid element is not 1, then we need to recurse for the lower half by decreasing the high to mid-1.
-Recurse for the above step.

def countOnes(A,N):

'''

def countOnesBinary(A, low, high):
    
    if(low <= high):
        
        mid = int(low + (high-low)/2)
        
        if((mid == high or A[mid+1]==0) and (A[mid]==1)): 
            return mid+1
        
        if(A[mid]==1): 
            return countOnesBinary(A, (mid+1), high)
        else:
            return countOnesBinary(A, low, mid-1)
             
    return 0  
   

def countOnes(A,N):
    low = 0
    high = N
    print(countOnesBinary(A, low, high))
    
A = [1,1,1,1,0,0,0]
N = len(A)
countOnes(A, N)
    
    
    
    
    
    
    
    