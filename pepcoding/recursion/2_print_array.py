'''
You are required to print the elements of array from beginning to end each in a separate line.

'''

def printArray(arr, idx):
    
    if(idx == len(arr)):
        return
    
    print(arr[idx])
    printArray(arr, idx+1)
    
printArray([1,2,3,4,5], 0)