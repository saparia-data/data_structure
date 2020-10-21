'''
Given an array of integers and a sum B, find all unique combinations in the array where the sum is equal to B. 
The same number may be chosen from the array any number of times to make B.

Note:
    1. All numbers will be positive integers.
    2. Elements in a combination (a1, a2, …, ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    3. The combinations themselves must be sorted in ascending order.

Example 1:
Input:
N = 4
arr[] = {7,2,6,5}
B = 16
Output:
(2 2 2 2 2 2 2 2)
(2 2 2 2 2 6)
(2 2 2 5 5)
(2 2 5 7)
(2 2 6 6)
(2 7 7)
(5 5 6)

Example 2:
Input:
N = 11
arr[] = {6,5,7,1,8,2,9,9,7,7,9}
B = 6
Output: (1 1 1 1 1 1)
(1 1 1 1 2)
(1 1 2 2)
(1 5)
(2 2 2)
(6)

https://www.youtube.com/watch?v=irFtGMLbf-s

'''

def sumUtil(a,n,s,result,temp,index):
    # if we have exceeded sum,or no more element is left
    if(index>=n or s<0):
        return
    
    # if we reached the given sum
    if(s==0): 
        result.append(temp[:])
        return
    
    # append current element in our temp result
    temp.append(a[index])
    
    # recurse for lesser sum, with curr index
    sumUtil(a,n,s-temp[-1],result,temp,index)
    
    # pop last element added to temp for backtrack
    temp.pop()

    sumUtil(a,n,s,result,temp,index+1) # recurse for next position




def combinationalSum(a,s):
    '''
    :param a: given array a
    :param n: size of a
    :param s: given sum to be achieved
    :return: list containing list of numbers in ascending order, giving the combinational sum
    '''
    # put it in set
    a=set(a)
    
    # removed duplicates from array a
    a=list(a)
    
    # sort to maintain order
    a.sort() 
    result = []
    
    # initial index is 0
    sumUtil(a,len(a),s,result,[],0) 
    
    # return result
    return result 