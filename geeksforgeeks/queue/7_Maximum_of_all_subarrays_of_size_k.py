'''
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The first line of each test case contains a single integer N denoting the size of array and the size of subarray K. 
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each testcase, in a new line, print the maximum for every subarray of size k.

Your Task:
This is a function problem. You only need to complete the function max_of_subarrays that returns an array of answer. 
The printing is automatically done by the driver code.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ A[i] <= 107

Example:
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13
Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90

Explanation:
Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum. Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.
Testcase 2: Starting from first subarray of size k =, we have 10 as maximum. Moving the window forward maximum elements are as follows 10 10 10 15 15 90 90.

hints:

-We create a Deque, Qi of capacity k, that stores only useful elements of current window of k elements. 
-An element is useful if it is in current window and is greater than all other elements on left side of it in current window. 
-We process all array elements one by one and maintain Qi to contain useful elements of current window and these useful elements are maintained in sorted order. 
-The element at front of the Qi is the largest and element at rear of Qi is the smallest of current window.

'''
from _collections import deque


def max_of_subarrays(arr,n,k):
    
    res = []
    
    d = deque()
    
    for i in range(k):
        while(len(d) and arr[i] >= arr[d[-1]]):
            d.pop()
            
    d.append(i)
    
    for i in range(k, n):
        
        res.append(arr[d[0]])
        
        while(len(d) and d[0] <= i - k):
            d.popleft()
            
        while len(d) and arr[i]>=arr[d[-1]]:
            d.pop()
            
        d.append(i)
        
    res.append(arr[d[0]])
    
    return res

arr = [12, 1, 78, 90, 57, 89, 56] 
k = 3
print(max_of_subarrays(arr, len(arr), k)) 