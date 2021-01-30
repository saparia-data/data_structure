'''
You are given a number n. You need to find nth Fibonacci number.
F(n)=F(n-1)+F(n-2); where F(1)=1 and F(2)=1

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

Output Format:
For each testcase, in a newline, print F(n).

Your Task:
This is a function problem. You only need to complete the function fibonacci that takes n as parameters and returns F(n).

Constraints: 
1 <= T <= 100
1 <= n <= 20

Examples:
Input:
2
1
20
Output:
1
6765

Hints:

1)
fibonacci(n)
    if(n==1||n==2)
    return 1
    else
    return fibonacci(n-1)+fibonacci(n-2)
 

def fibonacci(n):
'''

def fibonacci(n):
    
    if(n == 1 or n == 2):
        return 1
    elif(n == 0):
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    
def fibonacci2(n):
    
    if(n == 0 or n == 1):
        return n
    
    fibonm1 = fibonacci2(n - 1)
    fibonm2 = fibonacci2(n - 2)
    fibon = fibonm1 + fibonm2
    return fibon
    
print(fibonacci(20))
print(fibonacci2(20))