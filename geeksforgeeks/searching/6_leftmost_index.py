'''
Given a sorted array arr of N positive integers (elements may be repeated) and a number x. 
The task is to find the leftmost index of x in the array arr.

Input:
First line of input contains number of testcases T. For each testcase, first line contains number of elements N, 
and next line contains N elements. Last line contains x.

Output:
For each testcase, print the leftmost index at which x is present in the array. 
If the element is not present in the array, then output "-1" (without quotes).
Note: Avoid O(N) approach, try to solve in O(log N) time complexity.

User Task:
The task is to complete the function leftIndex() which finds leftmost occurrence of x in given input array. 
Return -1, if element is not present in the array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= arr[i] <= 106
1 <= x <= 106

Example:
Input:
2
10
1 1 2 2 3 4 5 5 6 7
1
7
10 20 20 20 20 20 20
20

Output:
0
1

Explanation:
Testcase 1: 1 is present two times in the array and its leftmost index is 0.
Testcase 2: 20 is present 5 times , but its leftmost index is 1.

hints:
Use binary search to find element x.
If element is found, then go for its lower bound index, the index at which it's occurrence starts.

'''
def leftIndex(N,A,x):
    
    low = 0
    high = N - 1
    mid = low + ((high - low) // 2)
    
    while(low <= high):
        
        mid = low + ((high - low) // 2)
        
        if((A[mid] == x and mid == 0) or (A[mid] == x and A[mid - 1] < x)):
            return mid
        
        if(x > mid):
            low = mid + 1
        
        if(x < mid):
            high = mid - 1
            
    return -1
    
    
    
A = [1,1,2,2,3,4,5,5,6,7]
N = len(A)
x = 2
print(leftIndex(N, A, x))