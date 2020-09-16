'''
https://www.geeksforgeeks.org/remove-duplicates-sorted-array/

time complexity -> O(n)
space complexity -> O(1)

'''

def removeDuplicates(arr, n):
    
    j=0
    
    for i in range(n-1):
        if(arr[i] != arr[i+1]):
            arr[j] = arr[i]
            j += 1
            
    arr[j] = arr[n-1]
    j += 1
    return j

arr = [1,1,1,2,2,2,3,3,4,5,5,5]
n = len(arr)
j = removeDuplicates(arr, n)
#print(j)

for i in range(j):
    print(arr[i])