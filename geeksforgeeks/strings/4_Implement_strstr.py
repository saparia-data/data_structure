'''
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s.

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. The first line of each test case contains two strings s and x.

Output:
For each test case, in a new line, output will be an integer denoting the first occurrence of the x in the string s.
Return -1 if no match found.

Your Task:
Since this is a function problem, you don't have to take any input. Just complete the strstr() function.
The function returns -1 if no match if found else it returns an integer denoting the first occurrence of the x in the string s.

Note : Try to solve the question in constant space complexity.

Constraints:
1 <= T <= 200
1 <= |s|,|x| <= 1000

Example:
Input
2
GeeksForGeeks Fr
GeeksForGeeks For
Output
-1
5

Explanation:
Testcase 1: Fr is not present in the string GeeksForGeeks as substring.
Testcase 2: For is present as substring in GeeksForGeeks from index 5.

hints:

A simple solution is to one by one check every index of s1. For every index, check if s2 is present. O(n*m)
For the efficient solution, we  can use KMP algorithm, Z algorithm, Rabin-Karp Algorithm

'''
def strstr(s,p):
    m = len(p)
    n = len(s)
    
    for i in range(n-m+1):
        j = 0
        for j in range(m):
            if(s[i+j] != p[j]):
                break
            j += 1
            
        if(j==m):
            return i
    return -1
    
    
s = "geeksforgeeks"
p = "for"
print(strstr(s, p))