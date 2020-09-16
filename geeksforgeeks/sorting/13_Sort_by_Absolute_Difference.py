'''
Given an array of N elements and a number K. The task is to arrange array elements according to the absolute difference with K,
i. e.,element having minimum difference comes first and so on.
Note : If two or more elements are at equal distance arrange them in same sequence as in the given array.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. 
First line of test case contains two space separated integers N and K. Second line of each test case contains N space separated integers.

Output:
For each test case print the given array in the order as described above.

Your Task:
This is a functional problem. You only need to complete the function sortABS(). The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= K <= 105

Example:
Input:
3
5 7
10 5 3 9 2
5 6
1 2 3 4 5
4 5
2 6 8 3
Output:
5 9 10 3 2
5 4 3 2 1
6 3 2 8

Explanation:
Testcase 1: Sorting the numbers accoding to the absolute difference with 7, we have array elements as 5, 9, 10, 3, 2.
Testcase 2: Sorting the numbers according to the absolute difference with 6, we have array elements as 5 4 3 2 1.
Testcase 3: Sorting the numbers according to the absolute difference with 5, we have array elements as 6 3 2 8.

Input : arr[] : x = 7, arr[] = {10, 5, 3, 9, 2}
Output : arr[] = {5, 9, 10, 3, 2}
Explanation:
7 - 10 = 3(abs)
7 - 5 = 2
7 - 3 = 4 
7 - 9 = 2(abs)
7 - 2 = 5
So according to the difference with X, 
elements are arranged as 5, 9, 10, 3, 2.

hints:

1)
The complete solution:

-Use stable_sort in STL, to sort, and modify it by using mycomparator function.
(Read about Stable sort here - http://www.cplusplus.com/reference/algorithm/stable_sort/).
-In this mycomparator function, if a & b values are passed, then compare a - k and b - k.
-if a- k < b - k then return 1 else return 0.

'''
def sortAbs(a, n, k):
    
    a = sorted(a, key = lambda x: abs(x - k))
    return a

a= [10, 5, 3, 9, 2]
k = 7
n = len(a)
print(sortAbs(a, n, k))
