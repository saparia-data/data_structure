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

Example 2:
Input:
N = 7, k = 3
arr[] = {1,23,12,9,30,2,50}
Output: 50 30 23
Explanation: Three Largest element in
the array are 50, 30 and 23.

hints:

1. Build a min heap, and start inserting the elements into it.
2. If heap size becomes equal to K, then compare the incoming element with the element at the top of the heap.
3. If element at the top is less than the incoming element, then pop the top from heap and insert the new element into the heap.
4. Finally, you are having K largest elements in the heap. Now, since you need to print the elements in decreasing order, 
   so you can now pop the elements from heap one by one and store it in a vector.

'''

from heapq import heappush, heappop, heapify

def kLargest(arr, n, k):
    
    heap = arr[:k]
    heapify(heap)
    print(heap[0])
    
    for i in range(k+1, n):
        p = heap[0]
        if(arr[i] > p):
            heappop(heap)
            heappush(heap, arr[i])
            
    return heap
        
    
    
arr = [1,23,12,9,30,2,50]
n = len(arr)
k = 3
print(kLargest(arr, n, k))