'''
Given an array arr[] of N positive integers, where elements are consecutive (sorted). 
Also, there is a single element which is repeating X (any variable) number of times. 
Now, the task is to find the element which is repeated and number of times it is repeated.

Input:
First line of input contains number of testcases T. 
For each testcase, first line of input contains number of elements in the array N. 
Next line contains the array elements.

Output:
For each testcase, there will be a single line containing the element 
which is repeated and the number of times it is repeated, seperated by space.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= arr[i] <= 1015

Input:
2
5
1 2 3 3 4
5
2 3 4 5 5

Output:
3 2
5 2

Example:
Testcase 1: In the given array, 3 is occuring two times.So the output is 3 2.
Testcase 2: In the given array, 5 is occuring two times.So the output is 5 2.

hints:

1) Number of times the element repeats. 
If the array is sorted and if max-difference of two adjacent elements is 1, 
then the length of the repeated sequence is n-(arr[n-1]-arr[0])

2) Value of the element. To the value, we do Binary Search.

'''
def findRepeating(arr, n):
    
    if(n == 0):
        return [0, 0]
    
    low = 0
    high = n - 1
    
    while(low < high):
        
        mid = (low + high) // 2
        
        if(arr[mid] >= mid + arr[0]):
            low = mid + 1
            
        else:
            high = mid
            
    return [arr[mid], n-(arr[n-1]-arr[0])]

arr = [1, 2, 3, 4, 4, 4, 5, 6]
n = len(arr)

print(findRepeating(arr, n))