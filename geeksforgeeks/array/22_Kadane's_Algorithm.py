'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

User Task:
The task is to complete the function maxSubarraySum() which finds subarray with maximum sum.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input:
2
5
1 2 3 -2 5
4
-1 -2 -3 -4

Output:
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

Hints:
1)
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far

'''
from turtledemo.penrose import star

def maxSubArraySum(a,size):
    
    max_so_far = a[0]
    min_end_here = 0
    
    start, end = 0, 0
    ind = 0
    
    for i in range(size):
        
        min_end_here = min_end_here + a[i]
        
        if(min_end_here > max_so_far):
            max_so_far = min_end_here
            start = ind
            end = i
            
        if(min_end_here < 0):
            min_end_here = 0
            ind = i + 1
            
    return max_so_far, start, end

a = [1,2,3,-2,5]
size = len(a)

max_sum, start, end = maxSubArraySum(a, size)
l = []
for i in range(start , end + 1):
    l.append(a[i])
    
print(l)