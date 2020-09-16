'''
https://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/
'''
def maxFromRight(arr, size):
    
    max_from_right = arr[size - 1]
    arr[size - 1] = -1
    
    for i in range(size - 2, -1, -1):
        temp = arr[i]
        
        arr[i] = max_from_right
        #print(arr)
        
        if(max_from_right < temp):
            max_from_right = temp
        
    
    print(arr)
    
arr = [16, 17, 4, 3, 5, 2] 
size = len(arr)
maxFromRight(arr, size)