'''
Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays in place,
i. e., we need to consider all n + m elements in sorted order,
then we need to put first n elements of these sorted in first array and remaining m elements in second array.

Note: Expected time complexity is O((n+m) log(n+m)). DO NOT use extra space.  We need to modify existing arrays as following.

Input: arr1[] = {10};
       arr2[] = {2, 3};
Output: arr1[] = {2}
        arr2[] = {3, 10}  

Input: arr1[] = {1, 5, 9, 10, 15, 20};
       arr2[] = {2, 3, 8, 13};
Output: arr1[] = {1, 2, 3, 5, 8, 9}
        arr2[] = {10, 13, 15, 20} 
Input:
First line contains an integer T, denoting the number of test cases. First line of each test case contains two space separated integers X and Y, 
denoting the size of the two sorted arrays. Second line of each test case contains X space separated integers, 
denoting the first sorted array P. Third line of each test case contains Y space separated integers, denoting the second array Q.

Output:
For each test case, print (X + Y) space separated integer representing the merged array.

Your Task:
This is a function problem. You only need to complete the function merge() that takes n and m as parameters.

Constraints:
1 <= T <= 100
1 <= X, Y <= 5*104
0 <= arr1i, arr2i <= 109

Example:
Input:
2
4 5
1 3 5 7
0 2 6 8 9
2 3
10 12
5 18 20
Output:
0 1 2 3 5 6 7 8 9
5 10 12 18 20

Explanation:
Testcase 1: After merging two non-decreasing arrays, we have, 0 1 2 3 5 6 7 8 9.
Testcase 2: After merging two sorted arrays , we have 5 10 12 18 20.

hints:

https://www.youtube.com/watch?v=NWMcj5QFW74


'''

def merge(ar1, ar2, m, n):
    
    for i in range(n-1, -1, -1):
        last = ar1[m-1]
        j = m-2
        
        while(j >0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j -= 1
            
        if(j != m-2 or last > ar2[i]):
            ar1[j+1] = ar2[i]
            ar2[i] = last
            
            
ar1 = [1, 5, 9, 10, 15, 20] 
ar2 = [2, 3, 8, 13] 
m = len(ar1) 
n = len(ar2) 

merge(ar1, ar2, m, n)
print(ar1)
print(ar2)