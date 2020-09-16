'''
You are given a number n. You need to find the sum of digits of n.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

Output Format:
For each testcase, in a newline, print the sum of digits of n.

Your Task:
This is a function problem. You only need to complete the function sumOfDigits that takes n as parameter and returns the sum of digits of n.

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
45

Hints:

1)
// f(234) = 2+3+4 = 9
f(n)
{
  if n is less than 10 return n
  else return units digits of n+ f(n/10)
}


def sumOfDigits(n):
    :param n: given number
    :return: sum of digits of n.

'''

def sumOfDigits(n):
    return 0 if n == 0 else int(n%10) + sumOfDigits(n/10)
    print("---------------------------------------")
    sum = 0
    if n == 0:
        return 0
    else:
        modu = int(n%10)
        sum  = modu + sumOfDigits(int(n/10))
        return sum
    

print(sumOfDigits(123))


def SD(n):
    
    if(n == 0):
        return 0
    else:
        return SD(n//10) + int(n%10)
    
print(SD(674))
    
    
    
    
    
    