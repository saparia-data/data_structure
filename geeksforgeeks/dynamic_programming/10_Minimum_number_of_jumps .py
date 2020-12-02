'''
Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
The task is to find the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.

Example 1:
Input:
N = 11
a[] = {1,3,5,8,9,2,6,7,6,8,9}
Output: 3
Explanation: First jump from 1st element,
and we jump to 2nd element with value 3.
Now, from here we jump to 5h element with
value 9. and from here we will jump to
last.

Example 2:
Input:
N = 6
a[] = {1,4,3,2,6,7}
Output: 2

https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

'''
def minJumps(arr, n):
    
    jumps = [float('inf') for i in range(n)]
 
    #if (n == 0) or (arr[0] == 0):
     #   return float('inf')
 
    jumps[0] = 0
 
    # Find the minimum number of 
    # jumps to reach arr[i] from 
    # arr[0] and assign this 
    # value to jumps[i]
    for i in range(1, n):
        #jumps[i] = float('inf')
        for j in range(i):
            if (j + arr[j] >= i) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                #break
                
    return jumps[n-1]
 
# Driver Program to test above function
arr = [1, 3, 6, 1, 0, 9]
size = len(arr)

arr1 = [1,4,3,2,6,7]
size1 = len(arr1)

print(minJumps(arr, size))
print(minJumps(arr1, size1))