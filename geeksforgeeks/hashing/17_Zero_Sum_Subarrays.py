'''
You are given an array A of size N. You need to print the total count of sub-arrays having their sum equal to 0

Input:
First line of the input contains an integer T denoting the number of test cases. Each test case consists of two lines. First line of each test case contains an Integer N denoting the size of the array, and the second line contains N space separated integers.

Output:
For each test case, in a new line, print the total number of subarrays whose sum is equal to 0.

Constraints:    
1 <= T <= 100
1 <= N <= 107
-1010 <= Ai <= 1010

Example:
Input:
2
6
0 0 5 5 0 0
10
6  -1 -3 4 -2 2 4 6 -12 -7
Output:
6
4

Explanation:
Testcase 1: There are 6 subarrays present whose sum is zero. The starting and ending indices are:
(0,0) (1,1) (0,1) (4,4) (5,5) (4,5)
Testcase 2: There are 4 subarrays present whose sum is zero. The starting and ending indices are:
(1,3) (4,5) (1,5) (5,8)

https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

'''
def findSubArrays(arr,n):
    
    hashMap = {}
    out = []
    
    sum1 = 0
    for i in range(n):
        
        sum1 += arr[i]
        
        if(sum1 == 0):
            out.append((0, i))
        
        al = []
        
        if sum1 in hashMap:
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
                
        al.append(i)
        hashMap[sum1] = al
    return out
                   
    
arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7] 
n = len(arr)
print(findSubArrays(arr, n)) 