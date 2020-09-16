'''
Hashing is very useful to keep track of the frequency of the elements in a list.

You are given an array arr of size n. You need to print the distinct elements as they appear in the array.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input.
The first line contains n denoting the size of the array. The second line contains n elements of the array.

Output:
For each testcase, in a new line, print the distinct elements in the order they appear in the array.

Constraints:
1 <= T <= 100
1 <= n <= 103
0 <= arri <= 107

Examples:
Input:
1
10
1 1 2 2 3 3 4 5 6 7
Output:
4 5 6 7

'''
def printDistinct(arr, n):
    
    hm = {}
    
    for i in arr:
        if i not in hm:
            hm[i] = 1
        else:
            hm[i] += 1
            
    for k, v in hm.items():
        if(v == 1):
            print(k)
    
    
arr = [1,1,2,2,3,3,4,5,6,7]
n = len(arr)
printDistinct(arr, n)