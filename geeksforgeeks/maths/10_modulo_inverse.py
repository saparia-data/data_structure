'''
Given two integers ‘a’ and ‘m’. The task is to find modular multiplicative inverse of ‘a’ under modulo ‘m’.

Note: Print the smallest modular multiplicative inverse.

Input Format:
First line consists of T test cases. Only line of every test case consists of 2 integers 'a' and 'm'.

Output Format:
For each testcase, in a new line, print the modular multiplicative inverse if exists else print -1.

Your Task:
This is a function problem. You just need to complete the function modInverse that takes a and m as parameters
and returns modular multiplicative inverse of ‘a’ under modulo ‘m’.

Constraints:
1 <= T <= 100
1 <= m <= 100
1 <= a <= m

Example:
Input:
2
3 11
10 17

Output:
4
12

Explanation:
Testcase1:
Input:  a = 3, m = 11
Output: 4
Since (4*3) mod 11 = 1, 4 is modulo inverse of 3
One might think, 15 also as a valid output as "(15*3) mod 11" 
is also 1, but 15 is not in ring {0, 1, 2, ... 10}, so not valid.

Hints:
1) a x ≡ 1 (mod m)
The value of x should be in {0, 1, 2, … m-1}, i.e., in the ring of integer modulo m.
The multiplicative inverse of “a modulo m” exists if and only if a and m are relatively prime (i.e., if gcd(a, m) = 1).

2) A Naive method is to try all numbers from 1 to m. For every number x, check if (a*x)%m is 1.

def modInverse(a,m):
'''
def modInverse(a,m):
    
    for i in range(1, m):
        if((a * i) % m == 1):
            return i
    
    return -1
    
