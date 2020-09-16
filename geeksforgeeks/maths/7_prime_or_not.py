'''
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case should contain a positive integer N.

Output:
For each testcase, in a new line, print "Yes" if it is a prime number else print "No".

Your Task:
This is a function problem. You just need to complete the function isPrime that takes N as parameter and returns True if N is prime else returns false.
The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example: 
Input:
2
5
4

Output:
Yes
No

Explanation:
Testcase 1: 5 is the prime number as it is divisible only by 1 and 5.

Hints:
Count the number of factors. If the factors of a number is 1 and itself, then the number is prime.

You can check this optimally by iterating from 2 to sqrt(n) as the factors from 2 to sqrt(n) have multiples from sqrt(n)+1 to n.
So, by iterating till sqrt(n) only, you can check if a number is prime.

def isPrime(N):
'''
import math

def isPrime(N):
    
    if(N == 1):
        return True
    else:
        for i in range(2, int(math.sqrt(N)) + 1):
            if (N % i == 0):
                return False
    return True

print(isPrime(9))