'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of two lines. 
The first line of each test case is N and S, where N is the size of array and S is the sum. 

The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left 
if sum equals to subarray, else print -1.

User Task:
The task is to complete the function subarraySum() which finds starting and ending positions(1 indexing) of first such occuring subarray 
from the left if sum equals to subarray, else -1 is printed. The driver code automatically appends a new line.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= Ai <= 1010

Example:
Input:
3
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
4 15
5 7 1 2
Output:
2 4
1 5
1 4

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12.
Testcase2: sum of elements from 1st position to 5th position is 15.
Testcase 3: Sum of elements from 1st to 4th position is 15.

hints:

1)
We need to use Sliding window Method to solve this Problem.

Add the elements, to currsum till it is less than S. If it becomes more than S, start deleting elements from start in the cuusum. 
if the currsum again becomes less than S, again start adding elements to it. In between also check, if the currsum becomes equal to S.
If yes, then output start and end index, else after traversing array no such solution is found, output -1.

2)
The complete solution is

Maintain start and last index to store and print these values 
Iterate the complete array.
Add array elements to cuursum
If currsum becomes greater than S, then remove elements starting from start index, till it become less than or equal to S, and increement start.
if currsum becomes equals to S, then print the starting and last index
if the currsum never maches to S, then print -1

'''
def subArraySum(arr, n, sum):
    
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    curr_sum = arr[0] 
    start = 0
    
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element
    i = 1
    while i <= n: 
        
        
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements
        while(curr_sum > sum and start < i - 1):
            curr_sum -= arr[start]
            start += 1
        
        # If curr_sum becomes 
        # equal to sum, then 
        # return true
        if(curr_sum == sum):
            print(start+1,i)
            return 1
        
        # Add this element  
        # to curr_sum
        if(i < n):
            curr_sum += arr[i]
        i += 1
    
    
arr = [1,2,3,7,5]
n = len(arr)
summ = 12
subArraySum(arr, n, summ)