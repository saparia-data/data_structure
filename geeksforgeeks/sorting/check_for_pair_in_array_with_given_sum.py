'''
Write a program that, given an array A[] of n numbers and another number x, 
determines whether or not there exist two elements in S whose sum is exactly x.

Input: arr[] = {0, -1, 2, -3, 1}
       sum = -2
Output: -3, 1

'''

def hasArrayTwoCandidates(A, arr_size, Sum): 
    
    A.sort()
    print(A)
    l = 0
    r = arr_size-1
    while(l < r):
        if (A[l] + A[r] == Sum): 
            return A[l],A[r]
        elif (A[l] + A[r] < Sum): 
            l += 1
        else: 
            r -= 1
    return 0
    
    
A = [0, -1, 2, -3, 1]
arr_size = len(A)
Sum = -2
print(hasArrayTwoCandidates(A, arr_size, Sum))