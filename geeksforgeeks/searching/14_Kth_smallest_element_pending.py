'''
Given an array arr[] and a number K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
Expected Time Complexity: O(n)

Input:
The first line of input contains an integer T, denoting the number of testcases. 
Then T test cases follow. Each test case consists of three lines. 
First line of each testcase contains an integer N denoting size of the array. 
Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the kth smallest element in a new line.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N

Example:
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4
Output:
7
15

Explanation:
Testcase 1: 3rd smallest element in the given array is 7.
Testcase 2: 4th smallest elemets in the given array is 15.

hints:

1)
The idea is to use quick select.

2)
Randomly pick a pivot element.

To implement randomized partition, we use a random function, rand() to generate index between l and r, 
swap the element at randomly generated index with the last element, 
and finally call the standard partition process which uses last element as pivot.

'''
print("----------------------------method-1------------------------------------")
def kthSmallest(arr, n, k):
    
    arr.sort()
    
    return arr[k - 1]
print("----------------------------method-2------------------------------------")

arr = [12, 3, 5, 7, 19] 
n = len(arr) 
k = 2
print(kthSmallest(arr, n, k))