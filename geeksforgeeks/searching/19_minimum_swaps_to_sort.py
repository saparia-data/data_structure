'''
Given an array of N distinct elements A[ ]. The task is to find the minimum number of swaps required to sort the array. 
Your are required to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. 
Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .

Output:
For each test case in a new line output will be an integer denoting  minimum umber of swaps that are  required to sort the array.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[] <= 106

User Task:
Your task is to complete minSwaps() which should return number of swaps required to make the array elements sorted.

Example(To be used only for expected output):
Input:
2
4
4 3 2 1
5
1 5 4 3 2

Output:
2
2

Explanation:
Testcase 1: We need two swaps, swap 1 with 4 and 3 with 2 to make it sorted.

https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
https://www.youtube.com/watch?v=f7IIW0HVUcQ

'''
def minSwaps(a,n):
    
    arrPos = []
    
    for i in range(n):
        arrPos.append([a[i], i])
        
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
        j = i
        while(not vis[j]):
            vis[j] = 1
            j = arrPos[j][1]
            cycle_size += 1
        ans += cycle_size - 1
        
    return ans
            
 
#a = [1,5,4,3,2]
a = [0,2,3,4,1,6,5]
n = len(a)
print(minSwaps(a, n))