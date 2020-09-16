'''
Given a number N. The task is to generate and print all binary numbers with decimal values from 1 to N.

Input:
The first line of input contains an integer T denoting the number of test cases. 
There will be a single line for each testcase which contains N.

Output:
Print all binary numbers with decimal values from 1 to N in a single line.

Your Task:
This is a function problem. You only need to complete the function generate 
that takes N as parameter and returns vector of strings denoting binary numbers.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 ≤ T ≤ 106
1 ≤ N ≤ 106

Example:
Input:
2
2
5
Output:
1 10
1 10 11 100 101

Explanation:

Testcase 1: Binary numbers from 1 to 2 are 1 and 10.
Testcase 2: Binary numbers from 1 to 5 are 1 , 10 , 11 , 100 and 101.

hints:

-Use a queue and push 1 in it. Now while n-- is not zero keep on popping and printing the output. 
-Now, append 1 and 0 to the output and push in the queue and keep repeating the same.

'''
from queue import Queue

def GenerateBinary(n):
    
    res = []
    
    q = Queue()
    
    q.put("1")
    
    while(n > 0):
        
        n -= 1
        
        s1 = q.get()
        res.append(s1)
        
        #s2 = s1
        
        q.put(s1 + "0")
        q.put(s1 + "1")
        
    return res

print(GenerateBinary(5))