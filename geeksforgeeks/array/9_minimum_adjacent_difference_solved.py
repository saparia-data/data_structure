'''
Given an array Arr of N integers arranged in a circular fashion. Your task is to find the minimum absolute difference between adjacent elements.

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines. The first line contains N(size of array). The second line contains N elements of array separated by space.

Output:
For each testcase in new line print the minimum absloute difference.

User Task:
The task is to complete the function minAdjDiff() which returns the minimum difference between adjacent elements in circular array.

Constraint:
1 <= T <= 100
2 <= N <= 106
-106 <= Arr[i] <= 106

Example:
Input:
3
7
8 -8 9 -9 10 -11 12
8
10 -3 -4 7 6 5 -4 -1
8
-1 40 -14 7 6 5 -4 -1

Output:
4
1
0

Explanation:
Testcase 1: The absolute difference between adjacent elements in the given array are as such: 16 17 18  19 21 23 4. 
Among the calculated absolute difference the minimum is 4.

Hint:

1) Initially consider the minimum value to be of first and second elements. Traverse from second element to last. 
Check the difference of every adjacent pair and store the minimum value. When last element is reached, check its difference with first element.

'''

def minAdjDiff(arr, n):
    
    mini = abs(arr[0] - arr[1])
    for i in range(n-1):
        diff = abs(arr[i] - arr[i+1])
        if(mini > diff):
            mini = diff
    if(abs(arr[n-1] - arr[0]) < mini):
        mini = abs(arr[n-1] - arr[0])
    return mini

arr = [8,-8,9,-9,10,-11,12]
n = len(arr)
print(minAdjDiff(arr, n))
        