'''
Given an array arr[] of integers of size N that might contain duplicates, the task is to find all possible unique subsets.

Example 1:
Input: N = 3, arr[] = {1,2,2}
Output:(),(1),(1 2),(1 2 2),(2),(2 2)

Example 2:
Input: N = 4, arr[] = {1,2,3,3}
Output: (),(1),(1 2),(1 2 3)
(1 2 3 3),(1 3),(1 3 3),(2),(2 3)
(2 3 3),(3),(3 3)

https://www.geeksforgeeks.org/find-distinct-subsets-given-set/
https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/

'''
def subsetsUtil(A, subset, index, res): 
    res.add(tuple(subset)) 
    for i in range(index, len(A)):  
          
        # include the A[i] in subset.  
        subset.append(A[i]) 
          
        # move onto the next element.  
        subsetsUtil(A, subset, i + 1, res)  
          
        # exclude the A[i] from subset and  
        # triggers backtracking. 
        subset.pop(-1)  
    return
  
# below function returns the subsets of vector A.  
def subsets(A): 
    res = set()
    subset = []
      
    # keeps track of current element in vector A  
    index = 0
    subsetsUtil(A, subset, index, res)
    #print(res)
    
    for x in res:
        print(list(x))
      
# Driver Code 
  
# find the subsets of below vector.  
array = [1, 2, 3, 3] 
  
# res will store all subsets.  
# O(2 ^ (number of elements inside array))  
# because at every step we have two choices  
# either include or ignore.  
subsets(array)