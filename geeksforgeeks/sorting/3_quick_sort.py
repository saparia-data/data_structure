def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):
        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return (i+1)

def quickSort(arr, low, high):
    
    if(low < high):
        
        p = partition(arr, low, high)
        
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
        return arr
    
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
print(quickSort(arr,0,n-1))