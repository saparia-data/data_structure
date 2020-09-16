'''
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing characters.

Output:
For each test case, in a new line, output a single line containing the reversed String.

User Task:
The task is to complete the function reverseWords() which reverse words from the given string and prints the answer. 
The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= |S| <= 2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno
Output:
much.very.program.this.like.i
mno.pqr

Explanation:
Testcase 1: After reversing the whole string(not individual words), the input string becomes much.very.program.this.like.i.
Testcase 2: After reversing the whole string , the input string becomes mno.pqr.


'''
def reverseWords(s):
    words = []
    curr_word = ""
    rev_str = ""
    
    for i in range(len(s)):
        if(s[i] == "."):
            words.append(curr_word)
            curr_word = ""
        else:
            curr_word += s[i]
    words.append(curr_word)
    #print(words)
    
    for i in range(len(words)-1, -1, -1):
        rev_str += words[i]
        if(i):
            rev_str += "."
            
    return rev_str
        
    

    
s = "i.like.this.program.very.much"
print(reverseWords(s))