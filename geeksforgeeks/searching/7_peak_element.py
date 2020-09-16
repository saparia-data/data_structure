'''
Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
Note: There may be multiple peak element possible, in that case you may return any valid index.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N. Then in the next line are N space separated values of the array.

Output:
For each test case output will be 1 if the index returned by the function is an index with peak element.

User Task:
You don't have to take any input. Just complete the provided function peakElement() and return the valid index.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[] <= 106

Example:
Input:
2
3
1 2 3
2
3 4
Output:
1
1

Explanation:
Testcase 1: In the given array, 3 is the peak element as it is greater than its neighbour.
Testcase 2: 4 is the peak element as it is greater than its neighbour elements.

hints:

The complete solution:

The peak element, is the element that is not smaller than its neighbours.
Checking at an element, if it is smaller than its right neighbour, then a peak element exists at its right. (Why ?)
If it is smaller than its left neighbour, then a peak element exists at its left side. (Why ?)
Do Binary search, with above conditions. Also check at the mid element, if it is not smaller than its neighbours.
Also, consider for corner cases, i.e for index position 0 and n-1, and modify the code accordingly.

'''
def peakElement(arr, low, high, n):

    mid = low + ((high - low) // 2)
    
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
       (mid == n - 1 or arr[mid + 1] <= arr[mid])): 
        return arr[mid] 
    
    elif (mid > 0 and arr[mid - 1] > arr[mid]): 
        return peakElement(arr, low, (mid - 1), n) 
    
    else: 
        return peakElement(arr, (mid + 1), high, n) 
    
    
arr = [1, -1, 0, 1, 1, 100] 
n = len(arr)
low = 0
high = n - 1 
print(peakElement(arr, low, high, n))