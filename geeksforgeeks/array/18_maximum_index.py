'''
Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].

Input:
The first line contains an integer T, depicting total number of test cases.  Then T test case follows. First line of each test case contains an integer N denoting the size of the array. Next line contains N space separated integeres denoting the elements of the array.

Output:
For each test case, print the maximum difference of the indexes i and j in a separtate line.

User Task:
The task is to complete the function maxIndexDiff() which finds and returns maximum index difference. Printing the output will be handled by driver code.

Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 1018

Example:
Input:
2
2
1 10
9
34 8 10 3 2 80 30 33 1

Output:
1
6

Explanation:
Testcase 1: A[0]<=A[1] so (j-i) is 1-0 = 1.
Testcase 2:  In the given array A[1] < A[7] satisfying the required condition(A[i] <= A[j]) thus giving the maximum difference of j - i which is 6(7-1).

hints:
1)
As we need the max difference j - i such that A[i]<= A[j], hence we do not need to consider element after the index j and element before index i.

But why..???

Lets say, we get max difference for a particular i and j. Then these conditions hold true.

A[i] <= A[j]
Any element before A[i] is larger then A[j], else it would make the max difference. Hence we do not consider any element before A[i].
Any element after A[j] is smaller then A[i], else it would make the max difference. Hence we do not consider any element after A[j].

2)
For the observation, in previous hint, make 2 arrays, 
First, will store smallest occuring element before the element
Second, will store largest occuring element after the element

Traverse the Second array, till the element in second array is larger than or equal to First array, and store the index difference. 
And if it becomes smaller, traverse the first array till it again becomes larger.

And store the max difference of this index difference.
'''
print("----------------------------------------O(n2)-------------------------------------------------------------------------------")
def maxIndexDiff(arr, n):
    
    maxDiff = -1
    
    for i in range(n):
        
        j = n - 1
        while(j > i):
            if(arr[j] > arr[i] and maxDiff < (j - i)):
                maxDiff = j - i
            j -= 1
    return maxDiff

arr = [34,8,10,3,2,80,30,33,1]
n = len(arr)
print(maxIndexDiff(arr, n))


arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0] 
n = len(arr) 
maxDiff = maxIndexDiff(arr, n) 
print(maxDiff) 
print("----------------------------------------------------------------------------------------------------------------------------")

def maxIndexDiff2(arr, n): 
    
    LMin = [0] * n
    RMax = [0] * n
    maxDiff = 0
    
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])
    print(LMin)
        
    print("n = "+ str(n))    
    RMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        RMax[i] = max(arr[i], RMax[i + 1])
    print(RMax)
    
    i, j = 0, 0
    while(j < n and i < n):
        print(i,j,LMin[i],RMax[j])
        if(RMax[j] > LMin[i]):
            maxDiff = max(maxDiff, j - i)
            j += 1
        else:
            i += 1
    return maxDiff
    
arr = [34,8,10,3,2,80,30,33,1] 
n = len(arr) 
print(maxIndexDiff2(arr, n)) 





