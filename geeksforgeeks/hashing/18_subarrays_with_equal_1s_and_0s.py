'''
Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of two lines. 
First line of each test case contains an Integer N denoting size of array and the second line contains N space separated 0 and 1.

Output:
For each test case, in a new line, print the count of required sub arrays in new line

Your Task:
You don't need to read input or print anything. Your task is to complete the function countSubarrWithEqualZeroAndOne() 
which takes the array arr[] and the size of the array as inputs and returns the number of subarrays with equal number of 0s and 1s.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= N <= 106
0 <= A[i] <= 1

Example:
Input:
2
7
1 0 0 1 0 1 1
5
1 1 1 1 0
Output:
8
1

Explanation:
Testcase 1: The index range for the 8 sub-arrays are:
(0, 1), (2, 3), (0, 3), (3, 4), (4, 5)
(2, 5), (0, 5), (1, 6)
Testcase 2: The index range for the subarray is (3,4).

https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/

'''
def countSubarrWithEqualZeroAndOne(arr, n): 
    
    mp = {}
    summ = 0
    count = 0
    
    for i in range(n):
        if(arr[i] == 0):
            arr[i] = -1
            
        summ += arr[i]
        
        if(summ == 0):
            count += 1
            
        if(summ in mp):
            count += mp[summ]
            
        mp[summ] = mp.get(summ, 0) + 1
        
    return count
    
arr = [1,0,0,1,0,1,1]
n = len(arr)
print(countSubarrWithEqualZeroAndOne(arr, n))