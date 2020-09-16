'''
You are given two numbers n and p. You need to find np.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n and p.

Output:
For each testcase, in a newline, print np.

Your Task:
This is a function problem. You only need to complete the function RecursivePower that takes n and p as parameters and returns np.

Constraints:
1 <= T <= 80
1 <= n, p <= 9

Examples:
Input:
2
9 9
2 9
Output:
387420489‬
512

Explanation:
Testcase 1: 387420489 is the value obtained when 9 is raised to the power of 9.
Testcase 2: 512 is the value obtained when 2 is raised to the power of 9.

Hints:

1) write a recursive function 

step1. if power is zero return 1

step 2. return number multiplied by recursive call to power-1

def RecursivePower(n,p):
'''

def RecursivePower(n,p):
    
    if(p == 1):
        return n
    else:
        return n * RecursivePower(n, p - 1)
    
print(RecursivePower(2, 4))
print(RecursivePower(9, 9))
    
    
    
    
    