'''
print index of first occurrence of element.

sample input:
print index of first occurrence of element 2 from array [1,2,3,4,2,7,8,3]

sample output:
1
'''
def firstOccurrence(arr, idx, element):
    
    if(idx == len(arr) - 1):
        return -1
    
    elif(arr[idx] == element):
        return idx
    
    else:
        fi = firstOccurrence(arr, idx+1, element)
        return fi
    
print(firstOccurrence([1,2,3,4,2,7,8,3], 0, 3))