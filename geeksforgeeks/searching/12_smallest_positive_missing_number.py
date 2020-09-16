'''
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
Note: Expected solution in O(n) time using constant extra space (don't use hash maps or sorting algorithms in your solution).

Input:
First line consists of T test cases. First line of every test case consists of N, denoting the number of elements in array. 
Second line of every test case consists of elements in array.

Output:
Single line output, print the smallest positive number missing.

User Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Constraints:
1 <= T <= 100
1 <= N <= 106
-106 <= arr[i] <= 106

Example:
Input:
2
5
1 2 3 4 5
5
0 -10 1 3 -20
Output:
6
2

Explanation:
Testcase 1: Smallest positive missing number is 6.
Testcase 2: Smallest positive missing number is 2.

1)
In Smallest Positive Number, we need to find Only Positive number, so no need to consider Negative numbers.

2)
After Eliminating Negative Numbers, Try using Index referencing for this Question,
as we need to find the Smallest Positive Missing Number.

3)
1. Segregrate Positve and Negative Numbers in the array.

2. Traverse all the Positive Numbers, 
     i) if, the number is larger then the input array size, do nothing
     ii) else, the number is within input array size limit, consider number as array index, and mark the element at that index Negative.

3. After doing the above operation, Traverse the array with initial Positve values again, and store the first occurunce of index, whose value is Non-Negative. (Because this means that index value was not present in the array)

4. This stored element is the Result 

'''
def missingNumber(arr,n):
    
    m = max(arr)
    if(m < 0):
        return 1
    
    if(n == 1):
        return 2 if arr[0] == 1 else 1
    
    L = [0] * n
    
    for i in range(n):
        if(arr[i] > 0):
            if(L[arr[i] - 1] != 1):
                L[arr[i] - 1] = 1
                
    print(L)
    
    for i in range(n):
        #Encountering first 0
        if(L[i] == 0):
            return (i+1)
    #In case all values are filled between 1 and m
    return (i+2)
    
    
    
    
arr = [0,-10,1,3,-20]
n = len(arr)
print(missingNumber(arr, n))