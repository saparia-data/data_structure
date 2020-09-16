'''
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

https://www.geeksforgeeks.org/nearly-sorted-algorithm/

'''

from heapq import heappop, heappush, heapify

def sort_k(arr, n, k):
    
    heap = arr[:k + 1]
    
    heapify(heap)
    
    target_idx = 0
    
    for rem_element in range(k+1, n):
        arr[target_idx] = heappop(heap)
        heappush(heap, arr[rem_element])
        target_idx += 1
        
    while(heap):
        arr[target_idx] = heappop(heap)
        target_idx += 1

        
k = 3
arr = [2, 6, 3, 12, 56, 8] 
n = len(arr) 
sort_k(arr, n, k)

for ele in arr:
    print(ele, end = " ")
    