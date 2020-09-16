'''
Given an array a[] of N positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer n denoting the size of the array. The next line contains N space separated integers forming the array.

Output:
Print "Yes" (without quotes) if there exist a subarray of size at least one with sum equal to 0 or else print "No" ( without quotes).

Your Task:
This is a function problem. You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false.

Constraints:
1 <= T <= 100
1 <= N <= 104
-105 <= a[i] <= 105

Example:
Input:
2
5
4 2 -3 1 6
5
4 2 0 1 6
Output:
Yes
Yes

Explanation:
Testcase 1: 2, -3, 1 is the subarray with sum 0.
Testcase 2: 0 is one of the element in the array so there exist a subarray with sum 0.

hints:

1)
think of doing this with hashing. Concept of prefix sum can be used with a hack to check if current sum ooccurred previously. 
If current sum encountered previously, this means elements between previous sum and current sum makes them 0. 

'''
def subArrayExists(arr,n):
    
    mySet = set()
    
    sum = 0
    
    for i in arr:
        sum += i
        
        if sum == 0 or sum in mySet:
            return True
        mySet.add(sum)
    
    return False

arr = [4,2,-3,1,6]
n = len(arr)
print(subArrayExists(arr, n))