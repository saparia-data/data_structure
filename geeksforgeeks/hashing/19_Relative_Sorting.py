'''
Given two arrays A1[] and A2[] of size N and M respectively. 
The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2. 
For the elements not present in A2, append them at last in sorted order. 
It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.

Note: Expected time complexity is O(N log(N)).

Input:
First line of input contains number of testcases. For each testcase, 
first line of input contains length of arrays N and M and next two line contains N and M elements respectively.

Output:
Print the relatively sorted array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N,M  ≤ 106
1 ≤ A1[], A2[] <= 106

Example:
Input:
2
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
8 4
2 6 7 5 2 6 8 4 
2 6 4 5
Output:
2 2 1 1 8 8 3 5 6 7 9
2 2 6 6 4 5 7 8

Explanation:
Testcase 1: After sorting the resulted output is 2 2 1 1 8 8 3 5 6 7 9.
Testcase 2: After sorting the resulted output is 2 2 6 6 4 5 7 8.

https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/

'''
#time complexity is O(n2)
def relativeSortArray(arr1, arr2):
    
    mp = {}
    
    for i in arr1:
        if i not in mp:
            mp[i] = 1
        else:
            mp[i] += 1
            
    print(mp)
    
    result = []
    temp = []
    for i in arr2:
        for j in range(mp[i]):
            result.append(i)
        mp[i] = 0
        
        
    for k, v in mp.items():
        if v:
            for i in range(v):
                temp.append(k)
                
    temp.sort()
    result.extend(temp)
    
    return result
            
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
n = len(arr1)
m = len(arr2)
print(relativeSortArray(arr1, arr2))