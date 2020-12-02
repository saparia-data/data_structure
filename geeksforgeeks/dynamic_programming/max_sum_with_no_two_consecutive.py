'''
Given an array of positive numbers, find the maximum sum of a subsequence 
with the constraint that no 2 numbers in the sequence should be adjacent in the array. 
So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).


'''

# space complexity is O(n)
def maxSum(arr, n):
    
    if(n == 0):
        return arr[0];
    
    dp = [0] * (n + 1)
    
    dp[1] = arr[0]
    dp[2] = max(arr[0], arr[1])
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i-1])
        
    return dp[n]

arr1 = [10, 20, 30, 40, 50]
n1 = len(arr1) 
print(maxSum(arr1, n1))


# space complexity is O(1)
def maxSum1(arr, n):
    
    if(n == 0):
        return arr[0]
    
    prev_prev = arr[0]
    prev = max(arr[0], arr[1])
    
    for i in range(3, n+1):
        res = max(prev, prev_prev + arr[i-1])
        prev_prev = prev
        prev = res
        
        
    return res

arr2 = [10, 20, 30, 40, 50]
n2 = len(arr2) 
print(maxSum1(arr2, n2))