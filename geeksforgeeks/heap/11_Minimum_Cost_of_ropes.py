'''
There are given N ropes of different lengths, we need to connect these ropes into one rope. 
The cost to connect two ropes is equal to sum of their lengths. 
The task is to connect the ropes with minimum cost.

Example:

Input:
N = 4
L[] = {4,3,2,6}
Output: 29
Explanation:For example if we are given 4
ropes of lengths 4, 3, 2 and 6. We can
connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3.
Now we have three ropes of lengths 4, 6
and 5.
2) Now connect ropes of lengths 4 and 5.
Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all
ropes have connected.
Total cost for connecting all ropes is 5
+ 9 + 15 = 29. This is the optimized cost
for connecting ropes. Other ways of
connecting ropes would always have same
or more cost. For example, if we connect
4 and 6 first (we get three strings of 3,
2 and 10), then connect 10 and 3 (we get
two strings of 13 and 2). Finally we
connect 13 and 2. Total cost in this way
is 10 + 13 + 15 = 38.

hints:

Following is complete algorithm for finding the minimum cost for connecting n ropes.
Let there be n ropes of lengths stored in an array len[0..n-1]
1) Create a min heap and insert all lengths into the min heap.
2) Do following while number of elements in min heap is not one.
……a) Extract the minimum and second minimum from min heap
……b) Add the above two extracted values and insert the added value to the min-heap.
……c) Maintain a variable for total cost and keep incrementing it by the sum of extracted values.
3) Return the value of this total cost.

'''
import heapq

def minCost(a,n) :
    
    min_heap = [] # curr list containing our heap

    for num in a:
        heapq.heappush(min_heap, num) # insert all elements in heap
        
    total_cost = 0 # cost till now

    while(len(min_heap)>1): # while single rope has not been formed
        # get minimum two lengths from the heap
        val_1 = heapq.heappop(min_heap)
        val_2 = heapq.heappop(min_heap)

        # join these two ropes
        val = val_1+val_2
        # add to total cost
        total_cost+=val
        # now push this new length in heap again
        heapq.heappush(min_heap,val)

    # return the total cost.
    return total_cost
