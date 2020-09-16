'''
Print numbers from 1 to N without the help of loops.

Input Format: 
The first line of the input contains T, denoting the number of testcases. First line of test case contains an integer N.

Output Format: 
For each test case, print numbers from 1 to N in newline.

Your Task:
This is a function problem. You only need to complete the function printNos that takes N as parameter and prints number from 1 to N recursively. The driver code adds the newline automatically after the function call.

Constraints:
1 <= T <= 100
1 <= N <= 990

Example:
Input:
2
10
5

Output:
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5
'''

def printNos(N):
    
    if(N > 0):    
        printNos(N-1)
        print(N, end=' ')
    else:
        return
        
printNos(5)
print("\n\n")
#program using tail recursion
def printNOS(n, k=1):
    
    if(n <= 0):
        return
    else:
        print(k)
        printNOS(n - 1, k + 1)
        
printNOS(5, 1)
print("\n\n")

def P1N(n):
    
    if(n == 0):
        return
    else:
        P1N(n-1)
        print(n)
        
P1N(4)
    
    
    
    
        
        
        
    