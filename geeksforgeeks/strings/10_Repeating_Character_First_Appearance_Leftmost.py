'''
You are given a string S (both uppercase and lowercase characters). You need to print the repeated character whose first appearance is leftmost.

Input:
The first line of input contains T denoting the number of testcases.
T testcases follow. Each testcase contains one line of input containing String S.

Output:
For each testcase, in a new line, print the character.

Your Task:
This is a function problem. You only need to complete the function repeatedCharacter()
that takes string as parameter and returns the index of the character. If no character repeats then return -1.

Constraints:
1 <= T <= 100
1 <= |S| <= 100

Examples:
Input:
2
geeksforgeeks
abcd
Output:
g
-1

Explanation:
Testcase1: We see that both e and g repeat as we move from left to right. But the leftmost is g so we print g.
Testcase2: No character repeats so we print -1.

hints:

We traverse the string from left to right. We keep track of the leftmost index of every character.
If a character repeats, we compare its leftmost index with current result and update the result if result is greater.

'''
#using array
def repeatingCharacter(s):
    occurences = [0 for i in range(256)]
    
    for i in s:
        occurences[ord(i)] += 1
        
    for i in s:
        if(occurences[ord(i)] > 1):
            return i
        
#using dict
def repeatingCharacter1(s):
    d = {}
    
    for i in s:
        if(i not in d):
            d[i] = 1
        else:
            d[i] += 1
            
    for i in s:
        if(d[i] > 1):
            return i       
    
s = "geeksforgeeks"
print(repeatingCharacter(s))
print(repeatingCharacter1(s))