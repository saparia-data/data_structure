'''
tapping rain water -> https://www.geeksforgeeks.org/trapping-rain-water/

'''
print("----------------------------------------O(n2)-------------------------------------------------------------------------------")
def trappingWater(arr,n):
    
    res = 0
    
    for i in range(n):
        
        left = arr[i]
        
        for j in range(i):
            left = max(left, arr[j])
            
        right = arr[i]
        
        for k in range(i + 1, n):
            right = max(right, arr[k])
            
        res = res + (min(left, right) - arr[i])
        
    return res
    

arr = [7,4,0,9]
n = len(arr)
print(trappingWater(arr,n))
print("----------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------O(n)------------------------------------------------------------------------")

def trappingWater2(arr,n):
    
    left = [0] * n
    right = [0] * n
    res = 0
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
        
    print(left)
    
    right[n-1] = arr[n-1]
    for j in range(n-2, -1, -1):
        right[j] = max(right[j+1], arr[j])
        
    print(right)
    
    for i in range(n):
        res = res + (min(left[i],right[i]) - arr[i])
       
    return res 
    
    
    
arr = [7,4,0,9]
n = len(arr)
print(trappingWater2(arr,n))