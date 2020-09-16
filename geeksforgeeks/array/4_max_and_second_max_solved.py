'''
Given an array arr[] of size N of positive integers which may have duplicates. The task is to find maximum and second maximum from the array, which must be distinct. If no second max exists, then second max will be -1.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains size of array N, next line contains array elements.

Output Format:
For each testcase, print the maximum and second maximum from the array. IF no second max exists, print "-1" for second max.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= arr[i] <= 106

User Task:
The task is to complete the function largestAndSecondLargest(), which should print maximum and second maximum element from the array.

Example:
Input:
2
5
1 2 3 4 5
3
2 1 2

Output:
5 4
2 1

Explanation:
Testcase 1: From the given array elements, 5 is the largest and 4 is the second largest.
Testcase 2: From the given array elements, 2 is the largest and 1 is the second largest.
'''

def largestAndSecondLargest(sizeOfArray, arr):
    max1 = -1
    max2 = -1
    
    arr = sorted(arr)
    
    max1 = arr[sizeOfArray - 1]
    
    for i in range(sizeOfArray-2,-1,-1):
        if(arr[i] != arr[i+1] and arr[i] < arr[i+1]):
            max2 = arr[i]
            break;
    
    print (max1, max2)
    
    print("--------------------------------------------------")
    
    max1 = -1
    max2 = -1
    
    for i in range(sizeOfArray-1):
        max1 = arr[i]
        if(arr[i] < arr[i+1]):
            max1 = arr[i+1]
    
    for i in range(sizeOfArray-1):
        #max2 = arr[i]
        if(arr[i] < arr[i+1] and arr[i+1] < max1):
            max2 = arr[i+1]
            
    print(max1, max2)
    
    print("--------------------------------------------------")
    
    max1 = -1
    max2 = -1
    
    for i in range(n):
        if(arr[i] > max1):
            max2 = max1
            max1 = arr[i]
        elif(arr[i] > max2 and arr[i] != max1):
            max2 = arr[i]
            
    print(max1, max2)
            
    
    
arr = [1,5,8,2,3]
n = len(arr)
largestAndSecondLargest(n, arr)