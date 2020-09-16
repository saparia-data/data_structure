'''
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

Input:
First line of input contains of an integer 'T' denoting number of test cases then T test cases follow . 
Each testcase contains a String 'S'.

Output:
For each test case print in a new line 1 if its a pangram else print 0 .

Your Task:
This is a function problem. You need to complete the function checkPanagram 
that takes string as parameter and returns true if string is panagram, else it returns false.

Constraints:
1 <= T <= 100
1 <= |S| <= 104

Example:
Input:
2
Bawds jog, flick quartz, vex nymph
sdfs
Output:
1
0

Explanation :
Testcase 1: In the given input , there are all the letters of the english alphabet.Hence, the output is 1.
Testcase 2: In the given input , there aren't all the letters present in the english alphabet. Hence, the output is 0.

hints:
-Lowercase and Uppercase are considered the same. So 'A' and 'a' are marked in index 0 and similarly 'Z' and 'z' are marked in index 25.
-After iterating through all the characters check whether all the characters are marked or not. 
-If not then return false as this is not a pangram else return true.

'''
def checkPanagram(s):
    marked = [0 for i in range(26)]
    
    for ch in s:
        if(ord(ch) <= ord('Z') and ord(ch) >= ord('A')):
            marked[ord(ch) - ord('A')] = 1
        elif(ord(ch) <= ord('z') and ord(ch) >= ord('a')):
            marked[ord(ch) - ord('a')] = 1
            
    for i in range(26):
        if(not marked[i]):
            return False
    return True

s = "Bawds jog, flick quartz, vex nymph"
print(checkPanagram(s))