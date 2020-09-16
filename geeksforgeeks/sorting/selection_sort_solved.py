'''
Selection sort algorithms_available
'''

def selectionSort(arr, n):
    
    for i in range(n):
        fp = i
        for j in range(i + 1, n):
            if(arr[fp] > arr[j]):
                arr[fp], arr[j] = arr[j], arr[fp]
                #print(arr)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

print(selectionSort(arr, n))