'''
Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.

Example 1:
Input:
N = 5
Output: 1 1 2 3 5

'''

def printFibb(n):
    res = []
    a=b=1
    if n>=1:
        res.append (1)
    if n>=2:
        res.append (1)
        
        
    for i in range(2,n):
        res.append (a+b)
        c=a+b
        a=b
        b=c
    return res