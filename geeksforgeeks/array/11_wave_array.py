'''
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it. 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).

Input Format:
The first line contains an integer T, depicting total number of test cases. T testcases follow. 
The first line of each testcase contains an integer N depicting the size of the array. The second line contains N space separated elements of the array.

Output Format:
For each testcase, in a new line, print the array into wave-like array.

User Task:
The task is to complete the function convertToWave() which converts the given array to wave array. The newline is automatically added by the driver code.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
0 ≤ A[i] ≤107

Example:
Input:
2
5
1 2 3 4 5
6
2 4 7 8 9 10

Output:
2 1 4 3 5
4 2 8 7 10 9

Explanation:
Testcase 1: Array elements after sorting it in wave form are 2 1 4 3 5.
Testcase 2: Array elements after sorting it in wave form are 4 2 8 7 10 9.

Hints:

1) You can reach the wave array by swapping the adjacent elements based on some checks.
2) 
This can be done in O(n) time by doing a single traversal of given array. 
The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements,
we don’t need to worry about odd positioned element. Following are simple steps.
1) Traverse all even positioned elements of input array, and do following.
….a) If current element is smaller than previous odd element, swap previous and current.
….b) If current element is smaller than next odd element, swap next and current.

'''

def convertToWave(A,N):
    
    for i in range(0, N - 1, 2):
        
        if(A[i] < A[i + 1]):
            A[i], A[i + 1] = A[i + 1], A[i]
    return A
    
A = [2,4,7,8,9,10]
N = len(A)

print(convertToWave(A, N))
    