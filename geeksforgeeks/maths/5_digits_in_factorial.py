'''
Given an integer N. The task is to find the number of digits that appear in its factorial, where factorial is defined as, factorial(n) = 1*2*3*4……..*N 
and factorial(0) = 1.

Input Format:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow.
Each test case consist of one line. The first line of each test case consists of an integer N.

Output Format:
Corresponding to each test case, in a new line, print the number of digits that appear in its factorial.

Your Task:
This is a function problem. You only need to complete the function digitsInFactorial() that takes N as parameter and returns number of digits in factorial of N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 104

Example:
Input:
2
5
120

Output:
3
199

Explanation:
Testcase 1: Factorial of 5 is 120. Number of digits in 120 is 3 (1, 2, and 0).

Hints:
1) When you need to calculate the digits of some number X. You do 10k=X. As 10 to power k tells us the k(digits).
The above point can easily be understood if you see that 104=10000 has (4+1) digits.

2) Let's take 10!=10x to get the value of x.

Take log both sides log(10)!=xlog10

log(10*9*8*..*1)=x

log10+log9+log8+...+log1=x

Take the floor of sum and add 1 to get the number of digits.

def digitsInFactorial(N):
'''
from math import log10, floor
def digitsInFactorial(N):
    f = 1
    while(N>1):
        f = f * N
        N = N - 1
    return floor(log10(f) + 1)

print(digitsInFactorial(4))
    
    
    
    
    
    

