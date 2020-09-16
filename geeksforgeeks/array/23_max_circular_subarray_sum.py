'''
Given an array arr[] of N integers arranged in a circular fashion. Your task is to find the maximum contigious subarray sum.

Input:
First line of input contains a single integer T which denotes the number of test cases. First line of each test case contains a single integer N which denotes the total number of elements. Second line of each test case contains N space separated integers denoting the elements of the array.

Output:
For each test case print the maximum sum obtained by adding the consecutive elements.

User Task:
The task is to complete the function circularSubarraySum() which finds the circular subarray with maximum sum.

Constraints:
1 <= T <= 101
1 <= N <= 106
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
22
23
52

Explanation:
Testcase 1: Starting from last element of the array, i.e, 12, and moving in circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, 
which gives maximum sum as 22.

Hints:
1)
Case 1 (We get maximum sum using normal subarray) : The elements that contribute to the maximum sum are arranged such that no wrapping is there. 
Examples: {-10, 2, -1, 5}, {-2, 4, -1, 4, -1}. In this case, Kadane's algorithm will produce the result.

Case 2 (We get maximum sum using both corner elements): The elements which contribute to the maximum sum are arranged such that wrapping is there. 
Examples: {10, -12, 11}, {12, -5, 4, -8, 11}. In this case, we need to remove some (0 or more) middle elements with minimum sum. 
So the idea is to use Kadane's algorithm again to find the minimum sum subarray.  
Instead of writing a separate function for minimum sum subarray, we can change signs of elements and call same maximum sum function again.
'''

def kadane(a): 
    n = len(a) 
    max_so_far = a[0]
    max_ending_here = 0
    for i in range(0, n): 
        max_ending_here = max_ending_here + a[i] 
        if (max_ending_here < 0): 
            max_ending_here = 0
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
    return max_so_far


def circularSubarraySum(arr,n):
    
    max_kadane = kadane(arr)
    
    max_wrap = 0
    for i in range(n):
        max_wrap += arr[i]
        arr[i] = -arr[i]
        
    max_wrap = max_wrap + kadane(arr)
    
    if(max_wrap > max_kadane):
        return max_wrap
    else:
        return max_kadane


def circularSubarraySum2(arr,n):
    
    #total  sum
    sum = 0
    for i in range(n):
        sum += arr[i]
        
    min_sum = 0    
    maxi = sum
    for i in range(n):
        min_sum = min(min_sum + arr[i], arr[i])
        if(min_sum == sum):
            return -99999999
        
        maxi = max(maxi, sum - min_sum)
        
    return maxi





    
a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
n = len(a)
print(circularSubarraySum(a, n))

K = kadane(a)
C = circularSubarraySum2(a, n)
print(max(K,C))