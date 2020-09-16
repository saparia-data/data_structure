'''
Given a sorted array arr[] of size N without duplicates, and given a value x. 
Find the floor of x in given array. Floor of x is defined as the largest element K in arr[] 
such that K is smaller than or equal to x.

Input:
First line of input contains number of testcases T. 
For each testcase, first line of input contains number of elements in the array and element whose floor is to be searched. 
Last line of input contains array elements.

Output:
Output the index of floor of x if exists, else print -1.

User Task:
The task is to complete the function findFloor() which finds the floor of x.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ X ≤ arr[n-1]

Example:
Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
-1
1
3

Explanation:
Testcase 1: No element less than 0 is found. So output is "-1".
Testcase 2: Number less than 5 is 2, whose index is 1(0-based indexing).
Testcase 3: Number less than or equal to 10 is 10 and its index is 3.

hints:

use binary search.
Find the first element in the array which is greater than x.
This can be found using binary search.
The element just before the found element is the floor of x.

'''
def floorSearch(arr, low, high, x):  
  
    # If low and high cross each other  
    if (low > high):  
        return -1
  
    # If last element is smaller than x  
    if (x >= arr[high]):  
        return high  
  
    # Find the middle point  
    mid = int((low + high) / 2)  
  
    # If middle point is floor.  
    if (arr[mid] == x):  
        return mid  
  
    # If x lies between mid-1 and mid  
    if (mid > 0 and arr[mid-1] <= x  
                and x < arr[mid]):  
        return mid - 1
  
    # If x is smaller than mid,  
    # floor must be in left half.  
    if (x < arr[mid]):  
        return floorSearch(arr, low, mid-1, x)  
  
    # If mid-1 is not floor and x is greater than  
    # arr[mid],  
    return floorSearch(arr, mid+1, high, x)  
    
def findFloor(A,N,X):
    return floorSearch(A,0,N-1,X)
    
A = [1, 2, 4, 6, 10, 12, 14]
N = len(A)
x = 10
print(findFloor(A, N, x))