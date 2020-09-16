'''
Given an input stream of n integers, find the kth largest element for each element in the stream.

Example 1:

Input:
k = 4, n = 6
arr[] = {1,2,3,4,5,6}
Output: -1 -1 -1 1 2 3
Explanation: k = 4
For 1, the 4th largest element doesn't
exist so we print -1.
For 2, the 4th largest element doesn't
exist so we print -1.
For 3, the 4th largest element doesn't
exist so we print -1.
For 4, the 4th largest element is 1
{1, 2, 3, 4}
For 5, the 4th largest element is 2
{2, 3, 4 ,5}
For 6, the 4th largest element is 3
{3, 4, 5, 6}


'''
import heapq

def kthLargest(a, n, k):
    
    k_largest_curr = [] # curr list containing k largest element from processed till now

    for num in a:
        if len(k_largest_curr)<k: # if the current size is less than k, add element in it
            heapq.heappush(k_largest_curr,num)
        else:
            # curr minimum element in heap
            curr_min = heapq.heappop(k_largest_curr) if len(k_largest_curr) else 0
            if num > curr_min : # if top element is smaller than
                # push the num in heap
                heapq.heappush(k_largest_curr,num)
            else:
                heapq.heappush(k_largest_curr, curr_min)
        if len(k_largest_curr)<k: # less than k elements in heap
            print(-1,end=" ")
        else:
            # print root of heap, dont change the heap
            curr_min = heapq.heappop(k_largest_curr)
            print(curr_min,end=" ")
            heapq.heappush(k_largest_curr, curr_min)