'''
You are given a number n. You need to find the digital root of n.
DigitalRoot of a number is the recursive sum of its digits until we get a single digit number.
Eg.DigitalRoot(191)=1+9+1=>11=>1+1=>2

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

Output Format:
For each testcase, in a newline, print the digital root of n.

Your Task:
This is a function problem. You only need to complete the function digitalRoot that takes n as parameter and returns the digital root of n.

Constraints: 
1 <= T <= 100
1 <= n <= 107

Examples:
Input:
2
1
99999
Output:
1
9

Hints:

1) You need two recursive function. One that calculates the sum of digits, and other that calls sum of digits as n so as we calculate the answer.
2)
sumDigits(n)
    if(n/10 is 0)
    return n
    else
    return n%10+sumDigits(n/10)

digitalRoot(int n)

    if(n/10 is 0)
    return n
    else
    return digitalRoot(sumDigits(n)) 

def digitalRoot(n):
    :param n: given number 
    :return: digital root as defined
'''

def sumOfDigits(n):
    
    if((n // 10) == 0):
        return n
    else:
        return n % 10 + sumOfDigits(n // 10) 
    
def digitalRoot(n):
    
    if((n // 10) == 0):
        return n
    else:
        return digitalRoot(sumOfDigits(n))


print(digitalRoot(1234))





