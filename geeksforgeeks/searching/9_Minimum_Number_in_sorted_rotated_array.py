'''
Given an array A  which is sorted and contains N distinct elements. Also, this array is rotated at some unknown point. 
The task is to find the minimum element in it. 
Note: Expected time complexity is O(logN).

Input:
The first line of input contains an integer T denoting the number of test cases. 
Each test case contains the number of elements in the array arr[] as N 
and next line contains space separated n elements in the array arr[].

Output:
Print an integer which denotes the minimum element in the array.

User Task:
The task is to complete the function minNumber() which finds the minimum in sorted and rotated array.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= arr[i] <= 107

Example:
Input:
3
10
2 3 4 5 6 7 8 9 10 1
5
3 4 5 1 2
8
10 20 30 45 50 60 4 6
Output:
1
1
4

Explanation:
Testcase 1: The array is rotated once anti-clockwise. So minium element is at last index (n-1) which is 1.
Testcase 2: The array is rotated and the minimum element present is at index (n-2) which is 1.
Testcase 3: The array is rotated and the minimum element present is 4.

hints:

The minimum element is the only element whose previous is greater than it. 
If there is no previous element element, then there is no rotation (first element is minimum). 
We check this condition for middle element by comparing it with (mid-1)'th and (mid+1)'th elements.

If minimum element is not at middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.

If middle element is smaller than last element, then the minimum element lies in left half

Else minimum element lies in right half.

'''
def findMin(arr, low, high):
    
    mid = (low + high) // 2
    
    if(low > high):
        return arr[0]
    
    if(high == low):
        return arr[low]
    
    if(mid < high and arr[mid + 1] < arr[mid]):
        return arr[mid + 1]
    
    if(mid > low and arr[mid - 1] > arr[mid]):
        return arr[mid]
    
    if(arr[high] > arr[mid]):
        return findMin(arr, low, mid-1)
    
    return findMin(arr, mid+1, high) 


arr = [5, 6, 1, 2, 3, 4]
low = 0
high = len(arr) - 1
print(findMin(arr, low, high)) 