'''
Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to the size of the Array.

Input:
The first line contains an integer T denoting the total number of test cases. 
In each test cases, the first line contains an integer N denoting the size of array. 
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
In each seperate line, print the array of numbers of size N for each of the considered window size 1, 2 , ..., N respectively.

User Task:
The task is to complete the function printMaxOfMin() which takes the array arr[] 
and its size N as inputs and finds the maximum of minimum of every window size and returns an array containing the result. 

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= T <= 50
1 <= N <= 105
1 <= A[i] <= 106

Example:
Input: 
2
7
10 20 30 50 10 70 30
3
10 20 30
Output: 
70 30 20 10 10 10 10 
30 20 10

Explaination:

Testcase 1:
First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10}, {70} and {30}. Maximum of these minimums is 70.
Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10}, and {30}. Maximum of these minimums is 30.
Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. Maximum of these minimums is 20.
Similarly other elements of output are computed.

Testcase 2: First element in output indicates maximum of minimums of all windows of size 1.Minimums of windows of size 1 are {10} , {20} , {30}. Maximum of these minimums are 30 and similarly other outputs can be computed. 


https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/

'''