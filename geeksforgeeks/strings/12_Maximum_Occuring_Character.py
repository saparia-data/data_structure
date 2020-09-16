'''
Given a string str. The task is to find the maximum occurring character in the string str.
If more than one character occurs maximum number of time then print the lexicographically smaller character.

Input:
The first line of input contains an integer T denoting the number of test cases.
Each test case consist of a string in 'lowercase' only in a separate line.

Output:
For each testcase, in a new line, print the lexicographically smaller character which occurred the maximum number of time.

User Task:
The task is to complete the function getMaxOccuringChar() which returns the character which is most occuring.

Constraints:
1 ≤ T ≤ 30
1 ≤ |s| ≤ 100

Example:
Input:
2
testsample
output
Output:
e
t

Explanation:
Testcase 1: e is the character which is having highest frequency.
Testcase 2: t and u are the characters with the same frequency, but t is lexicographically smaller.


'''
def getMaxOccurringChar(s):
    
    occurences=[0 for i in range(256)]
    
    for char in s:
        occurences[ord(char)] += 1
    
    max_occurence=0
    character='~'
    
    #we are iterating upto 256 because we want lexicographically smaller character of occurences of two character is same
    for i in range(256):
        if(occurences[i] > max_occurence):
            character = chr(i)
            max_occurence = occurences[i]
    return character
    
    
s = "testsample"
print(getMaxOccurringChar(s))