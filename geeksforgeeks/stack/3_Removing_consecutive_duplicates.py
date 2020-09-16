'''
Stacks can be used to remove duplicate characters from a string that are stacked next to each other. For example, 
we take the string aabbccccc and convert it into abc. We can push the first character into a stack 
and skip if the top of the stack is equal to the current character.
You are given a string str. You need to remove the consecutive duplicates.

Input:
The first line of input contains T denoting the number of test cases. T test cases follow. 
Each testcase contains one line of input containing string str.

Output:
For each testcase, in a new line, print the modified string.

Your Task:
This is a function problem. You need to complete the function removeConsecutiveDuplicates() that takes a string as a parameter 
and returns the modified string. The printing is done automatically by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= |str| <= 103

Examples:
Input:
2
aaaaaabaabccccccc
abbccbcd
Output:
ababc
abcbcd

Explanation:
Testcase 1: Removing all consecutive duplicates, we have no duplicates consecutively.
Testcase 2: Removing all the consecutive duplicates, we have the output as abcbcd.

hints:
-Push the first character into a stack and skip if the top of the stack is equal to current character.

'''
def removeConsecutiveDuplicates(s):
    
    stack = []
    
    stack.append(s[0])
    curr_index = 1
    
    while(curr_index < len(s)):
        if(s[curr_index] == stack[-1]):
            pass
        else:
            stack.append(s[curr_index])
        curr_index += 1
        
    ans = ""
    
    for char in stack:
        ans += char
        
    return ans

s = ['a','a','b','b','b','d','d','d','d']
print(removeConsecutiveDuplicates(s))