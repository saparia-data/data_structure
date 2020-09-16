'''
Given an array of integers, find the closest (not considering distance, but value) greater or same value on left of every element. 
If an element has no greater or same value on the left side, print -1.

Input : arr[] = {10, 5, 11, 6, 20, 12}
Output : -1, 10, -1, 10, -1, 20

https://www.geeksforgeeks.org/closest-greater-or-same-value-on-left-side-for-every-element-in-array/

'''

# O(n2) solution. We can use self balancing BST for O(nlogn) solution. In java we can use TreeSet
def printPrevGreater(arr, n):
    
    s = set()
    
    for i in range(n):
        
        it = [x for x in s if x >= arr[i]]
        
        if(len(it)) == 0:
            print(-1, end = " ")
        else:
            print(min(it), end = " ")
            
        s.add(arr[i])
        
arr = [10, 5, 11, 10, 20, 12]  
n = len(arr)  
printPrevGreater(arr, n) 