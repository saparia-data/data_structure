'''
Given an array arr[] of N positive and negative integer pairs, may not be in sorted order. 
The task is to pair the positive and negative element in such a way that a positive element is paired with a negative element of same absolute value. 
If a pair element is not present for an element, then ignore it. The output should contain all pairs in increasing order of absolute values. 
To print a pair, positive value should be printed before its corresponding negative value.
Note: The elements in array are distinct.

Input:
First line of input contains number of testcases T. For each testcase, first line contains an integer N, number of elements in the array. 
Next line contains N space separated array elements.

Output:
For each testcase, print the pairs of positive and negative, sorted with positive numbers. If no such pair exists, print 0.

Constraints:
1 <= T <= 100
1 <= N <= 106
-106 <= arr[i] <= 106

Example:
Input:
2
8
1 3 6 -2 -1 -3 2 7
3
3 2 -3
Output:
1 -1 2 -2 3 -3
3 -3

Explanation:
Testcase 1: 1, 2 and 3 are present pairwirse postive and negative. 6 and 7 have no pair.
Testcase 2: 3 is the only element present pairwise positive and negative.

hints:

1)
The idea is to use hashing. Traverse the given array, increase the count at absolute value of hash table. 
If count becomes 2, store its absolute value in another vector. 
And finally sort the vector. 
If the size of the vector is 0, print "0", else for each term in vector print first its negative value and the the positive value.

'''

def positiveNegativePair(arr, n):
    
    #mymap = dict()
    s = set()
    #arr_s = []
    
    #for i in range(n):
     #   mymap[arr[i]] = 1
        
    #print(mymap)
    
    for i in range(n):
        
        if(arr[i] > 0 and (-1 * arr[i]) in arr):
            s.add(arr[i])
            
    #print(s)
    
    #for num in s:
     #   arr_s.append(num)
        
    #print(arr_s)
    #arr_s.sort()
    #print(arr_s)
    
    if(len(s) == 0):
        return 0
    
    for num in s:
        print(num, -1*num, end="\n")

    
arr = [1,3,6,-2,-1,-3,2,7]
n = len(arr)
positiveNegativePair(arr, n)