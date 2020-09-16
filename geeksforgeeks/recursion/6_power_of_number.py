'''
Given a number N, let the reverse of the number be R. The task is to print the output of the Expression power(N,R), 
where pow function represents N raised to power R.
Note: As answers can be very large, print the result modulo 1000000007.

Input Format:
The first line of the input consists of an integer T denoting the number of test cases. Then T test cases follow. 
Each test case consists of a single line containing an integer N.

Output Format:
Corresponding to each test case, print in a new line, the output of the expression pow as described above.

Your Task:
This is a function problem. You just need to complete the function pow that takes two parameters N and R and returns power of (N to R)mod(1000000007)

Constraints:
1 <= T <= 103
1 <= N <= 105

Example:
Input:
2
2
12

Output:
4
864354781

Explanation:
Testcase 1: The reverse of 2 is 2 and after raising power of 2 by 2 we get 4 which gives remainder as 4 by dividing 1000000007.

Hints:

1) Try using modulus property with fast exponentian:

Property 1:
(m * n) % p has a very interesting property:
(m * n) % p =((m % p) * (n % p)) % p

Property 2:
if b is even:
(a ^ b) % c = ((a ^ b/2) * (a ^ b/2))%c ? this suggests divide and conquer
if b is odd:
(a ^ b) % c = (a * (a ^( b-1))%c

Property 3:
If we have to return the mod of a negative number x whose absolute value is less than y:
then (x + y) % y will do the trick

Note:
Also as the product of (a ^ b/2) * (a ^ b/2) and a * (a ^( b-1) may cause overflow, hence we must be careful about those scenarios

def power(N,R):
'''
from math import pow
def numRev(n):
    
    num = n
    rev = 0
    
    if(n < 0):
        return n
    else:
        while(num > 0):
            rev = (num % 10) + (rev * 10)
            num = num // 10
    return rev


def power(N,R):
    
    if(N < 0):
        return pow(N, R)
    else:
        #revR = numRev(R)
        return int((pow(N, R) % 1000000007))
    
print(power(12, 21))


           
           
           
            






