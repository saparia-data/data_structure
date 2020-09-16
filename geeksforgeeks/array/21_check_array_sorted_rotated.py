'''
Given an array arr[] of N distinct integers, check if this array is Sorted (non-increasing or non-decreasing) and Rotated counter-clockwise. 
Note that input array may be sorted in either increasing or decreasing order, then rotated.
A sorted array is not considered as sorted and rotated, i.e., there should be at least one rotation.

Input:
The first line of input contains number of testcases T. Each testcase contains 2 lines, the first line contains N, the number of elements in array, 
and second line contains N space separated elements of array.

Output:
Print "Yes" if the given array is sorted and rotated, else Print "No", without Inverted commas.

User Task:
The task is to complete the function checkRotatedAndSorted() which checks if an array is sorted and rotated clockwise.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106

Example:
Input:5
4
3 4 1 2
3
1 2 3
4
10 20 30 14
5
30 20 10 50 35
5
30 20 10 50 25

Output:
Yes
No
No
Yes
No

Explanation:
Testcase 1: The array is sorted (1, 2, 3, 4) and rotated twice (3, 4, 1, 2).
Testcase 2: The array is sorted (1, 2, 3) is not rotated.
Testcase 3: The array is sorted (10, 20, 30, 14) is not sorted and rotated as 14 is greater than 10.
 
Hints:
1)
So How to Find, if array is Decreasingly or Increasingly Sorted in a Sorted and Rotated Array.

Simple,

If the positon of Max. Element is just before Min. Element, then it is Increasingly Sorted
Else if position of Max. Element is just after Min. Element then it is Decreasingly Sorted,
Else it is not sorted and rotated.

2)
In case of Increasingly Sorted,

Check if array is increasing upto Max. Element
Check if array is increasing again after Min Element
Check if Last Element is smaller than the first element
In case of Decreasingly Sorted,

Check if array is decreasing upto Min. Element
Check if array is decreasing again after Max Element
Check if Last Element is larger than the first element
If all these conditions meet, the array is sorted and rotated
'''
import sys
def checkRotatedAndSorted(arr,n):
    
    minIndex, maxIndex = 0, 0
    
    for i in range(n):
        if(arr[i] < arr[minIndex]):
            minIndex = i
        elif(arr[i] > arr[maxIndex]):
            maxIndex = i
            
    print("min",minIndex)
    print("max",maxIndex)
            
    if(abs(minIndex - maxIndex) != 1):
        return False
    
    sorted = True
    
    if(maxIndex < minIndex):
        #for increasing order
        for i in range(n - 1):
            if(arr[(minIndex+i)%n] > arr[(minIndex+i+1)%n]):
                sorted = False
                break
    else:
        #for decreasing order
        for i in range(maxIndex + 1):
            if(arr[(minIndex +n-i) % n] > arr[(minIndex + n - i - 1) % n]):
                sorted = False
                break
    return sorted
        
    
    

arr = [3,2,1,5,4]
n = len(arr)
print(checkRotatedAndSorted(arr, n))

