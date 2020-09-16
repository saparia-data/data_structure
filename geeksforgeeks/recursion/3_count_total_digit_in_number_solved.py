'''
You are given a number n. You need to find the count of digits in n.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

Output Format:
For each testcase, in a newline, print the count of digits in n.

Your Task:
This is a function problem. You only need to complete the function countDigits that takes n as parameter and returns the count of digits in n.

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
5

Hints:

1)
// f(501287) = 6
f(n)
{
  if n is less than 10 return 1
  return 1 + f(n/10)
}

def countOfDigits(n):
    :param n: given number
    :return: count of digits of n.

'''

def countOfDigits(n):
    
    return 1 if n < 10 else 1 + countOfDigits(int(n/10))

print(countOfDigits(99999))