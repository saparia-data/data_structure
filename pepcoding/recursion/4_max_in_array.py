'''
print max value in array

'''

def arrayMax(arr, idx):
    
    if(idx == len(arr) - 1):
        return arr[idx]
    
    element = arrayMax(arr, idx+1)
    if(element > arr[idx]):
        maxx = element
    else:
        maxx = arr[idx]
        
    return maxx

print(arrayMax([20,10,5,40,45], 0))