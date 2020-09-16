'''
Given an unsorted array arr[] of N integers and a sum. The task is to count the number of subarray which adds to a given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer N denoting the size of the array. The next line contains N space separated integers forming the array. 
The last line contains an integer denoting the value of the sum.

Output:
For each testcase, in a new line, print the count of the subarray which adds to the given sum.

Your Task:
This is a function problem. You only need to complete the function subArraySum() that takes arr, n, sum as parameters and returns the count.

Constraints:
1 <= T <= 200
1 <= N <= 105
-105 <= arr[i] <= 105
-105 <= sum <= 105

Example:
Input:
2
5
10 2 -2 -20 10
-10
6
1 4 20 3 10 5
33
Output:
3
1

Explanation:
Testcase 1: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].
Testcase 2: Subarray with sum 33 is: [20,3,10].

hint:
A way is to use a map/hash table. The idea is to maintain sum of elements encountered so far in a variable (say curr_sum). 
Let the given number is sum. Now for each element, we check if (curr_sum minus sum) exists in the map or not. If we found it in the map/hash table that means, 
we have a subarray present with given sum, else we insert curr_sum into the map/hash table and proceed to next element.
If all elements of the array are processed and we didn't find any subarray with given sum, then subarray doesn't exists.


'''

from collections import OrderedDict

def subArraySum(arr, n, sum):
    
    mp = OrderedDict({})
    curr_sum, count = 0, 0
    
    for i in range(n):
        curr_sum+=arr[i]
        print(curr_sum)
        if curr_sum==sum:
            count+=1
        print(curr_sum, sum, curr_sum-sum)
        x=mp.get(curr_sum-sum,False)
        print(x)
        
        if x is not False:
            count+=x
        mp[curr_sum]=mp.get(curr_sum,0)+1
        print(mp)
    return count
        
    
    
    
arr = [10,2,-2,-20,10]
n = len(arr)
sum = -10
print(subArraySum(arr, n, sum))