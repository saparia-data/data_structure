'''
Given a positive integer N. The task is to find factorial of N.

Input:
The first line contains an integer 'T' denoting the total number of test cases. T testcases follow. In each test cases, it contains an integer 'N'.

Output:
For each testcase, in a new line, print the factorial of N.

Your Task:
This is a function problem. You just need to complete the function factorial() that takes N as parameter and returns factorial of N.

Constraints:
1 <= T <= 100
0 <= N <= 18

Example:
Input:
2
1
4

Output:
1
24

Explanation:
Testcase 2: Factorial of 4 is 4 * 3 * 2 * 1 = 24.

Hints:
1)

def factorial(N):
'''
def factorial(N):
    f = 1
    while(N>=1):
        f = f * N
        N = N - 1
    return f

print(factorial(4))

def factorialRecursive(n):
    if(n == 0):
        return 1
    else:
        f = (n*factorialRecursive(n-1))
        return f

print(factorialRecursive(5))
    
    
    