'''
print array content in reverse order

'''

def printArrayReverse(arr, idx):
    
    if(idx == len(arr)):
        return
    
    printArrayReverse(arr, idx+1)
    print(arr[idx])
    
printArrayReverse([1,2,3,4,5], 0)