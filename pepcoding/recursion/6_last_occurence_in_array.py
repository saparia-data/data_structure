'''
print last occurence index of an element

sample input:
arr = [2,3,4,3,6,7,3,8]

sample output:
last occurence index of element 3 is : 6

'''

def lastOccurence(arr, idx, x):
    
    if(idx == len(arr)):
        return -1
    
    last_idx = lastOccurence(arr, idx+1, x)
    
    if(last_idx == -1):
        
        if(arr[idx] == x):
            return idx
        else:
            return -1
        
    else:
        return last_idx
    
    
print(lastOccurence([2,3,4,3,6,7,3,8], 0, 3))