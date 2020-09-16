'''
Given N integer ranges, the task is to find the maximum occurring integer in these ranges. If more than one such integer exits, print the smallest one.
For example consider the following ranges.
[2, 5] = {2, 3, 4, 5}
[1, 3] = {1, 2, 3}
[3, 9] = {3, 4, 5, 6, 7, 8, 9}
The maximum occurred integer in these ranges is 3.

The ranges are given as two arrays L[] and R[].  L[i] consists of starting point of range and R[i] consists of corresponding end point of the range.
The task is to find the maximum occurred integer in all the ranges.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case contains an integer n denoting the size of the ranges. The next two lines contain the n space separated elements of L and R respectively.

Output:
Print the smallest maximum occured integer in all the ranges.

User Task:
The task is to complete the function maxOccured() which returns the maximum occured integer in all ranges.

Constraints:
1 <= T <= 102
1 <= n <= 106
0 <= L[i], R[i] <= 106

Example:
Input:
2
4
1 4 3 1
15 8 5 4
5
1 5 9 13 21
15 8 12 20 30

Output:
4
5

Explanation:
Testcase 1: 4 is the most occurring element after considering all the ranges. So, output is 4.

Hints:

1) We create an array arr[] of size 1000000 (limit given on maximum value of an interval). 
The idea is to add +1 to each Li index and -1 to corresponding Ri index in arr[]. 
After this, find the prefix sum of the array. Adding +1 at Li shows the starting point of ith Range and adding -1 shows the ending point of ith range. 
Finally we return the array index that has maximum prefix sum.

Algorithm to solve the problem:

-Initialize an array arr[] to 0.
-For each range i, add +1 at Li index and -1 at index 1 + Ri of the array.
-Find the prefix sum of the array and find the smallest index having maximum prefix sum.

'''
def maxOccured(L,R,N,maxx):
    i=0
    A = [0] * 11
    while(i<N):
        A[L[i]]+=1
        print(A)
        A[R[i]+1]-=1
        print(A)
        i+=1
    msum=A[0]
    ind=-1
    
    i=1
        
    while(i<=maxx):
        A[i]+=A[i-1]
        print(A)
        if msum<A[i]:
            msum=A[i]
            ind=i
        i+=1
    return ind

L = [2, 1, 3]
R = [5, 3, 9]
maxx = max(R)

print(maxOccured(L, R, 3, maxx))

