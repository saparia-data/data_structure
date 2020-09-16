'''
It can be optimized by stopping the algorithm if inner loop didn't cause any swap.
'''

def bubbleSort(arr, n):
    
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            #print(arr)
                
        if(swapped == False):
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

print(bubbleSort(arr, n))