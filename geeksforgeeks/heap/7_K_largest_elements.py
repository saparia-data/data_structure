'''
Given an array of N positive integers, print k largest elements from the array. 

Example 1:

Input:
N = 5, k = 2
arr[] = {12,5,787,1,23}
Output: 787 23
Explanation: First largest element in
the array is 787 and the second largest
is 23.

'''
import heapq

def KLargest(arr, n, k):
    
    heap = []
    
    for value in arr:
        heapq.heappush(heap, value)
        if(len(heap) > 2):
            heapq.heappop(heap)
        
    ans = []        
    while(len(heap) > 0):
        ans.append(heapq.heappop(heap))
        
    return ans

arr = [12,5,787,1,23]
n = len(arr)
k = 2
print(KLargest(arr, n, k))