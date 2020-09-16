'''
https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
'''

def printRepeating(arr, size):
    
    for i in range(0, size):
        
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]))
            
arr = [1, 2, 3, 1, 3, 6, 6] 
arr_size = len(arr) 
  
printRepeating(arr, arr_size)