'''
https://www.youtube.com/watch?v=gf7vdIin0dk

time complexity is O(n)
space complexity -> O(n)
'''

def removeDuplicates(arr, n):
    
    j = 0
    temp = [0] * len(set(arr))
    for i in range(n-1):
        
        if(arr[i] != arr[i+1]):
            temp[j] = arr[i]
            j += 1
    temp[j] = arr[n-1]
    return temp

arr = [1,1,1,2,2,2,3,3,4,5,5,5]
n = len(arr)
print(removeDuplicates(arr, n))

            
        