'''
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Input Format:
First line contains an integer, the number of test cases 'T'. T testcases follow. 
Each test case in its first line contains two positive integer A and B (First 2 terms of GP). 
In the second line of every test case it contains of an integer N.

Output Format:
In each seperate line print the Nth term of the Geometric Progression. Print the floor ( floor(2.3)=2 ) of the answer.

Your Task:
This is a function problem. You need to complete the function termOfGP() that takes A and B as parameter and returns Nth term of GP. 
The return value should be double that would be automatically converted to floor by the driver code.

Constraints:
1 <= T <= 100
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

Example:
Input:
2
2 3
1
1 2
2

Output:
2
2

Explanation:
Testcase 2: The second term of series whose common ratio is 2 will be 2.

Hints:
1) Gp series is a, ar, ar2, ar3.. and so on
2) Nth term of gp is given by an=arn-1
ratio is given by r= (n+1)term/(n)term

def termOfGP(A,B,N):
'''
import math
def termOfGP(A,B,N):
    r = B/A
    return math.floor(A * (pow(r,N-1)))

print(termOfGP(1, 2, 2))
    
    
    
    
    
    