'''
Given an integer array Arr[] and an element x. The task is to find if the given element is present in array or not.

Input:
First line contains an integer, the number of test cases 'T'. For each test case, first line contains an integer 'N', size of array. 
The second line contains the elements of the array separated by spaces. Third line contains element to be find in the array.

Output:
For each testcase, output a single line containing first index of element to be found in array. If element is not in the array, then print "-1" (without quotes).

User Task:
The task is to complete the function search() which searched for the given element in the array.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Arr[i] <= 100

Example:
Input:
1
4
1 2 3 4
3

Output:
2

Explanation:
Testcase 1: There is one test case with array as {1, 2, 3 4} and element to be searched as 3.  Since 3 is present at index 2, output is 2.

Hints:

1) Use linear search.
2) 
-Start traversing through the array using loop (eg. for loop).
-Now, if element to be found is striked at any index in the array, then print the index 
 and break out of the loop as this will be the first time you got the element in the array.
-If you have traversed whole array and unable to found key in the array, then print -1.

'''

def search(A,N,x):
    
    if (x in A):
        print(A.index(x, ))
    else:
        print(-1)
    
    print("------------------------------------------------------")
    '''
    try:
        return A.index(x, )
    except:
        return -1
    '''    

A = [86,77,15,93,35,86,92,49,21,62,27,90,59,63,26,40,26,72,36,11,68,67,29,82,30,62,23,67,35,29,2,22,58,69,67,93,56,11,42,29,73,21,19,84,37,98,24,15,70,13,26,91,80,56,73,62,70,96,81,5,25,84,27,36,5,46,29,13,57,24,95,82,45,14,67,34,64,43,50,87,8,76,78,88]
N = len(A)
x = 1
print(search(A, N, x))