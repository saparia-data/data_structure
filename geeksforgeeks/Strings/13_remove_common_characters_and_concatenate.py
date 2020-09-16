'''
Given two strings s1 and s2. Modify string s1 such that all the common characters of s1 and s2 is to be removed 
and the uncommon characters of s1 and s2 is to be concatenated.
Note: If no modification is possible print -1.

Input:
The first line consists of an integer T i.e number of test cases. 
The first line of each test case consists of a string s1.The next line consists of a string s2. 

Output:
Print the concatenated string.

User Task:
The task is to complete the function concatenatedString() which removes the commong characters, concatenates, and returns the string.

Constraints: 
1 <= T <= 200
1 <= |Length of Strings| <= 104

Example:
Input:
2
aacdb
gafd
abcs
cxzca
Output:
cbgf
bsxz

Explanation:
Testcase 1:The common characters of s1 and s2 are: a, d.The uncommon characters of s1 and s2 are: c, b, g and f. 
Thus the modified string with uncommon characters concatenated is: cbgf.

Testcase 2: The common characters of s1 and s2 are: a,c . The uncommon characters of s1 and s2 are: b,s,x and z.
Thus the modified string with uncommon characters concantenated is: bsxz.

hints:

1)
The idea is to use an array of size 26 (or a hash) where key is character and value is number of strings in which character is present. 
If a character is present in one string, then count is 1, else if character is present in both strings, count is 2.

2)
-Initialize result as empty string.
-Push all characters of 2nd string in map with count as 1.
-Traverse first string and append all those characters to result that are not present in map. Characters that are present in map, make count 2.
-Traverse second string and append all those characters to result whose count is 1.

'''
def concatenatedString(s,p):
    
    res = ""
    
    for i in s:
        if(i in p):
            continue
        else:
            res += i
            
    for j in p:
        if(j in s):
            continue
        else:
            res += j
            
    if(len(res)):
        return res
    return -1

#Another method
def concatenatedString1(s,p):
    occurrence_s=[0 for i in range(256)]
    occurrence_p=[0 for i in range(256)]
    
    # storing the count of chars in s1
    for i in range(len(s)):
        occurrence_s[ord(s[i])]+=1
        
    # storing the count of chars in p
    for i in range(len(p)):
        occurrence_p[ord(p[i])]+=1
    
    concatenated_str=""
    
    # Find characters of s1 that are not
    # present in s2 and append to result
    for i in range(len(s)):
        if(occurrence_p[ord(s[i])]==0):
            concatenated_str+=s[i]
    
    # Find characters of s2 that are not 
    # present in s1.
    for i in range(len(p)):
        if(occurrence_s[ord(p[i])]==0):
            concatenated_str+=p[i]
            
    if(len(concatenated_str)):
        return concatenated_str
    return -1

s = "abcs"
p = "cxzca"
print(concatenatedString(s, p))
print(concatenatedString1(s, p))