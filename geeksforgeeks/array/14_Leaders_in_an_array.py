'''
Given an array A of positive integers. Your task is to find the leaders in the array.

Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader. 

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each testcase, in a new line, the leaders will be printed.

User Task:
The task is to complete the function leader() which returns an array of leaders in same order as they appear in the array.
The printing is automatically done by driver code.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= Ai <= 107

Example:
Input:
4
6
16 17 4 3 5 2
5
1 2 3 4 0
5
7 4 5 7 3
3
4 1 4

Output:
17 5 2
4 0
7 7 3
4 4

Explanation:
Testcase 1: The first leader is 17 as it is greater than all the elements to its right.
Similarly, the next leader is 5. The right most element is always a leader so it is also included.

Testcase 2: 4 and 0 are leaders.

Testcase 3: All elements on the right of 7 (at index 0) are smaller than or equal to 7.
Also, all the elements of right side of 7 (at index 3) are smaller than 7. And, the last element 3 is itself a leader since no elements are on its right.

Testcase 4: 4 is equal to the 4 on its right so we make it a leader. The other 4 is rightmost so it is also a leader.

'''
def leaders(A,N):
    print(A[N - 1])
    maxx = A[N - 1]
    for i in range(N-2, -1, -1):
        #print(i)
        if(A[i] > maxx):
            maxx = A[i]
            print(maxx)

A = [16,17,4,3,5,2]
N = len(A)

leaders(A, N)
