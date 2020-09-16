'''
Given a string S of lowercase aplhabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow.
Each test case consist of one string in 'lowercase' only, in a separate line.

Output:
For each testcase, in a new line, Print 1 if string is Isogram else print 0.

Your Task:
This is a function problem. You only need to complete the function isIsogram() that takes string as parameter and returns either true or false.

Constraints:
1 <= T <= 100
1 <= |S| <= 103

Example:
Input:
2
machine
geeks
Output:
1
0

Explanation:
Testcase 1: machine is an isogram as no letter has appeared twice. Hence we print 1.
Testcase 2: geeks is not an isogram as 'e' appears twice. Hence we print 0.

'''
#you can also consider using ord() function
def isIsogram(s):
    hm = {}
    
    for i in s:
        if(i not in hm):
            hm[i] = 1
        else:
            hm[i] += 1
            
    print(hm)
    
    for k, v in hm.items():
        if(v > 1):
            return False
    return True
    
    
s = "abcdefabcdef"
res = isIsogram(s)
if(res == True):
    print(1)
else:
    print(0)