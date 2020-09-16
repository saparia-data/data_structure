'''
Given an array consisting of cost of toys. Given an integer K depicting the amount of money available to purchase toys. 
Write a program to find the maximum number of toys one can buy with the amount K.

Note: One can buy only 1 quantity of a particular toy.

Examples :

Input:  N = 10, K =  50
        cost = { 1, 12, 5, 111, 200, 1000, 10, 9, 12, 15 }
Output: 6
Explanation: Toys with amount 1, 5, 9, 10, 12, and 12 
can be purchased resulting in a total amount of 49. Hence,
maximum number of toys is 6.

Input: N = 7, K = 50
       cost = { 1, 12, 5, 111, 200, 1000, 10 }
Output: 4


'''
#by sorting element
def maximum_toys(arr, N, K):
    
    summ = 0
    count = 0
    
    arr.sort()
    #print(arr)
    
    for i in range(N):
        if(summ + arr[i] <= K):
            summ += arr[i]
            count += 1
            
    return count

#by using heap data structure
from heapq import heapify, heappop
def maximum_toys_heap(arr, n, k):
    
    heapify(arr)
    #print(arr)
    SUMM = 0
    COUNT = 0
    for i in range(n):
        p = heappop(arr)
        if(SUMM + p <= k):
            SUMM +=  p
            COUNT += 1
            
    return COUNT
    
    

K = 50
arr = [1, 12, 5, 111, 200,1000, 10, 9, 12, 15] 
N = len(arr) 

print(maximum_toys(arr, N, K))
print(maximum_toys_heap(arr, N, K))