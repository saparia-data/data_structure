'''
Given an array A[] and a range [a, b]. The task is to partition the array around the range such that array is divided in three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified arranged array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
First line of each test case contains an integer N denoting the size of the array. 
Then in the next line are N space separated values of the array (A[]).Then the next line contains two space separated integers 
which denote the range(a,b).

Output:
For each test case the output will be 1 if the array is properly arranged else it would be 0.

User Task:
The task is to complete the function threeWayPartition() which should segregate the elements as required. The function returns an array.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
5
1 2 3 3 4
1 2
3
1 2 3
1 3
Output:
1
1

Explanation:
Testcase 1: First, array has elements less than or equal to 1. Then , elements between 1 and 2. And, finally elements greater than 2. So, output is 1.
Testcase 2: First, array has elements less than or equal to 1. Then, elements between 1 and 3. And, finally elements greater than 3. So, output is 1.

hints:

1)
These are the folowing steps:

Maintain 3 variables low, high and mid
-low - all elements before low are less than low_value
-mid - all elements between low and mid are between low_value and high_value
-high - all elements after high are more than high_value

Initially low, mid are set at 0 and high is at n-1

Now, we iterate mid from 0 to high, and for every element
-if it is lower than low_value, we swap it with element at low, and increment low and mid
-else if it is higher than high_value, we swap it with element at high, and decrement high
-else we just increment mid

This method ensures partition, as low and high maintain elements according to their values, 
and then change their positions, ensuring all elements before low are lower than low_value and all elements after high are higher than high_value

'''
def threeWayPartition(arr, n, a, b):
    i, start = 0, 0
    end = n - 1
    print(arr)
    
    while(i <= end):
        
        # If current element is smaller than 
        # range, put it on next available smaller 
        # position. 
        if(arr[i] < a):
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
            #print(arr)
        
        # If current element is greater than 
        # range, put it on next available greater 
        # position.    
        elif(arr[i] > b):
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
            #print(arr)
            
        else:
            i += 1
            #print(arr)
            
    return arr

arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
n = len(arr)
a = 10
b = 20
print(threeWayPartition(arr, n, a, b))
