'''
Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example 1:
Input:
N = 16
A[]={0,8,4,12,2,10,6,14,1,9,5
     13,3,11,7,15}
Output: 6
Explanation:Longest increasing subsequence
0 2 6 9 13 15, which has length 6

https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

'''

def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and  
    # initialize LIS values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if(arr[i] > arr[j]): 
                lis[i] = max(lis[i], lis[j]+1)
  
    # Initialize maximum to 0 to get  
    # the maximum of all LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
        
    return maximum
  

arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print(lis(arr))