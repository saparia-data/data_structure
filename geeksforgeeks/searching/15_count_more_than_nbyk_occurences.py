'''
Given an array arr[] of size N and an element k. The task is to find all elements in array that appear more than n/k times.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer n denoting the size of the array. 
Then the next line contains n space separated integers forming the array. The last line of input contains an integer k.

Output:
Print the count of elements in array that appear more than n/k times.

User Task:
The task is to complete the function countOccurence() which returns count of elements with more than n/k times appearance.

Constraints:
1 <= T <= 102
1 <= N <= 104
1 <= a[i] <= 106
1 <= k <= N

Example:
Input:
2
8
3 1 2 2 1 2 3 3
4
4
2 3 3 2
3
Output:
2
2

Explanation:
Testcase 1: In the given array, 3 and 2 are the only elements that appears more than n/k times.
Testcase 2: In the given array, 3 and 2 are the only elements that appears more than n/k times. 
            So the count of elements are 2.
            
hints:

1)
A simple method is to pick all elements one by one. For every picked element, count its occurrences by traversing the array,
if count becomes more than n/k, then print the element. Time Complexity of this method would be O(n2).

A better solution is to use sorting. First, sort all elements using a O(nLogn) algorithm. 
Once the array is sorted, we can find all required elements in a linear scan of array. 
So overall time complexity of this method is O(nLogn) + O(n) which is O(nLogn).

'''
def countOccurence(arr,n,k):
    
    arr.sort()
    #print(arr)
    
    nbyk = n // k
    #print(nbyk)
    counter = 0
    for i in range(n):
        if(arr[i] in arr):
            counter += 1
            if(counter > nbyk):
                print(arr[i])
                counter = 0
    
arr = [3,1,2,2,1,1,2,3,3]
n = len(arr)
k = 4

countOccurence(arr, n, k)