'''
Given an array arr[] of N positive integers and a number K. The task is to find the kth smallest element in the array.

Example 1:
Input: N = 5, K = 3
arr[] = [3 5 4 2 9]
Output: 4
Explanation: 
Third smallest element in the array is 4.

Example 2:
Input: N = 5, K = 5
arr[] = [4 3 7 6 5]
Output: 7
Explanation: 
Fifth smallest element in the array is 7.

'''
import heapq

def kthSmallest(a, n, k):
    
    max_heap = []
    
    for num in a:
        if len(max_heap)<k: # if the current size is less than k, add element in it
            heapq.heappush(max_heap,-1*num) # storing negative for max heap purpose
            #print(max_heap)
        else:
            curr_min = -1*heapq.heappop(max_heap) # curr maximum element in heap
            #print(curr_min)
            # push min out of current element and heap min in heap again
            heapq.heappush(max_heap,-1*min(curr_min,num))
            #print(max_heap)

    # now the negative of top element is our kth smallest
    return (-1*heapq.heappop(max_heap))

a = [3,5,4,2,9]
n = len(a)
k = 3
print(kthSmallest(a, n, k))