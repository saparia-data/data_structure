'''
Given an array and an element, print all indices of an element in an array.

sample input:

arr = [1,2,3,4,6,3,4,3]

sample output:

All indices of element 3 are : 2,5,7

https://www.youtube.com/watch?v=bQkwHBaNioE&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=24

'''

def allIndices(arr, idx, fsf, element):
    
    if(idx == len(arr)):
        # return array of length as many times element is present
        return [0] * fsf
    
    if(arr[idx] == element):
        # if element found increment fsf variable and do recursive call
        lst = allIndices(arr, idx+1, fsf+1, element)
        lst[fsf] = idx
        return lst
    else:
        # if element not equal to current element make recursive call without incrementing fsf variable
        lst = allIndices(arr, idx+1, fsf, element)
        return lst
    
print(allIndices([1,2,3,4,6,3,4,3], 0, 0, 3))
    
    