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

https://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/

variations of longest increasing subsequence:
1) minimum deletions to make an array sorted
2) maximum sum increasing sub-sequence
3) maximum length of bitonic sub-sequence
4) Building bridges such that max bridges to form with crossing
5) Longest chain of pairs

'''
def binarySearch(lst, l, h, value):
    # this function finds the position of the first integer
    # in arr which is greater than or equal to 'value'
    
    if value > lst[h]:
        return h+1
    # if new value is greater than all array values,
    # then it is places at the end
    
    while h>l:
        middle = (h+l)//2
        
        if lst[middle] == value:
            return middle
        
        if lst[middle] > value:
            h = middle
        
        else:
            l = middle + 1
    
    return h

def longestSubsequence(a,n):
    tail = [0 for _ in range(n)]
    tail[0] = a[0]
    # tail[i] holds the last value in a sub sequence of length = i+1
    
    lastIndex = 0 # the position of last filled index in tail[]
    
    for i in range(1,n):
        index = binarySearch( tail, 0, lastIndex, a[i] )
        # getting the furthest possible index for a[i]
        
        tail[index] = a[i]
        lastIndex = max(lastIndex, index)
    
    return lastIndex+1


arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print(longestSubsequence(arr, n))