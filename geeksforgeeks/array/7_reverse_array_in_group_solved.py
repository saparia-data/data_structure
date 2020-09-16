'''
Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.

Input Format:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines of input. The first line of each test case consists of an integer N(size of array) and an integer K separated by a space. The second line of each test case contains N space separated integers denoting the array elements.

Output Format:
For each test case, in a new line, print the modified array.

User Task:
The task is to complete the function reverseInGroups() which reverses elements of the array in groups and returns the array. The printing of array is done by drivercode.

Constraints:
1 ≤ T ≤ 200
1 ≤ N, K ≤ 107
1 ≤ A[i] ≤ 1018

Example:
Input
2
5 3
1 2 3 4 5
4 3
5 6 8 9

Output
3 2 1 5 4
8 6 5 9

Explanation:
Testcase 1: Reversing groups in size 3, first group consists of elements 1, 2, 3. Reversing this group, we have elements in order as 3, 2, 1.
'''
def reverseInGroups(A,N,K):
    i = 0

    while(i < N):

        start = i
        #handle if K is not multiple of N
        end = min(i + (K-1), N - 1)
        print(end,i)
        while(start < end):
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        i += K
    return A
        
        
arr = [1,2,3,4,5,6,7]
n = len(arr)
print(reverseInGroups(arr, n, 3))