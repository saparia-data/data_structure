'''
Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product, with the elements of the subsequence being in increasing order.

Input: 
The first line of input contains number of testcases T. Each testcase contains 2 lines, the first line contains N, 
the number of elements in array, and second line contains space separated elements of array.

Output: 
Print the subsequence of size 3 having maximum product, numbers of subsequence being in increasing order. 
If no such sequence exists, print "Not Present".

User Task:
The task is to complete the function maxProductSubsequence() which finds maximum product of increasing subsequence of size 3. 
You should store answer in res array. The driver code prints the res array.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 105

Example:
Input:
3
8
6 7 8 1 2 3 9 10
4
3 4 2 1
6
1 2 20 10 11 12

Ouput:
8 9 10
-1
10 11 12

Explanation:
Testcase 1: 3 increasing elements of the given arrays are 8, 9 and 10 which forms the subsequence of size 3 with maximum product.

refer -> https://www.youtube.com/watch?v=99ssGWhLPUE use dynamic programming

'''