'''
Given an array of integers. Find the minimum number of swaps required to sort the array in non-decreasing order.

https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
https://levelup.gitconnected.com/graphs-everywhere-finding-the-minimum-swaps-required-to-sort-an-array-b8dea0a3af52

'''

def minSwaps(a,n):
    arrPos = []

    for i in range(n):
        arrPos.append([a[i],i])
    
    print(arrPos)    
    arrPos.sort()
    print(arrPos)
    
    vis = [0 for i in range(n)]
    print(vis)
    
    ans = 0
    
    for i in range(n):
        if(vis[i] or arrPos[i][1] == i):
            continue

        cycle_size = 0
        j=i
        
        while(not vis[j]):
            vis[j] = 1
            j = arrPos[j][1]
            cycle_size += 1
            
        ans += cycle_size - 1
        
    return ans





arr = [1, 5, 4, 3, 2] 
n = len(arr)
print(minSwaps(arr, n))