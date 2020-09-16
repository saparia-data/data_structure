'''
Given a sorted array arr[] of N integers and a number K is given. The task is to check if the element K is present in the array or not.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array 
and the number K seperated by space. Next line contains N elements.

Output:
For each testcase, if the element is present in the array print "1" (without quotes), else print "-1" (without quotes).

User Task:
The task is to complete the function searchInSorted() which searches for an element in sorted array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= K <= 106
1 <= arr[i] <= 106

Example:
Input:
2
5 6
1 2 3 4 6
5 2
1 3 4 5 6

Output:
1
-1

Explanation:
Testcase 1: Since, 6 is present in the array at index 4 (0-based indexing), so output is 1.
Testcase 2: Since, 2 is not present in the array, so output is -1.

Hints:

1) Since the array is sorted, you may use binary search.

2)
-Start traversing through the array using binary search.
-Follow the steps below:
i. Take two pointers low and high with low at oth index and high at n-1th index.
ii. Go for middle element, if it matches with the key, then success, else, check if the middle element is greater of less than the key.
iii. If middle element is less than key, then low will be jumped to mid+1, and high will remain same.
iv. If middle element is greater than key, then low will remain same and high will come down to mid-1.
Steps in 2 will continue till element is found or low <= high.
If element is found, print 1, else print -1.

def searchInSorted(A,N,K):

'''
def binarySearch(A, low, high, K):
    
    while(low <= high):
    
        mid = int((low+high)/2)
        print(mid)
        
        if(A[mid] == K):
            return 1
        
        elif(A[mid] > K):
            return binarySearch(A, low, mid - 1, K)
        else:
            return binarySearch(A, mid + 1, high, K)
        
    else:
        return -1
        
def searchInSorted(A,N,K):
    #Your code here
    low = 0
    high = N
    res =  binarySearch(A, low, high, K)
    return res

A = [1,2,3,4,5,6]
N = len(A)
K = 5
print(searchInSorted(A, N, K))
    

