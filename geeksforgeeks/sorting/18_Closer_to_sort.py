'''
Given an array arr[] of N integers which is closer sorted (defined below) and an element x. 
The task is to find index of the element x if it is present. If not present, then print -1.
Closer Sorted: First array is sorted, but after sorting some elements are moved to either of the adjacent positions,
i.e, may be to the arr[i+1] or arr[i-1].

Expected Time Complexity: O(Log N)

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array. 
Next line contains the array elements. Last line contains the element to be searched.

Output:
Output the index at which the element is present (0-based), if present, else print "-1".

Your Task:
This is a function problem. You only need to complete the function closer() that arr, N, and x as parameters and returns the index. 
If element is not present, return -1.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= arr[i],x <= 106

Example:
Input:
2
5
3 2 10 4 40
2
4
2 1 4 3
5
Output:
1
-1

Explanation:
Testcase 1: 2 is present at index 1 (0-based indexing) in the given array.
Testcase 2: 5 is not in the array so the output will be -1.

Note: You may assume that the array does not contain any duplicate elements. 

hints:

1)
Complete Solution:
-Use Binary search.
-In binary search, apart from checking the element at mid, also, check for element at mid - 1 and mid +1. Make sure, not to go out of bounds of array.
-Rest is same as binary search.
-Expected time complexity O(logn).

'''
def binarySearch(arr, l, r,  x):

    mid = (l + (r-l)) // 2
    
    
    while(l <= r):
        
        if(arr[mid] == x):
            return mid
        
        # element at mid+1 is equal to x
        if(arr[mid] < r and arr[mid+1] == x):
            return (mid+1)
        
        # if element at mid-1 is equal to x
        if(arr[mid] > l and arr[mid-1] == x):
            return (mid-1)
        
        # if element at mid is greater than x, recruse for left half
        if(arr[mid] > x):
            return binarySearch(arr, l, mid-2, x)
        
        # if element at mid is less than x , recurse for right half
        return binarySearch(arr, mid+2, r, x)
    
    return -1

def closer( arr, n,  x):
    return binarySearch(arr, 0, n-1, x)

arr = [3,2,10,4,40]
n = len(arr)
x = 2
print(closer(arr, n, x))
    
    