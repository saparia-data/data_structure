'''
Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. 
Every student is assigned to read some consecutive books. 
The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.

Example :

Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed 
in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113.

https://www.geeksforgeeks.org/allocate-minimum-number-pages/

'''
import sys

def summ(arr, start, end):
    
    s = 0
    for i in range(start, end+1):
        s = s + arr[i]
        
    return s

# recursive solution
def minPages(arr, n, k):
    
    if(k == 1):
        return summ(arr, 0, n-1)
    
    elif(n == 1):
        return arr[0]
    
    res = sys.maxsize
    
    for i in range(1, n):
        res = min(res, max(minPages(arr, i, k-1), summ(arr, i, n-1)))
        
    return res

arr = [10,20,30,40]
n = len(arr)
k = 2
print(minPages(arr, n, k))    

# DP based solution

def minPages_DP(arr, n, k):
    
    dp = [[0 for i in range(n+1)] for i in range(k+1)]
    print(dp)
    
    # if no. of student is 1
    for i in range(1, n+1):
        dp[1][i] = summ(arr1, 0, i-1)
        
    print(dp)
        
    # if no of book is 1
    for i in range(1, k+1):
        dp[i][1] = arr[0]
        
    print(dp)
        
    for i in range(2, k+1):
        for j in range(2, n+1):
            res = sys.maxsize
            for p in range(j):
                res = min(res, max(dp[i-1][p], summ(arr,p,j-1)));
        dp[i][j] = res
    
        
    print(dp)
    return dp[k][n]
    
    
arr1 = [12, 34, 67, 90]
n1 = len(arr1)
k1 = 2
print(minPages_DP(arr1, n1, k1))