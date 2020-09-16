'''
Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
Each testcase contains the string S.

Output:
For each testcase, print the first non repeating character present in string. Print -1 if there is no non repeating character.

Your Task:
This is a function problem. You only need to complete the function nonrepeatingCharacter()
that takes string S as parameter and returns the character. If there is no non repeating character then return '$' .
The driver code automatically appends a new line after function call.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input :
3
hello
zxvczbtxyzvy
xxyyzz
Output :
h
c
-1

Explanation:
Testcase 1: In the given string, first character which is non-repeating is h, as it appars first and there is no other 'h' in the string.
Testcase 2: In the given string, 'c' is the character which is non-repeating. 
Testcase 3: In the given string no character is there which is non-repeating.Hence, the output is -1.

'''
#we can also use dict to maintain count of each character
def nonrepeatingCharacter(s):
    occurences=[0 for i in range(256)]
    
    for char in s:
        occurences[ord(char)]+=1
    
    for i in range(len(s)):
        if(occurences[ord(s[i])]==1):
            return s[i]
    return '$'

s = "geeksforgeeks"
print(nonrepeatingCharacter(s))